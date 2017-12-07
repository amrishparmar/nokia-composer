import re
import math
import winsound
import time


def extract_components(note):
	match = re.search(r"([0-9]{1,2}\.?)(-|#?[a-g])([0-9])?", note)
	return match.groups()


def calculate_time(note_length, tempo):
	if (note_length[-1] == '.'):
		nl = int(note_length[:-1])
		nl *= 1.5
	else:
		nl = int(note_length)

	return ((60000 / tempo) / 4) / nl


def calculate_freq(pitch, octave):
	if pitch == '-':
		return 0

	freqencies = {
		'c': 16.35,
		'#c': 17.32,
		'd': 18.35,
		'#d': 19.45,
		'e': 20.6,
		'f': 21.83,
		'#f': 23.12,
		'g': 24.5,
		'#g': 25.96,
		'a': 27.5,
		'#a': 29.14,
		'b': 30.87,
		'-': 0,
	}

	return freqencies[pitch] * math.pow(4, int(octave))



def main():
	song = "32f2 32#d2 32f2 8#d2 32#d2 32#d2 32f2 32g2 32f2 16.#d2 32- 16f2 8#d2 16#g2 32#g2 32#g2 32#g2 16g2 16.#d2 32- 8#a2 32#a2 32#a2 16#a2 16f2 16g2 8#g2 16g2 16g2 32g2 16g2 16d2 16#d2 8f2 16f2 8#d2 16#g2 32#g2 32#g2 32#g2 32g2 32#d2 32f2 16#d2"
	tempo = 40

	song_note_components = [extract_components(note) for note in song.split()]

	tune = [(calculate_time(component[0], tempo), calculate_freq(component[1], component[2])) for component in song_note_components]

	print(tune)

	for note in tune:
		if note[1] == 0:
			time.sleep(note[0]/1000)
		else:
			winsound.Beep(int(note[1]), int(note[0]) * 20)


if __name__ == '__main__':
	main()