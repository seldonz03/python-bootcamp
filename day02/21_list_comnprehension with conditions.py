requests = {"Andrew": 10, "Peddy": 21, "Alex": 30}
banned = {"Alex"}
adults = [name for name, age in requests.items() if age >= 18]
print(adults)
allowed = [name for name in adults if name not in banned]
print(allowed)

requests = {"Josh": 12,"Peddy": 16, "Alex": 30,"Jeff": 21, "Josel": 18 }
banned={"Jeff"}
adults={name for name,age in requests.items() if age>=1}
print(adults)
allowed = [name for name in adults if name not in banned]
print(allowed)
