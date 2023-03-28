import subprocess
import requests
from commands import cli_commands
from commands import weather_commands

def main():
        execute = command()
        run_commands(execute)

def command():
        # creates the file to record your voice
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
        return words_said

def run_commands(words_said):
        words_said = words_said.split(" ")
        command_type = words_said[0]

        if command_type == 'COMMAND':
                print(words_said[1])
                cli_command = words_said[1].lower()
                # speech recognition api rarely recognizes the word 'ping'
                if cli_command == 'pig':
                        print("I think you meant: \"ping\"")
                        cli_command = 'ping'
                cli_commands.execute_command(cli_command)



        if command_type == 'WHETHER' or command_type == 'WEATHER':
                # placeholder for the querystring in commands.py that the weather api uses
                placeholder_dict = {"void","void"}
                city = ""


