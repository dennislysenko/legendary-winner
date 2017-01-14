import json
import random

# ==============================================================================
# ================================== MODULES ===================================
# ==============================================================================

def cleanup_word(word):
	# TODO write
	return word

class EmojiMap:
	keyword_emoji_map = dict()

	def __init__(self):
		self.construct_emoji_map()

	def construct_emoji_map(self):
		emojis_data = open('emojis.json').read()
		emojis = json.loads(emojis_data)

		# schema:
		# "emojikey": { "keywords": [...], "char": <emoji>, "category": "people" }

		for (name, entry) in emojis.iteritems():
			emoji = entry['char']
			keywords = entry['keywords']
			for keyword in keywords:
				if keyword not in self.keyword_emoji_map:
					self.keyword_emoji_map[keyword] = []

				if emoji not in self.keyword_emoji_map[keyword] and emoji is not None:
					self.keyword_emoji_map[keyword].append(emoji)

	def get_emoji(self, cleaned_word):
		if cleaned_word in self.keyword_emoji_map and len(self.keyword_emoji_map[cleaned_word]) > 0:
			emojis = self.keyword_emoji_map[cleaned_word]
			
			randIndex = random.sample(range(len(emojis)), 1)
			randIndex.sort()

			emoji = emojis[randIndex[0]]

			return emoji

# TODO maybe implement emoji frequency module?

# ==============================================================================
# ================================== DRIVER ===================================
# ==============================================================================

emoji_map = EmojiMap()

# process copypasta
copypasta = open('input.txt').read()
f = open('output.txt', 'w')

for word in copypasta.split():
	cleaned_word = cleanup_word(word)

	f.write(word.encode('UTF-8'))

	emoji = emoji_map.get_emoji(cleaned_word)

	if emoji is not None:
		f.write(' ' + emoji.encode('UTF-8') + ' ')

	f.write(' ')

f.close()
