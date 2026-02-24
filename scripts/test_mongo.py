from pymongo import MongoClient

uri = "mongodb+srv://taufieqqqhr_db_user:ulOLc0lldJ8GQArf@cluster0.prnycqo.mongodb.net/?appName=Cluster0"

try:
    client = MongoClient(uri)
    print("Koneksi berhasil!")
    print(client.list_database_names())
except Exception as e:
    print("Koneksi gagal:", e)