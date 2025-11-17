def test():
    data = {
        "query": {'animes(search: "bakemono", limit: 1, kind: "!special")': {"id": ""}}
    }

    print(
        str(data)
    )  #  {'query': {'animes(search: "bakemono", limit: 1, kind: "!special")': {'id': ''}}}


(
    '{"query":"{\n  # look for more query params in the documentation\n  people(limit: 1) {\n    id\n    malId\n    name\n    russian\n    japanese\n    synonyms\n    url\n    isSeyu\n    isMangaka\n    isProducer\n    website\n    createdAt\n    updatedAt\n    birthOn {\n      year\n      month\n      day\n      date\n    }\n    deceasedOn {\n      year\n      month\n      day\n      date\n    }\n\n    poster {\n      id\n      originalUrl\n      mainUrl\n    }\n  }\n}\n"}'
    - -compressed
)

test()
