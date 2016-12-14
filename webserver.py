from service.ElasticsearchService import ElasticsearchIndex
import json
import web

urls = (
    '/create/(.*)', 'Index',
    '/delete/(.*)', 'Index',

    '/query/(.*)', 'Content',
    '/remove/(.*)/(.*)/(.*)', 'Content',
    '/index/(.*)/(.*)', 'Content',
)

class Index:

    def POST(self, index_name):
        web.header('Content-Type', 'application/json')

        settings = web.data()
        index = ElasticsearchIndex.create(index_name, settings)
        return json.dumps(index)

    def DELETE(self, index_name):
        web.header('Content-Type', 'application/json')

        index = ElasticsearchIndex.delete_index(index_name)
        return json.dumps(index)


class Content:

    def POST(self, index_name):
        web.header('Content-Type', 'application/json')

        criteria = web.data()
        index = ElasticsearchIndex.query(index_name, criteria)
        return json.dumps(index)

    def PUT(self, index_name, document_type):
        web.header('Content-Type', 'application/json')

        payload = web.data()
        index = ElasticsearchIndex.index(index_name, document_type, payload)
        return json.dumps(index)

    def DELETE(self, index_name, document_type,  document_id):
        web.header('Content-Type', 'application/json')

        index = ElasticsearchIndex.delete_document(index_name, document_type, document_id)
        return json.dumps(index)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()