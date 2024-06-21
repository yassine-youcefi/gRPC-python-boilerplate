# gRPC-python-boilerplate

## Overview

This repository provides a boilerplate setup for a gRPC server implemented in Python. The goal is to offer a structured and easy-to-use template to quickly get started with gRPC development.

## Features

* gRPC server implementation in Python
* Example .proto file defining service and messages
* Basic server and client implementation
* Instructions for generating gRPC code from .proto files
* Docker support for containerized deployment

## Prerequisites

* Python 3.7+
* pip (Python package installer)
* gRPC tools (`grpcio`, `grpcio-tools`)
* Docker (optional, for containerization)

## Getting Started

1. Clone the Repository

```bash
git clone https://github.com/yourusername/gRPC-python-boilerplate.git
cd gRPC-python-boilerplate
```

2. Install Dependencies

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   pip install -r requirements.txt
   ```

* Download the [couchbase](https://www.couchbase.com/downloads/?family=couchbase-server) [server](https://www.couchbase.com/downloads/?family=couchbase-server) [community](https://www.couchbase.com/downloads/?family=couchbase-server) [version](https://www.couchbase.com/downloads/?family=couchbase-server).
  Post download, create a new cluster with a new bucket and user. Give
  the bucket name and username of your choice and use the same names
  (bucketname , username and password) in [.env](https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1) file.
* Install [grpc](https://pypi.org/project/grpc/), [grpcio-tools](https://pypi.org/project/grpcio-tools/),[couchbase](https://pypi.org/project/couchbase/), [load_dotenv](https://pypi.org/project/python-dotenv/) packages

---

> Genarate product_pb2.py and product_pb2_grpc.py :
>
> ```bash
> python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. protos/product.proto
> ```

#### product_pb2.py:

This file contains the classes for the message types defined in `.proto` file. It includes:

* **Classes for Messages** : For each message type in `.proto` file, there will be a corresponding class in `product_pb2.py`. These classes are used to serialize and deserialize the message types to and from binary format.
* **Serialization Methods** : Methods to serialize messages to binary format and parse messages from binary format.
* **Descriptors** : Metadata about the message types, including fields and their types.

For example, based on `product.proto`, `product_pb2.py` will include classes like `product`, `productId`, etc.

#### product_pb2_grpc.py:

This file contains the classes and methods for the gRPC service defined in `.proto` file. It includes:

* **Stub Classes** : These are client-side classes that contain methods corresponding to the RPC methods defined in the service. You use these stubs to call the RPC methods from the client code.
* **Servicer Classes** : These are server-side classes that you subclass to implement the RPC methods. You define the logic of your RPC methods in these subclasses.
* **Server Registration Functions** : Functions to add your service implementations to a gRPC server.

For example, based on `product.proto`, `product_pb2_grpc.py` will include:

* `productServiceStub` class: For the client to call RPC methods.
* `productServiceServicer` class: For the server to implement RPC methods.
* `add_productServiceServicer_to_server` function: To register the service implementation with a gRPC server.




## usage :

URL :` localhost:5001`

### **create product :** 

```json
{
"description":"t-shirt",
"price":1000,
"productName":"t-shirt nike",
"status":"active",
"tax":10
}
```

### create cart item :


```json
{
  "products":[
    {
      "productId":
      "ec630b78-19af-4969-8b39-12235e10e82b"
    }   
  ],
  "quantity":2
}
```

### get cart item :


```json
{
 "cartItemId":"50ba8e1a-c043-4c29-b87a-61b894b57480"
}
```
