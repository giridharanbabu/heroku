from configparser import ConfigParser

from pymongo import MongoClient
from dynaconf import settings


def config(filename='C:/Users/gdnau/PycharmProjects/user_auth/config/settings.toml', section='pymongo'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # print(parser)
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        client = MongoClient()
        connection = MongoClient(settings.from_env('pymongo').IPADDRESS, 27017)
    #     params = parser.items(section)
    #     #print(params)
    #     for param in params:
    #         for para in param:
    #             print(para)
            #con = psycopg2.connect(database="postgres", user="postgres", password="", host="127.0.0.1", port="5432")

    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return connection

# print(config())