
from translate import Translator

translator = Translator(to_lang="ja")

try:
	with open('blah.txt', 'r') as my_file:
		text = my_file.read()
		translation = translator.translate(text)
		with open('blah.txt', 'w') as my_file2:
			my_file2.write(translation)
except FileNotFoundError as e:
		print('Check your file path!')










