from mongoengine import connect

def connection():
    username = "skuzalexandr"
    password = "1NbBEO7mLNyzFRnp"
    host = "cluster0.kcbs7ww.mongodb.net"
    db_name = "Web-HW-8-2"
    URI = f"mongodb+srv://{username}:{password}@{host}/{db_name}"
    connect(host=URI)
