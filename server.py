import os
from concurrent import futures
import grpc
import uuid
from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster
from couchbase.exceptions import CouchbaseException
from couchbase.options import ClusterOptions
from dotenv import load_dotenv
import protos.product_pb2_grpc as product_pb2_grpc
import protos.cart_pb2_grpc as cart_pb2_grpc
from protos import cart_pb2
from protos import product_pb2
import google.protobuf.empty_pb2
from google.protobuf.json_format import MessageToDict, ParseDict
from couchbase.exceptions import (CouchbaseException,
                                  DocumentExistsException,
                                  DocumentNotFoundException,)

import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ProductServicer(product_pb2_grpc.productServiceServicer):

    def __init__(self):
        load_dotenv()
        self._cluster, self._connection = self.connectDB()

    def connectDB(self):
        conn_str = "couchbase://"+os.getenv("DB_HOST")
        try:
            cluster_opts = ClusterOptions(authenticator=PasswordAuthenticator(
                os.getenv("USERNAME"), os.getenv("PASSWORD")))
            cluster = Cluster(conn_str, cluster_opts)
        except CouchbaseException as error:
            print(f"Could not connect to cluster. Error: {error}")
            raise
        bucket = cluster.bucket(os.getenv("BUCKET"))
        collection = bucket.scope(os.getenv("SCOPE")).collection(
            os.getenv("COLLECTION"))
        return cluster, collection

    def createProduct(self, request, context):
        product_id = str(uuid.uuid4())
        doc = MessageToDict(request)
        logger.info(doc)

        response = product_pb2.productId()
        try:
            logger.info("Inserting document", doc)
            self._connection.insert(product_id, doc)
        except DocumentExistsException as e:
            logger.warning("Document already exists: %s", e)
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details("Document already exists")
            return product_pb2.productId()
        except Exception as e:
            logger.error("Error inserting document", e)
            response.productId = "Exception Occured , Unable to Create Product"
            return response
        response.productId = product_id
        return response

    def getProduct(self, request, context):
        response = product_pb2.product()
        try:
            result = self._connection.get(request.productId)
        except Exception as e:
            logger.error("Error inserting document", e)
            response.productId = "Exception Occured , Unable to Retrieve Product"
            return response
        doc = result.content_as[dict]
        response = ParseDict(doc, response)
        return response

    def updateProduct(self, request, context):
        doc = MessageToDict(request)
        logger.info("Updating document", doc)
        try:
            self._connection.replace(request.productId, doc)
        except Exception as e:
            logger.error("Error inserting document", e)
        return google.protobuf.empty_pb2.Empty()

    def deleteProduct(self, request, context):
        try:
            self._connection.remove(request.productId)
        except Exception as e:
            logger.error("Error inserting document", e)
        return google.protobuf.empty_pb2.Empty()

    def getAllProducts(self, request, context):
        query = "SELECT a.* FROM " + os.getenv("BUCKET") + " a"
        try:
            result = self._cluster.query(query)
        except Exception as e:
            logger.error("Error inserting document", e)
            response = product_pb2.product()
            response.productId = "Exception Occured , Unable to Retrieve All Products"
            return response
        for product in result.rows():
            response = product_pb2.product()
            response = ParseDict(product, response)
            yield response


class CartServicer(cart_pb2_grpc.CartServicerServicer):

    def __init__(self):
        load_dotenv()
        self._cluster, self._connection = self.connectDB()

    def connectDB(self):
        conn_str = "couchbase://"+os.getenv("DB_HOST")
        try:
            cluster_opts = ClusterOptions(authenticator=PasswordAuthenticator(
                os.getenv("USERNAME"), os.getenv("PASSWORD")))
            cluster = Cluster(conn_str, cluster_opts)
            logger.info("Connected to Couchbase cluster")
        except CouchbaseException as error:
            print(f"Could not connect to cluster. Error: {error}")
            raise
        bucket = cluster.bucket(os.getenv("BUCKET"))
        collection = bucket.scope(os.getenv("SCOPE")).collection(
            os.getenv("COLLECTION"))
        return cluster, collection

    def createCartItem(self, request, context):
        logger.info("Received request: %s", request)
        doc = MessageToDict(request)
        cart_item_id = str(uuid.uuid4())
        doc['cartItemId'] = cart_item_id
        logger.info("Converted request to dict: %s", doc)
        response = cart_pb2.cartItemId()

        try:
            logger.info("Inserting document")
            self._connection.insert(cart_item_id, doc)
        except DocumentExistsException as e:
            logger.warning("Document already exists: %s", e)
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details("Document already exists")
            return cart_pb2.cartItemId()
        except Exception as e:
            logger.error("Error inserting document: %s", e)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(
                "Exception Occurred, Unable to Create Cart Item")
            return cart_pb2.cartItemId()
        response.cartItemId = cart_item_id
        return response

    def getCartItem(self, request, context):
        logger.info("Received getCartItem request: %s", request)
        cart_item_id = request.cartItemId

        try:
            result = self._connection.get(cart_item_id)
            cart_item_dict = result.content_as[dict]
            cart_item = ParseDict(cart_item_dict, cart_pb2.cartItem())
        except DocumentNotFoundException as e:
            logger.warning("Document not found: %s", e)
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Cart item not found")
            return cart_pb2.cartItem()
        except Exception as e:
            logger.error("Error fetching document: %s", e)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(
                "Exception Occurred, Unable to fetch Cart Item")
            return cart_pb2.cartItem()

        return cart_item


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    product_pb2_grpc.add_productServiceServicer_to_server(
        ProductServicer(), server)
    cart_pb2_grpc.add_CartServicerServicer_to_server(CartServicer(), server)
    server.add_insecure_port("[::]:5000")
    logger.info("Starting server. Listening on port 5001")
    server.start()
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("Reloading server")
        server.stop(0)
        print("Server reloading successful")


if __name__ == "__main__":
    main()
