from ElasticsearchConnection import Resource
from uuid import uuid4


class ElasticsearchIndex:

    @staticmethod
    def create(index_name, settings):
        es = Resource().connect()

        index = es.indices.create(index=index_name, ignore=400, body=settings)
        return index

    @staticmethod
    def delete_index(index_name):
        es = Resource().connect()

        index = es.indices.delete(index=index_name, ignore=[400, 404])
        return index

    @staticmethod
    def index(index_name, document_type, payload):
        es = Resource().connect()

        index = es.index(index=index_name, doc_type=document_type, id=uuid4(), body=payload)
        return index

    @staticmethod
    def query(index_name, query_criteria):
        es = Resource().connect()
        index = es.search(index=index_name, body=query_criteria)
        return index

    @staticmethod
    def delete_document(index_name, document_type, document_id):
        es = Resource().connect()

        index = es.delete(index=index_name, doc_type=document_type, id=document_id)
        return index
