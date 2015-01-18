#!/usr/bin/python

from random import randint

# A safe way to access list items. Returns `default` if `item` does not exist in
# `array1 instead of throwing exception.
def get(array, item, default = ''):
	try:
		return array[item]
	except:
		return default

def translate(text):
	text = text.upper()
	text_arr = text.split()

	output = ''
	text_arr_len = len(text_arr)
	word_len = None

	i = 0
	while i < text_arr_len:
		word_len = len(text_arr[i])

		if text_arr[i].find('YOUR') != -1 or text_arr[i].find('YOU\'RE') != -1:
			output += 'UR'
		elif text_arr[i].find('YOU') != -1:
			output += 'U'
		elif (text_arr[i] + ' ' + get(text_arr, i + 1)).find('WHAT THE') != -1:
			output += 'WT'
			if get(text_arr, i + 2).find('FUCK') != -1 and \
				get(text_arr[i + 2], text_arr.index('FUCK') + 4) != 'I':
				output += 'F'
				i += 1
			elif get(text_arr, i + 2).find('HELL') != -1 or \
				get(text_arr, i + 2).find('HECK') != -1:
				output += 'H'
				i += 1
			i += 1
		elif text_arr[i].find('WHAT') != -1:
			output += 'WUT'
		elif text_arr[i] == 'ARE':
			output += 'R'
		elif text_arr[i] == 'WHY':
			output += 'Y'
		elif (text_arr[i] + ' ' + get(text_arr, i + 1) + ' ' + get(text_arr, i + 2)).find('BE RIGHT BACK') != -1:
			output += 'BRB'
			i += 2
		elif text_arr[i].find('BECAUSE') != -1:
			output += 'B/C'
		elif (text_arr[i] + ' ' + get(text_arr, i + 1) + ' ' + get(text_arr, i + 2)).find('OH MY GOD') != -1:
			output += 'OMG'
			i += 2
		elif text_arr[i].find('OH') != -1:
			output += 'O'
		elif text_arr[i] == 'THE':
			if randint(0, 1) == 0:
				output += 'TEH'
			else:
				output += 'DA'
		elif text_arr[i] == 'MY':
			output += 'MAH'
		elif text_arr[i] == 'NEW':
			output += 'NU'
		elif text_arr[i] == 'WITH':
			output += 'WIT'
		elif text_arr[i].find('REALLY') != -1:
			output += 'RILLY'
		elif text_arr[i].find('PLEASE') != -1:
			output += 'PLZ'
		elif text_arr[i].find('THANKS') != -1:
			output += 'THX'
		elif text_arr[i].find('THERE') != -1:
			if randint(0, 1) == 0:
				output += 'THEIR'
			else:
				output += 'THEYRE'
		elif text_arr[i].find('THEIR') != -1:
			if randint(0, 1) == 0:
				output += 'THERE'
			else:
				output += 'THEYRE'
		elif text_arr[i].find('THEY\'RE') != -1:
			if randint(0, 1) == 0:
				output += 'THERE'
			else:
				output += 'THEIR'
		elif text_arr[i].find('OK') != -1:
			output += 'K'
		elif text_arr[i].find('LIBRARY') != -1:
			output += 'LIBERRY'
		else:
			j = 0
			while j < word_len:
				if text_arr[i][j] == get(text_arr[i], j + 1):
					output += text_arr[i][j]
					j += 1
				elif text_arr[i][j] == 'B':
					output += 'B'
					if get(text_arr[i], j + 1) == 'E':
						j += 1
				elif text_arr[i][j] == 'C':
					if get(text_arr[i], j + 1) == 'K':
						output += 'K'
						j += 1
					else:
						output += 'C'
				elif text_arr[i][j] == 'E':
					if randint(0, 2) == 0:
						output += '3'
					elif randint(0, 2) == 1:
						output += 'A'
					else:
						output += 'E'
				elif text_arr[i][j] == 'I':
					if get(text_arr[i], j + 1) + get(text_arr[i], j + 2) == 'NG':
						output += 'NG'
						j += 2
					elif get(text_arr[i], j + 2) == 'E':
						output += 'IE' + text_arr[i][j + 1]
						j += 2
					elif get(text_arr[i], j + 1) == 'E':
						output += 'EI'
						j += 1
					elif get(text_arr[i], j + 1) + get(text_arr[i], j + 2) == '\'M' and \
						j + 3 == word_len:
						if get(text_arr, i + 1) + ' ' + get(text_arr, i + 2) == 'GOING TO':
							output += 'IMA'
							i += 2
							j += 2
						else:
							output += 'IM'
					elif get(text_arr, i + 1) == 'AM':
						if get(text_arr, i + 2) + ' ' + get(text_arr, i + 3) == 'GOING TO':
							output += 'IMA'
							i += 3
						else:
							output += 'IM'
							i += 1
					else:
						output += 'I'
				elif text_arr[i][j] == 'A':
					if get(text_arr[i], j + 1) == 'M':
						output += 'M'
						j += 1
					elif get(text_arr[i], j + 1) + get(text_arr[i], j + 2) == 'LK':
						output += 'OK'
						j += 2
					elif get(text_arr[i], j + 1) == 'I':
						output += 'A' + get(text_arr[i], j + 2) + 'E'
						j += 2
					elif get(text_arr[i], j + 1) + get(text_arr[i], j + 2) + get(text_arr[i], j + 3) == 'TER':
						output += '8R'
						j += 3
					elif get(text_arr[i], j + 2) == 'E':
						output += 'AE' + get(text_arr[i], j + 1)
						j += 2
					else:
						output += 'A'
				elif text_arr[i][j] == 'S':
					if get(text_arr[i], j + 1) + get(text_arr[i], j + 2) + get(text_arr[i], j + 3) \
						+ get(text_arr[i], j + 4) + get(text_arr[i], j + 5) == 'CHOOL':
						output += 'SKOOL'
						j += 5
					elif get(text_arr[i], j + 1) + get(text_arr[i], j + 2) + ' ' + text_arr[i][0] \
						+ get(text_arr[i], 1) + get(text_arr[i], 2) == 'SEE YOU':
						output += "CYA"
						j += 5
					elif get(text_arr[i], j + 1) + get(text_arr[i], j + 2) + ' ' + text_arr[i][0] \
						+ get(text_arr[i], 1) == 'SEE YA':
						output += "CYA"
						j += 5
					else:
						output += 'S'
				elif text_arr[i][j] == 'O':
					if get(text_arr[i], j + 1) == 'O':
						output += 'U'
						j += 1
					elif get(text_arr[i], j + 1) == 'U' and get(text_arr[i], j + 2) == 'L':
						output += 'U'
						j += 2
					else:
						output += 'O'
				elif text_arr[i][j] == 'T':
					if get(text_arr[i], j + 1) == 'O':
						output += '2'
						if get(text_arr[i], j + 2) == 'O':
							j += 2
						else:
							j += 1
					elif get(text_arr[i], j + 1) + get(text_arr[i], j + 2) + get(text_arr[i], j + 3) == 'HAT':
						output += 'TAHT'
						j += 3
					else:
						output += 'T'
				elif text_arr[i][j] not in ['.', '!', '?', '\'', ';', ',', ':', '"', '`', '~']:
					output += text_arr[i][j]

				j += 1

		if text_arr[i].find('.') != -1 or text_arr[i].find('!') != -1 or text_arr[i].find('?') != -1:
			place_in_word = None

			if text_arr[i].find('!') != -1:
				first_char = '!'
			elif text_arr[i].find('.') != -1:
				first_char = '.'
			elif text_arr[i].find('?') != -1:
				first_char = '?'

			if text_arr[i].find('.') < text_arr[i].find(first_char) and text_arr[i].find('.') != -1:
				first_char = '.'

			if text_arr[i].find('?') < text_arr[i].find(first_char) and text_arr[i].find('?') != -1:
				first_char = '?'

			place_in_word = text_arr[i].find(first_char)

			if text_arr[i].find('?') != -1:
				output += '?'

			while get(text_arr[i], place_in_word) == '.' or get(text_arr[i], place_in_word) == '!' or \
				get(text_arr[i], place_in_word) == '?':
				
				if text_arr[i][place_in_word] == '!' or text_arr[i][place_in_word] == '.':
					k = randint(4, 8)
					while k > 0:
						if randint(0, 1) == 0:
							output += '!'
						else:
							output += '1'
						k -= 1
				elif text_arr[i][place_in_word] == '?':
					k = randint(4, 8)
					while k > 0:
						if randint(0, 1) == 0:
							output += '?'
						else:
							output += '!'
						k -= 1

				place_in_word += 1

			if randint(0, 1) == 0:
				output += ' OMG'
			if randint(0, 1) == 0:
				output += ' WTF'
			if randint(0, 1) == 0:
				output += ' LOL'

		if i != text_arr_len - 1 and get(text_arr, i + 1) != '':
			output += ' '

		i += 1
	
	return output