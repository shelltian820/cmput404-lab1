#!/user/bin/env python
import requests

print(requests.__version__)
r = requests.get("https://raw.githubusercontent.com/shelltian820/cmput404-lab1/master/main.py")
# print(dir(r))
print(r.text)
# print(r.status_code)
