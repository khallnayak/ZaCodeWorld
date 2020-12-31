import requests
print(requests.post('http://0.0.0.0:6969/login',json={'name':'khallnayak','rollno':'123456'}).content)
