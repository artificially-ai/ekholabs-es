import pkg_resources
from requests_aws4auth import AWS4Auth
from elasticsearch import Elasticsearch, RequestsHttpConnection

import json


class Resource:
    __instance = None
    __elasticsearch = None

    def __new__(cls, val):
        if Resource.__instance is None:
            Resource.__instance = object.__new__(cls)
            Resource.__instance.val = val

        return Resource.__instance

    def connect(self):

        if self.__elasticsearch is not None:
            return self.__elasticsearch

        config_package = 'config'
        file_path = 'properties.json'
        properties = pkg_resources.resource_string(config_package, file_path)

        configuration = json.loads(properties)

        awsauth = AWS4Auth(configuration['access_key'], configuration['secret_key'], configuration['region'], 'es')
        self.__elasticsearch = Elasticsearch(
            hosts=[{'host': configuration['host'], 'port': 443}],
            http_auth=awsauth,
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection
        )

        return self.__elasticsearch
