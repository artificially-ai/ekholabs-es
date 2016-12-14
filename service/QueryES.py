from service.ElasticsearchConnection import Resource

es = Resource().connect()

# res = es.get(index="twig", doc_type='friends', id=1)
# print(res['_source'])

# res = es.search(index="twig", body={"query": {"match_all": {}}, "filter": {"people": {"Name": "People"}}})
res = es.search(index="twig", body={"query": {"match": {"ContentId": "friends"}}})

# res = es.search(index="twig",
#                 body={"query": {"filtered": {"filter": {"terms": {"Name": ["People", "Person"]}}}}})

print("Got %d Hit[s]:" % res['hits']['total'])

for hit in res['hits']['hits']:
    print(hit["_source"])
