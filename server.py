import os
from concurrent import futures
import grpc
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

import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProductServicer(product_pb2_grpc.productServiceServicer):

    def __init__(self):
        load_dotenv()
        self._cluster,self._connection = self.connectDB()

    def connectDB(self):
        conn_str = "couchbase://"+os.getenv("DB_HOST")
        try:
            cluster_opts = ClusterOptions(authenticator=PasswordAuthenticator(os.getenv("USERNAME"), os.getenv("PASSWORD")))
            cluster = Cluster(conn_str, cluster_opts)
        except CouchbaseException as error:
            print(f"Could not connect to cluster. Error: {error}")
            raise
        bucket = cluster.bucket(os.getenv("BUCKET"))
        collection = bucket.scope(os.getenv("SCOPE")).collection(os.getenv("COLLECTION"))
        return cluster,collection

    def createProduct(self, request, context):
        doc = MessageToDict(request)
        response = product_pb2.productId()
        try:
            logger.info("Inserting document", doc)
            self._connection.insert(request.productId, doc)
        except Exception as e:
            logger.error("Error inserting document", e)
            response.productId = "Exception Occured , Unable to Create Product"
            return response
        response.productId = request.productId
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
        response=ParseDict(doc,response)
        return response

    def updateProduct(self, request, context):
        doc = MessageToDict(request)
        logger.info("Updating document", doc)
        try:
            self._connection.replace(request.productId,doc)
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


class CartServicer(cart_pb2_grpc.cartServiceServicer):
    
        def __init__(self):
            load_dotenv()
            self._cluster,self._connection = self.connectDB()
    
        def connectDB(self):
            conn_str = "couchbase://"+os.getenv("DB_HOST")
            try:
                cluster_opts = ClusterOptions(authenticator=PasswordAuthenticator(os.getenv("USERNAME"), os.getenv("PASSWORD")))
                cluster = Cluster(conn_str, cluster_opts)
            except CouchbaseException as error:
                print(f"Could not connect to cluster. Error: {error}")
                raise
            bucket = cluster.bucket(os.getenv("BUCKET"))
            collection = bucket.scope(os.getenv("SCOPE")).collection(os.getenv("COLLECTION"))
            return cluster,collection
        
        def createCartItem(self, request, context):
            doc = MessageToDict(request)
            response = cart_pb2.cartItemId()
            
            try:
                logger.info("Inserting document", doc)
                self._connection.insert(request.cartItemId, doc)
            except Exception as e:
                logger.error("Error inserting document", e)
                response.cartItemId = "Exception Occured , Unable to Create Cart Item"
                return response
            response.cartItemId = request.cartItemId
            return response
        
        def updateCartItem(self, request, context):
            doc = MessageToDict(request)
            logger.info("Updating document", doc)
            try:
                self._connection.replace(request.cartItemId,doc)
            except Exception as e:
                logger.error("Error inserting document", e)
            return google.protobuf.empty_pb2.Empty()
        
        
        def getCartByUserId(self, request, context):
            query = "SELECT a.* FROM " + os.getenv("BUCKET") + " a WHERE a.userId = $1"
            try:
                result = self._cluster.query(query, request.userId)
            except Exception as e:
                logger.error("Error inserting document", e)
                response = cart_pb2.cart()
                response.cartId = "Exception Occured , Unable to Retrieve Cart"
                return response
            for cart in result.rows():
                response = cart_pb2.cart()
                response = ParseDict(cart, response)
                yield response
    
        def createCart(self, request, context):
            doc = MessageToDict(request)
            response = cart_pb2.cartId()
            try:
                logger.info("Inserting document", doc)
                self._connection.insert(request.cartId, doc)
            except Exception as e:
                logger.error("Error inserting document", e)
                response.cartId = "Exception Occured , Unable to Create Cart"
                return response
            response.cartId = request.cartId
            return response
    
        def getCart(self, request, context):
            response = cart_pb2.cart()
            try:
                result = self._connection.get(request.cartId)
            except Exception as e:
                logger.error("Error inserting document", e)
                response.cartId = "Exception Occured , Unable to Retrieve Cart"
                return response
            doc = result.content_as[dict]
            response=ParseDict(doc,response)
            return response
    
        def updateCart(self, request, context):
            doc = MessageToDict(request)
            logger.info("Updating document", doc)
            try:
                self._connection.replace(request.cartId,doc)
            except Exception as e:
                logger.error("Error inserting document", e)
            return google.protobuf.empty_pb2.Empty()
    
        def deleteCart(self, request, context):
            try:
                self._connection.remove(request.cartId)
            except Exception as e:
                logger.error("Error inserting document", e)
            return google.protobuf.empty_pb2.Empty()
    
        def getAllCarts(self, request, context):
            query = "SELECT a.* FROM " + os.getenv("BUCKET") + " a"
            try:
                result = self._cluster.query(query)
            except Exception as e:
                logger.error("Error inserting document", e)
                response = cart_pb2.cart()
                response.cartId = "Exception Occured , Unable to Retrieve All Carts"
                return response
            for cart in result.rows():
                response = cart_pb2.cart()
                response = ParseDict(cart, response)
                yield response
    

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    product_pb2_grpc.add_productServiceServicer_to_server(ProductServicer(), server)
    cart_pb2_grpc.add_cartServiceServicer_to_server(CartServicer(), server)
    server.add_insecure_port("[::]:5000")
    logger.info("Starting server. Listening on port 5001")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    main()