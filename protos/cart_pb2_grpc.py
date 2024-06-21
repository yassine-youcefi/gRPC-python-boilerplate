# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from protos import cart_pb2 as cart__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in cart_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class cartServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.createCartItem = channel.unary_unary(
                '/cart.cartService/createCartItem',
                request_serializer=cart__pb2.cartItem.SerializeToString,
                response_deserializer=cart__pb2.cartItemId.FromString,
                _registered_method=True)
        self.updateCartItem = channel.unary_unary(
                '/cart.cartService/updateCartItem',
                request_serializer=cart__pb2.cartItem.SerializeToString,
                response_deserializer=cart__pb2.cartItemId.FromString,
                _registered_method=True)
        self.getCartByUserId = channel.unary_unary(
                '/cart.cartService/getCartByUserId',
                request_serializer=cart__pb2.userId.SerializeToString,
                response_deserializer=cart__pb2.cart.FromString,
                _registered_method=True)
        self.createCart = channel.unary_unary(
                '/cart.cartService/createCart',
                request_serializer=cart__pb2.cart.SerializeToString,
                response_deserializer=cart__pb2.cartId.FromString,
                _registered_method=True)
        self.getCart = channel.unary_unary(
                '/cart.cartService/getCart',
                request_serializer=cart__pb2.cartId.SerializeToString,
                response_deserializer=cart__pb2.cart.FromString,
                _registered_method=True)
        self.updateCart = channel.unary_unary(
                '/cart.cartService/updateCart',
                request_serializer=cart__pb2.cart.SerializeToString,
                response_deserializer=cart__pb2.cart.FromString,
                _registered_method=True)
        self.deleteCart = channel.unary_unary(
                '/cart.cartService/deleteCart',
                request_serializer=cart__pb2.cartId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class cartServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def createCartItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateCartItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getCartByUserId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createCart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getCart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateCart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteCart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_cartServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'createCartItem': grpc.unary_unary_rpc_method_handler(
                    servicer.createCartItem,
                    request_deserializer=cart__pb2.cartItem.FromString,
                    response_serializer=cart__pb2.cartItemId.SerializeToString,
            ),
            'updateCartItem': grpc.unary_unary_rpc_method_handler(
                    servicer.updateCartItem,
                    request_deserializer=cart__pb2.cartItem.FromString,
                    response_serializer=cart__pb2.cartItemId.SerializeToString,
            ),
            'getCartByUserId': grpc.unary_unary_rpc_method_handler(
                    servicer.getCartByUserId,
                    request_deserializer=cart__pb2.userId.FromString,
                    response_serializer=cart__pb2.cart.SerializeToString,
            ),
            'createCart': grpc.unary_unary_rpc_method_handler(
                    servicer.createCart,
                    request_deserializer=cart__pb2.cart.FromString,
                    response_serializer=cart__pb2.cartId.SerializeToString,
            ),
            'getCart': grpc.unary_unary_rpc_method_handler(
                    servicer.getCart,
                    request_deserializer=cart__pb2.cartId.FromString,
                    response_serializer=cart__pb2.cart.SerializeToString,
            ),
            'updateCart': grpc.unary_unary_rpc_method_handler(
                    servicer.updateCart,
                    request_deserializer=cart__pb2.cart.FromString,
                    response_serializer=cart__pb2.cart.SerializeToString,
            ),
            'deleteCart': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteCart,
                    request_deserializer=cart__pb2.cartId.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cart.cartService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cart.cartService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class cartService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def createCartItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cart.cartService/createCartItem',
            cart__pb2.cartItem.SerializeToString,
            cart__pb2.cartItemId.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def updateCartItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cart.cartService/updateCartItem',
            cart__pb2.cartItem.SerializeToString,
            cart__pb2.cartItemId.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def getCartByUserId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cart.cartService/getCartByUserId',
            cart__pb2.userId.SerializeToString,
            cart__pb2.cart.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def createCart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cart.cartService/createCart',
            cart__pb2.cart.SerializeToString,
            cart__pb2.cartId.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def getCart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cart.cartService/getCart',
            cart__pb2.cartId.SerializeToString,
            cart__pb2.cart.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def updateCart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cart.cartService/updateCart',
            cart__pb2.cart.SerializeToString,
            cart__pb2.cart.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def deleteCart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cart.cartService/deleteCart',
            cart__pb2.cartId.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
