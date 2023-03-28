import subprocess
import requests
from commands import cli_commands
from commands import weather_commands

def main():
	execute = command()
	print(execute)
	run_commands(execute)

def command():
	subprocess.run(['arecord','-d','3','-r','48000','command.wav'])
	api_url = 'https://speech-recognition-english.p.rapidapi.com/api/asr'
	api_key = '9b3e089dfdmsh441fc6b319431ddp14ec82jsn1f9a66bcec21'

	sound_path = 'voice_recog_project'
	sound_name = 'command.wav'

	files = {'sound': (sound_name, open(sound_name, 'rb'), 'multipart/form-data')}
	header = {
		"X-RapidAPI-Key": "9b3e089dfdmsh441fc6b319431ddp14ec82jsn1f9a66bcec21",
		"X-RapidAPI-Host": "speech-recognition-english1.p.rapidapi.com"
		}
	response = requests.post(api_url, files=files, headers=header)
	words_said = response.text.split("text")[1].split(" \",")[0].replace("\":\"","")
	print(words_said)
	return words_said

def run_commands(words_said):
	words_said = words_said.split(" ")
	command_type = words_said[0]
        # TODO: Maps do not work the way I thought, find another way to correlate words with commands

	if command_type == 'COMMAND':
		print(words_said[1])
		cli_command = words_said[1].lower()
		if cli_command == 'pig':
			print("I think you meant: \"ping\"")
			cli_command = 'ping'
		cli_commands.execute_command(cli_command)



	if command_type == 'WHETHER':
		placeholder_dict = {"void","void"}
		city = words_said[1].lower()
		weather_for_city = weather_commands(city,placeholder_dict)
		weather_command = words_said[2].lower()
		print("Giving you the: " +  weather_command + " in " + weather_commands.city)
		weather_for_city.execute_command(weather_command)

if __name__ == '__main__':
        main()

