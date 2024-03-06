import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://wksixhtcr:wPRRSQpzu2UQ0q4O@cluster0.gozjdwl.mongodb.net"
)
result = str(client)

if "connect=True" in result:
    print("MONGODB CONNECTED SUCCESSFULLY ✅")
else:
    print("MONGODB CONNECTION FAILED ❌")

folder = client["CTH_DATABASE"]
usersdb = folder.USERSDB
chats_auth = folder.CHATS_AUTH
gcdb = folder.GCDB
