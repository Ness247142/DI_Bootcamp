
# Write a class called Text, it accepts a string as argument and store the text in a attribute.
# Implement the following:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or meaningful message
# a method that returns the most common word in the text
# a method that returns a list of the unique words in the text
# a classmethod that returns a instance of Text but with a text file: >>> Text.from_file('my_text.txt')
# Write a TextModification class that inherits from Text
# Implement the following:
# a method that returns the text without punctuation
# a method that returns the text without english stop-words (check out what this is !!)
# a method that returns the text without special characters
# Now, use the provided txt file and try using the class you created above.


from collections import Counter 

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 

import re

class Text:
	def __init__(self, input_text):
        self.text = input_text

	def frequency(self, input_text):
		input_text = str.split()          
		str2 = []
		for i in input_text:              
			if i not in str2: 
				str2.append(i)  
		for i in range(0, len(str2)): 
			print('Frequency of', str2[i], 'is :', input_text.count(str2[i]))     


    def most_common_word(self, input_text):
    	frequency = {}
    	file = open("the_stranger.txt", "r")
    	for line in file.readlines():
    		for word in line.strip().split():
    			if word not in frequency:
    				frequency[word] = 0
    				frequency[word] += 1
    			"the_stranger.txt".close()
    			return frequency


    def unique_word(self, input_text):
    	input_file = open("the_stranger.txt", 'r')
    	file_contents = "the_stranger.txt".read()
    	word_list = file_contents.split()
    	file = open("the_stranger.txt", 'w')
    	unique_words = set(word_list)
    	for word in unique_words:
    		file.write(str(word) + "\n")
    	"the_stranger.txt".close()

	@classmethod
    def return_text(cls, input_text):
        return cls(input_text)

if __name__ == '__main__':
    obj = Text()
    newobj = obj.func() 


class TextModification(Text):
	def __init__(self, input_text):
		self.text = input_text

	def text_no_punctuation(self, input_text):
		punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
		for x in input_text.lower(): 
			if x in punctuations: 
				input_text = input_text.replace(x, "") 
			print(input_text) 


	def stop_words(self, input_text):
		stop_words = set(stopwords.words('english'))  
		word_tokens = word_tokenize(input_text)  
		filtered_sentence = [w for w in word_tokens if not w in stop_words]  
		filtered_sentence = []  
		for w in word_tokens:  
			if w not in stop_words:  
				filtered_sentence.append(w)  
			print(word_tokens) 
			print(filtered_sentence)


	import re
	def no_special_characters(self, input_text):
		nstr = re.sub(r'[?|$|.|!]',r'',input_text)
		print nstr
		nestr = re.sub(r'[^a-zA-Z0-9 ]',r'',input_text)
		print nestr

 
with open("the_stranger.txt", "r") as f:
		data = f.readlines()
		return data

print(frequency)
print(most_common_word)
print(unique_word)
print(text)
print(return_text)
print(text_no_punctuation)
print(stop_words)
print(no_special_characters)

