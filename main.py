import json
import random

emojis_data = open('emojis.json').read()
emojis = json.loads(emojis_data)

# schema:
# "emojikey": { "keywords": [...], "char": <emoji>, "category": "people" }

keyword_emoji_map = dict()
for (name, entry) in emojis.iteritems():
	emoji = entry['char']
	keywords = entry['keywords']
	for keyword in keywords:
		if keyword not in keyword_emoji_map:
			keyword_emoji_map[keyword] = []

		if emoji not in keyword_emoji_map[keyword] and emoji is not None:
			keyword_emoji_map[keyword].append(emoji)

def encode_emoji(emoji):
	return emoji.encode('UTF-8')

# proof of concept, make sure our map is correct
f = open('test.txt', 'w')
for keyword in keyword_emoji_map.keys()[0:5]:
	for emoji in keyword_emoji_map[keyword]:
		f.write(emoji.encode('UTF-8'))
f.close()

# process copypasta
copypasta = open('input.txt').read()
f = open('output.txt', 'w')
for word in copypasta.split():
	# TODO clean up word
	cleaned_word = word

	f.write(word.encode('UTF-8'))

	if cleaned_word in keyword_emoji_map and len(keyword_emoji_map[cleaned_word]) > 0:
		emojis = keyword_emoji_map[cleaned_word]
		
		randIndex = random.sample(range(len(emojis)), 1)
		randIndex.sort()

		emoji = emojis[randIndex[0]]
		
		f.write(' ' + emoji.encode('UTF-8') + ' ')

	f.write(' ')

f.close()
