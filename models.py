from mongoengine import Document, StringField, BooleanField
from connect_with_mongodb import connection

# Підключення до MongoDB
connection()

class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    email_sent = BooleanField(default=False)

    meta = {
        'collection': 'contacts'
    }
