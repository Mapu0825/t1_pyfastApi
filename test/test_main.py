from pymongo import MongoClient
from pymongo .errors import ConnectionFailure, ServerSelectionTimeoutError

# Agregar la URI de conexion a tubase de datos mongoDB
MONGO_URI = "mongodb+srv://mayorivera08_db_user:W49tyjtcbQsJtO49@cluster0.k8ctrhf.mongodb.net/?appName=Cluster0:"

# Crear una instancia del cliente de MongoDB y asignar un tiempo de espera para la seleccion del servidor.
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
#crear la base de datos y la coleccion 
db = client.ambiente703
collection = db.mesa

#crear el modelo de datos para la coleccion
nueva_mesa = {
    "name": "Maria Paula",
    "status": "Alive",
    "species": "Human",
    "gender": "Male"
}
#insertar el modelo de datos en la coleccion
collection.insert_one(nueva_mesa)
print("Documento insertado en la coleccion 'mesa' de la base de datos 'ambiente703'")

try:
    # Intentar obtener información del servidor para verificar la conexión.
    client.server_info()
    client.admin.command('ping')
    print("Conexión exitosa a MongoDB")
except (ConnectionFailure, ServerSelectionTimeoutError) as e:
    print(f"Error de conexión a MongoDB: {e}")
finally:
    # Cerrar la conexión al cliente de MongoDB.
    client.close()
