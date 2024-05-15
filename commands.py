import subprocess
import requests

class cli_commands():

	def shutdown():
		print("Shutting down...")
		subprocess.run(['shutdown'])


	def reboot():
		print("Rebooting...")
		subprocess.run(['reboot'])


	def ping():
		print("Pinging Google...")
		subprocess.run(['ping','-c 1','www.google.com'])


	def update():
		print("Updating...")
		subprocess.run(['sudo', 'apt-get', 'update'])


	def execute_command(keyword):
		if keyword == 'ping':
			cli_commands.ping()
		elif keyword == 'reboot':
			cli_commands.reboot()
		elif keyword == 'shutdown':
			cli_commands.shutdown()
		elif keyword == 'update':
			cli_commands.update()
		else:
			print('Unknown command. Please Try Again')


class weather_commands():
	city = ""
	url = "https://weatherapi-com.p.rapidapi.com/current.json"
	querystring = {"q":city}
	headers = {
		"X-RapidAPI-Key": #API Key here,
		"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
		}
	response = requests.request("GET", url, headers=headers, params=querystring)

	def __init__(self,city,querystring):
		self.city = city
		self.querystring = {"q":city}

	def execute_command(self, keyword):
		if keyword == 'temperature':
			response = requests.request("GET", self.url, headers=self.headers, params=self.querystring)
			temp = (float(response.text.split("temp")[1].replace(",\"","").replace("_c\":",""))*(9/5))+32
			print("It is currently {} degrees outside (Farenheit)".format(temp))
		elif keyword == 'condition':
			response = requests.request("GET", self.url, headers=self.headers, params=self.querystring)
			condition = response.text.split("text")[1].split(",")[0].replace("_c\":","").replace("\":","")
			print("It is currently {} in {}".format(condition,self.city))
		else:
			print("Unknown command. Please Try Again")
