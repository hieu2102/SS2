# encoding: utf-8
import spacy
from nltk.stem.wordnet import WordNetLemmatizer
from spacy.lang.en import English
import random
import nltk
from nltk.corpus import wordnet as wn
import gensim
from gensim import corpora
import pickle
import xlwt
import os
# prepare spacy parser -> get text structure
spacy.load('en')
parser = English()
# basically a dictionary
# nltk.download('wordnet')
# get English stopwords
# nltk.download('stopwords')
en_stop = set(nltk.corpus.stopwords.words('english'))

# tokenize input


def tokenize(text):
    lda_tokens = []
    tokens = parser(text)
    for token in tokens:
        if token.orth_.isspace():
            continue
        elif token.like_url:
            lda_tokens.append('URL')
        elif token.orth_.startswith('@'):
            lda_tokens.append('SCREEN_NAME')
        else:
            lda_tokens.append(token.lower_)
    return lda_tokens


def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma


def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)


def prepare_text_for_lda(text):
    tokens = tokenize(text)
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in en_stop]
    tokens = [get_lemma(token) for token in tokens]
    return tokens


# text_data = []
# with open('C:\\\\Users\\USER\\Desktop\\SS2\\NLP\\training_data\\dataset.csv',encoding="utf8") as f:
#     for line in f:
#         tokens = prepare_text_for_lda(line)
#         if random.random() > .99:
#             try:
#                 # print(tokens)
#                 text_data.append(tokens)
#             except:
#                 continue
# dictionary = corpora.Dictionary(text_data)
# corpus = [dictionary.doc2bow(text) for text in text_data]
# pickle.dump(corpus, open('corpus.pkl', 'wb'))
# dictionary.save('dictionary.gensim')
# NUM_TOPICS = 4
# ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = NUM_TOPICS, id2word=dictionary, passes=150)
# # ldamodel.save('model5.gensim')
# topics = ldamodel.print_topics(num_words=10)
# for topic in topics:
#     print(topic)
# new_doc = "When it comes to cakes, the more layers it has, the more impressive it feels -- that's why crepe cakes always seem so special"
# new_doc = prepare_text_for_lda(new_doc)
# new_doc_bow = dictionary.doc2bow(new_doc)
# print(new_doc_bow)
# print(ldamodel.get_document_topics(new_doc_bow))
NUM_TOPICS = 20
# def getLargestValue(dict):
#     print(dict)
#     # print ("get most likely topic")
#     max = (dict[0])[1]
#     # print(max)
#     index =1
#     while (index <NUM_TOPICS):
#         if (dict[index])[1]> max:
#             # print (dict[index])
#             max = (dict[index])[1]
#         index=index+1
#     # print('most likely topic is: ',max)
#     return max
text_data = []
with open('C:\\\\Users\\USER\\Desktop\\SS2\\NLP\\combined.csv', encoding="utf8") as f:
    for line in f:
        tokens = prepare_text_for_lda(line)
        if random.random() > .99:
            try:
                # print(tokens)
                text_data.append(tokens)
            except:
                continue
dictionary = corpora.Dictionary(text_data)
corpus = [dictionary.doc2bow(text) for text in text_data]
pickle.dump(corpus, open('corpus.pkl', 'wb'))
dictionary.save('dictionary.gensim')
times = 0
base_dir = "C:\\Users\\USER\\Desktop\\SS2"
while times < 3:
    count = 0
    excel = xlwt.Workbook()
    while count < 200:
        if not os.path.exists('set'+str(times)+'\\model\\'+str(count)):
            os.makedirs('set'+str(times)+'\\model\\'+str(count))
        ws = excel.add_sheet('Model '+str(count))
        ldamodel = gensim.models.ldamodel.LdaModel(
            corpus, num_topics=NUM_TOPICS, id2word=dictionary, passes=3)
        ldamodel.save('set'+str(times)+'\\model\\'+str(count)+'\\model.gensim')
        topics = ldamodel.print_topics(num_words=15)
        ws.write(0,0,"Topic")
        ws.write(0,1,"Keywords")
        row = 1
        for topic in topics:
            # print(topic)
            ws.write(row, 1, str(topic))
            row = row+1
        count = count+1
    excel.save('NLP Model Set '+str(times)+'.xls')
    times = times + 1
