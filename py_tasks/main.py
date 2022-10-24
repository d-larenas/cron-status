import datetime
import requests
print("hello", datetime.datetime.now())
r = requests.get('https://diego-larenas.gropoz.com')
print("page status: ", r.status_code)
