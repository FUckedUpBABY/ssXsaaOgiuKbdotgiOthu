def getuserinfo(user_id):
    try:
        import pymongo
        from mongodb import client, usersdb
        find = usersdb.find_one({"id": f"{user_id}"}, {"_id": 0})
        return find
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")


def randgen(len=6):
    import string
    import random
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choice(chars) for _ in range(len))


def getallusers():
    try:
        import pymongo
        from mongodb import client, usersdb
        find = usersdb.find({}, {"_id": 0})
        return find
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")


def updateuserinfo(user_id, module, value):
    try:
        import pymongo
        from mongodb import client, usersdb
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {f"{module}": f"{value}"}}
        update = usersdb.update_one(prev, nextt)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")


def premiumuser(user_id):
    try:
        import pymongo
        from mongodb import client, usersdb
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {f"status": f"PREMIUM"}}
        update = usersdb.update_one(prev, nextt)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")

def pmlife(user_id,amt):
    try:
        import pymongo
        from mongodb import client, usersdb
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {f"status": f"𝐏𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭"}}
        update = usersdb.update_one(prev, nextt)
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {f"credit": f"{amt}"}}
        update = usersdb.update_one(prev, nextt)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")

def freeuser(user_id):
    try:
        import pymongo
        from mongodb import client, usersdb
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {f"status": f"FREE"}}
        update = usersdb.update_one(prev, nextt)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")


def directcredit(user_id, amt):
    try:
        import pymongo
        from mongodb import client, usersdb
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {f"credit": f"{amt}"}}
        update = usersdb.update_one(prev, nextt)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")


def addchat(chat_id):
    try:
        import pymongo
        from mongodb import client, chats_auth
        add = {"id": f"{chat_id}", "status": "approved"}
        insert = chats_auth.insert_one(add)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")


def getchatinfo(chat_id):
    try:
        import pymongo
        from mongodb import client, chats_auth
        find = chats_auth.find_one({"id": f"{chat_id}"}, {"_id": 0})
        return find
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")


def getallchat():
    try:
        import pymongo
        from mongodb import client, chats_auth
        find = chats_auth.find({}, {"_id": 0})
        return find
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")


def setantispamtime(user_id):
    try:
        import time
        import pymongo
        from mongodb import client, usersdb
        settime = int(time.time())
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {"antispam_time": f"{settime}"}}
        update = usersdb.update_one(prev, nextt)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")


def deductcredit(user_id):
    try:
        import pymongo
        from mongodb import client, usersdb
        getuser = usersdb.find_one({"id": f"{user_id}"}, {"_id": 0})
        plan = getuser["plan"]
        if "∞" in plan:
            pass
        else:
            credit = int(getuser["credit"])
            setcredit = credit - 1
            prev = {"id": f"{user_id}"}
            nextt = {"$set": {"credit": f"{setcredit}"}}
            update = usersdb.update_one(prev, nextt)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")


def massdeductcredit(user_id, amt):
    try:
        import pymongo
        from mongodb import client, usersdb
        getuser = usersdb.find_one({"id": f"{user_id}"}, {"_id": 0})
        plan = getuser["plan"]
        if "∞" in plan:
            pass
        else:
            credit = int(getuser["credit"])
            setcredit = credit - amt
            prev = {"id": f"{user_id}"}
            nextt = {"$set": {"credit": f"{setcredit}"}}
            update = usersdb.update_one(prev, nextt)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")


def refundcredit(user_id):
    try:
        import pymongo
        from mongodb import client, usersdb
        getuser = usersdb.find_one({"id": f"{user_id}"}, {"_id": 0})
        plan = getuser["plan"]
        if "∞" in plan:
            pass
        else:
            credit = int(getuser["credit"])
            setcredit = credit + 1
            prev = {"id": f"{user_id}"}
            nextt = {"$set": {"credit": f"{setcredit}"}}
            update = usersdb.update_one(prev, nextt)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")


def getpm(user_id,time_of_pm):
    try:
        import pymongo
        from datetime import date
        from datetime import timedelta
        from mongodb import client, usersdb
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {f"status": f"PREMIUM"}}
        update = usersdb.update_one(prev, nextt)
        getvalidity = str(date.today() + timedelta(days=time_of_pm)).split("-")
        yy = getvalidity[0]
        mm = getvalidity[1]
        dd = getvalidity[2]
        validity = f"{dd}-{mm}-{yy}"
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {"expiry": f"{validity}"}}
        update = usersdb.update_one(prev, nextt)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")


def getplan2(user_id):
    try:
        import pymongo
        from datetime import date
        from datetime import timedelta
        from mongodb import client, usersdb
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {f"status": f"PREMIUM"}}
        update = usersdb.update_one(prev, nextt)
        plan_value = "Silver Plan 1.99$ ∞"
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {"plan": f"{plan_value}"}}
        update = usersdb.update_one(prev, nextt)
        getvalidity = str(date.today() + timedelta(days=15)).split("-")
        yy = getvalidity[0]
        mm = getvalidity[1]
        dd = getvalidity[2]
        validity = f"{dd}-{mm}-{yy}"
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {"expiry": f"{validity}"}}
        update = usersdb.update_one(prev, nextt)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")


def getplan3(user_id):
    try:
        import pymongo
        from datetime import date
        from datetime import timedelta
        from mongodb import client, usersdb
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {f"status": f"PREMIUM"}}
        update = usersdb.update_one(prev, nextt)
        plan_value = "Gold Plan 4.99$ ∞"
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {"plan": f"{plan_value}"}}
        update = usersdb.update_one(prev, nextt)
        getvalidity = str(date.today() + timedelta(days=30)).split("-")
        yy = getvalidity[0]
        mm = getvalidity[1]
        dd = getvalidity[2]
        validity = f"{dd}-{mm}-{yy}"
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {"expiry": f"{validity}"}}
        update = usersdb.update_one(prev, nextt)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")


def plan_expirychk(user_id):
    try:
        import pymongo
        from mongodb import client, usersdb
        from datetime import date
        from datetime import timedelta
        today = str(date.today())
        getuser = usersdb.find_one({"id": f"{user_id}"}, {"_id": 0})
        getexpiry = getuser["expiry"].split("-")
        dd = getexpiry[0]
        mm = getexpiry[1]
        yy = getexpiry[2]
        expiry = f"{yy}-{mm}-{dd}"
        if expiry != 'N/A' and expiry < today:
            prev = {"id": f"{user_id}"}
            nextt = {"$set": {f"status": f"FREE"}}
            update = usersdb.update_one(prev, nextt)
            prev = {"id": f"{user_id}"}
            nextt = {"$set": {"expiry": "N/A"}}
            update = usersdb.update_one(prev, nextt)
            return "YES"

    except Exception as e:
        pass
