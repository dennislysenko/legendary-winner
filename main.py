import json
import random
from io import StringIO
import numpy
import string
import nlp
import sys

# ==============================================================================
# ================================== MODULES ===================================
# ==============================================================================

def cleanup_word(word):
	return word.lower().translate({key: None for key in string.punctuation})

class EmojiMap:
	keyword_emoji_map = dict()
	model = None

	def __init__(self):
		self.model = nlp.load_model()
		self.construct_emoji_map()

	def construct_emoji_map(self):
		emojis_data = open('emojis.json', 'r', encoding='UTF-8').read()
		emojis = json.loads(emojis_data)

		# schema:
		# "emojikey": { "keywords": [...], "char": <emoji>, "category": "people" }

		for (name, entry) in emojis.items():
			emoji = entry['char']
			keywords = entry['keywords']
			for keyword in keywords:
				if keyword not in self.keyword_emoji_map:
					self.keyword_emoji_map[keyword] = []

				if emoji not in self.keyword_emoji_map[keyword] and emoji is not None:
					self.keyword_emoji_map[keyword].append(emoji)

	def get_emoji(self, cleaned_word):
		emoji = None

		try:
			emoji = nlp.get_closest_emoji(self.model, cleaned_word)
		except:
			emoji = None

		if emoji == None and cleaned_word in self.keyword_emoji_map and len(self.keyword_emoji_map[cleaned_word]) > 0:
			emojis = self.keyword_emoji_map[cleaned_word]
			
			randIndex = random.sample(range(len(emojis)), 1)
			randIndex.sort()

			emoji = emojis[randIndex[0]]

			return emoji

# ==============================================================================
# ================================== DRIVER ===================================
# ==============================================================================

def emojipastafy(copypasta):
	emoji_map = EmojiMap()

	f = StringIO()

	for word in copypasta.split():
		cleaned_word = cleanup_word(word)

		f.write(word)

		emoji = emoji_map.get_emoji(cleaned_word)

		if emoji is not None:
			count = numpy.random.poisson(1)
			if count > 0:
				f.write(' ')
				for i in range(count):
					f.write(emoji)
				f.write(' ')

		f.write(' ')

	emojipasta = f.getvalue()

	f.close()

	return emojipasta

if __name__ == '__main__':
	# process copypasta
	copypasta = open('input.txt', 'r', encoding='UTF-8').read()
	emojipasta = emojipastafy(copypasta)
	sys.stdout.buffer.write(emojipasta.encode('UTF-8'))
