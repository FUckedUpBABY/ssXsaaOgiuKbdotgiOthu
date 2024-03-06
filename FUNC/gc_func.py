def gcgenfunc(len=4):
    try:
        import string
        import random
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        return ''.join(random.choice(chars) for _ in range(len))
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")


def insert_pm(gc):
    try:
        import pymongo
        from mongodb import client, gcdb
        info = {"gc": f"{gc}", "status": "ACTIVE", "type": "PREMIUM"}
        insert = gcdb.insert_one(info)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")


def getgc(gc):
    try:
        import pymongo
        from mongodb import client, gcdb
        find = gcdb.find_one({"gc": f"{gc}"}, {"_id": 0})
        return find
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")


def getallgc():
    try:
        import pymongo
        from mongodb import client, gcdb
        find = gcdb.find({}, {"_id": 0})
        return find
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")


def updategc(gc):
    try:
        import pymongo
        from mongodb import client, gcdb
        prev = {"gc": f"{gc}"}
        nextt = {"$set": {"status": "USED"}}
        update = gcdb.update_one(prev, nextt)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")



def onlycredits(user_id):
    try:
        import pymongo
        from mongodb import client, usersdb
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {f"status": f"PREMIUM"}}
        update = usersdb.update_one(prev, nextt)
        getuser = usersdb.find_one({"id": f"{user_id}"}, {"_id": 0})
        credit = int(getuser["credit"])
        getkey = int(getuser["totalkey"])
        setcredit = credit + 100
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {"credit": f"{setcredit}"}}
        update = usersdb.update_one(prev, nextt)
        setkey = getkey + 1
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {"totalkey": f"{setkey}"}}
        update = usersdb.update_one(prev, nextt)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
