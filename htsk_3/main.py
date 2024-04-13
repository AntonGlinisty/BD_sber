import couchdb

couch = couchdb.Server('http://admin:password@localhost:5984/')
database = couch.create('database')

document = {'name' : 'Глинистый'}
database.save(document)