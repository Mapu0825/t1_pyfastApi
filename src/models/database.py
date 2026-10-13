from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

# Agregar la URI de conexión a tu base de datos
MONGO_URI = "mongodb+srv://mayorivera08_db_user:W49tyjtcbQsJtO49@cluster0.k8ctrhf.mongodb.net/?appName=Cluster0:"

# Crear una instancia del cliente de MongoDB y asignar un tiempo de espera para la seleccion del servidor
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
# Crear la base de datos y la coleccion 
db = client.dataap
collection = db.trainee

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
