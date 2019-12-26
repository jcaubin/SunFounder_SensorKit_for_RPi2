#pruebas de concepto con mongodb

import pymongo as pm

uri = ""
myclient = pm.MongoClient(uri)

mydb=myclient["demoDb"]

mycol = mydb["demoCollection"]

mydata ={"nombre":"Juan","demoKey":"peñalara"}

x=mycol.insert_one(mydata)

print(x)
