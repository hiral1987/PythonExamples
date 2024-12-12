import requests

# Get requests
r = requests.get('https://financialmodelingprep.com/api/v3/search-ticker?query=AA&limit=10&exchange=NASDAQ')

print(r.text)
print(r.status_code)

# url = 'www.something.com'
# data = {
#     'p1': 'nm',
#     'p2': 'nm2',
# }
# r2 = requests.post(url=url, data=data)


