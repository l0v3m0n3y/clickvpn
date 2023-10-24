import requests
class Client():
	def __init__(self):
		self.api="https://1clickvpn.net/api/v1"
		self.api_2="https://api.1clickvpn.net/api/v1"
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
	def my_ip(self):
		return requests.get(f"{self.api_2}/checks/ip/",headers=self.headers).json()
	def login(self,email,password):
		data={"email":email,"password":password}
		return requests.post(f"{self.api}/auth/signin",json=data,headers=self.headers).json()
	def register(self,email,password):
		data={"email":email,"password":password,"passwordConfirmation":password}
		return  requests.post(f"{self.api}/auth/signup",json=data,headers=self.headers).json()
	def get_proxies(self):
		return requests.get(f"{self.api}/servers/",headers=self.headers).json()
	def reset_password(self,email):
		data={"email":email}
		return requests.post(f"{self.api}/reset-password-requests",json=data,headers=self.headers).json()