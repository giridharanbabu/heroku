import werkzeug
from flask import Flask, jsonify
import configparser
import json
from flask import request
from dynaconf import settings
from flask_restplus import Api, Resource, fields
from flask_cors import CORS
import utils.pymongoconnection
from loguru import logger
import pymongo
from bson import ObjectId


app = Flask(__name__)

CORS(app)

api = Api(app, openapi='3.0.0', title='Models',description='''Sample App''')
ns = api.namespace('appengine')

@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return 'bad request!', 400


@ns.route(settings.PRODUCTS)
class getproductlist(Resource):
    def get(self):
        '''
        List all available Products
        '''
        try:
            product=None
            connection = utils.pymongoconnection.config(section='pymongo')
            collection = connection['ProductDetails']['Products']
            products = collection.find()
            product_list =[]
            for product in products:
                product_list.append({ "_id": str(product['_id']), "item": product['item']})
                product = jsonify({"products":product_list})

            return product

        except Exception as e:
            api.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

# def to_bson(self, value):
#     """convert type to a mongodb type"""
#     return ObjectId(value)

@ns.route(settings.PRODUCTSDETAILS+'/<product_id>')
class getproductdetails(Resource):
    def get(self,product_id):
        '''
        List all available Products
        '''
        try:
            from functions.build_function import product_details
            bucket = product_details(product_id)
            bucket = {"product_details":bucket}




        except Exception as e:
            api.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")
        return bucket






if __name__ == "__main__":
    app.run()



