import json

# data = '{"var1": "Hiral", "var2": "56"}'
# print(data)  # output: {"var1": "Hiral", "var2": "56"}

# parsing json
# parsed = json.loads(data)
# print(parsed)  # output: {'var1': 'Hiral', 'var2': '56'}
# print(parsed['var1'])  # output: Hiral


# To be check
# par = json.load()


data2 = {
    "channel": "Hiral87",
    "cars": ["bmw", "audi", "ferrari"],
    "fridge": ("milk", "veges"),
    "isBd": False
}

js = json.dumps(data2)
print(js)  # output: {"channel": "Hiral87", "cars": ["bmw", "audi", "ferrari"], "fridge": ["milk", "veges"], "isBd": false}


