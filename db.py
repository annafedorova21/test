from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']

accrual = db['accrual']
payment = db['payment']

payments = payment.find().sort("date", 1)

matched = []
unmatched = []

for p in payments:
    a = accrual.find({"date": {"$lte": p["date"]}}).sort([("month", -1), ("date", 1)])
    if a.count() > 0:
        m = a[0]
        matched.append({"payment_id": p["id"], "accrual_id": m["id"]})
    else:
        unmatched.append(p["id"])

print("Matched payments and accruals:", matched)
print("Unmatched payments:", unmatched)

table = PrettyTable()
table.field_names = ["Payment ID", "Accrual ID"]

for m in matched:
    table.add_row([m["payment_id"], m["accrual_id"]])

print(table)
print("Unmatched payments:", unmatched)