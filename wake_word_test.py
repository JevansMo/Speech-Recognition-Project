import pvporcupine
import struct
import time
import pyaudio
from sr import command
from sr import run_commands

def main():
	porcupine = None
	pa = None
	audio_stream = None


	try:
		porcupine = pvporcupine.create(
			access_key = 'xVBfiZ37cJufNWC+6Zlzvij/wOaIttDdNj8SqpFXu14ZHaah8Eg1kw==',
			keywords = ['blueberry', 'grapefruit']
		)
		pa = pyaudio.PyAudio()
		audio_stream = pa.open(
			rate = porcupine.sample_rate ,
			channels = 1 ,
			format = pyaudio.paInt16 ,
			input = True ,
			frames_per_buffer = porcupine.frame_length)


		while True:
			pcm = audio_stream.read(porcupine.frame_length)
			pcm = struct.unpack_from('h' * porcupine.frame_length, pcm)

			keyword_index = porcupine.process(pcm)
			if keyword_index == 0:
				print('Wake word detected. Listening for command.. ')
				user_input = command()
				print(user_input)
				run_commands(user_input)
				print('On standby ')
			elif keyword_index == 1:
				print('Ending...')
				exit()

	finally:
		if porcupine is not None:
			porcupine.delete()

		if audio_stream is not None:
			audio_stream.close()

		if pa is not None:
			pa.terminate()

if __name__ == '__main__':
	main()
