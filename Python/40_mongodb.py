#pruebas de concepto con mongodb

import pymongo as pm

uri = "mongodb://2b41d18f-0ee0-4-231-b9ee:mNlRbGPqQMAbtmEhzL7F8JR0cv52nnYTZRW5qWVpV8VCxW6YFuwHNUPkI9BwFX8Bh9Opx9qFVxePZLJ39qjscQ==@2b41d18f-0ee0-4-231-b9ee.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
myclient = pm.MongoClient(uri)

mydb=myclient["demoDb"]

mycol = mydb["demoCollection"]

mydata ={"nombre":"Juan","demoKey":"peñalara"}

x=mycol.insert_one(mydata)

print(x)