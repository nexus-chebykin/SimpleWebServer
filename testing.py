import requests
fixed_IP = 'localhost'
port = 777
t = requests.post('http://{}:{}/'.format(fixed_IP, str(port)), json = {'summands': [1000000000000, 20000000000000]})
print(t.headers)