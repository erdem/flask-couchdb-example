from flaskext.couchdb import Document, TextField, IntegerField


class Products(Document):
    doc_type = 'product'

    name = TextField()
    category = TextField()
    quantity = IntegerField()


