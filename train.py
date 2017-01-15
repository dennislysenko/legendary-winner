from gensim.models import word2vec

sentences = word2vec.LineSentence('corpora/corpus_final.txt')
model = word2vec.Word2Vec(sentences, size=100, window=5, min_count=5, workers=4)
model.save('model.w2v')
