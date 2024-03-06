from func.adyen import *
ccs = open("cc.txt",encoding="UTF-8").read().splitlines()

print("STARTING ADYEN CHECKER...")
for cc in ccs:
    result = charge(cc)
    if "CVV" in result:
        resp = f"{cc} - CARD ATTACHED SUCCESSFULLY ✅"
    elif "CVC Declined" in result:
        resp = f"{cc} - CVC DECLINED ✅"

    elif "Not enough balance" in result:
        resp = f"{cc} - LOW FUNDS ✅"

    elif "AVS Declined" in result:
        resp = f"{cc} - AVS DECLINED ✅"

    else:
        resp = f"{cc} - {result}"
    print(resp)