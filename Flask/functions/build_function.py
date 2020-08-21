import utils.pymongoconnection
from bson import ObjectId
from flask import Flask, jsonify

def product_details(product_id):

    connection = utils.pymongoconnection.config(section='pymongo')
    product_collections = connection['ProductDetails']['Products']
    selin_collections = connection['ProductDetails']['Selindetails']
    diaper_collections = connection['ProductDetails']['diaperdetails']
    products =[i for i in product_collections.find({"_id": ObjectId(product_id)})]

    selin = selin_collections.find()
    diaper = diaper_collections.find()
    product_details =[]
    for product in products:
        item = product['item']
        if selin_collections.count_documents({'product': item})> 0:
            for selin_data in selin:
                product_details.append(str(selin_data))
            #product_details_list = jsonify({"productsdetails": product_details})
        elif diaper_collections.count_documents({'product': item}) > 0:
            for diaper_data in diaper:
                product_details.append(str(diaper_data))
            #product_details_list = jsonify({"productsdetails": product_details})

    return product_details


# print(product_details('5f2fca6134d89bd90ccc0c18'))
# id = '5f2fca1c34d89bd90ccc0c17'
# connection = utils.pymongoconnection.config(section='pymongo')
# product_collections = connection['ProductDetails']['Products']
# products = product_collections.find({"_id":ObjectId(id)})
# for data in products:
#     print(data)
