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
import modelsTopic
# import mysql.connector
# mydb = mysql.connector.connect(
#     host="192.168.100.34",
#     user="root",
#     # passwd="lmao",
#     database="tweetapi"

# )

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


# list of models names
models = ['1_2', '1_4', '2_12', '2_9']
topicsName = ['food_cat', 'eco_cat', 'tech_cat', 'pol_cat']


def getMostLikelyTopic(topics, model):
    # print(topics)
    # print ("get most likely topic")
    max = (topics[0])[1]
    # print(max)
    topicId = 0
    # print('topic ', topics)
    # print(max)
    index = 0
    # print(len(model))
    while (index < len(topics)):
        print("(loop) topicId: ",(topics[index])[0])
        try:
            # print((topics[index])[1])
            # print(topics[index])
            # print((topics[index])[1] > max)
            if (topics[index])[1] >= max:
                # print (dict[index])
                max = (topics[index])[1]
                topicId = (topics[index])[0]
            # print(max)
        # print('most likely topic is: ',max)
        except:
            # traceback.print_exception()ư
            print("error")
            # traceback.print_exc()
        index = index+1

    if (type(topicId) != int):
        topicId = topicId[0]

    # print(type(topicId))
    # print(model[topicId])
    print("topic id from selection ",topicId)
    # print('model length ', len(model))
    # print(model[topicId])
    print("topic id in model: ", modelsTopic.getModelIndex(model, topicId))
    try:
        topicName = topicsName[modelsTopic.getModelIndex(model, topicId)-1]
        print("topic name: ", topicName)
    except:
        print("error get topic")
    return topicName


def compareModelResult(topic):
    # print(topic)
    f_count = topic.count('food_cat')
    e_count = topic.count('eco_cat')
    t_count = topic.count('tech_cat')
    p_count = topic.count('pol_cat')
    print(f_count, e_count, t_count, p_count)
    if (f_count >= e_count and f_count >= t_count and f_count > p_count):
        return 'food_cat'
    elif (e_count >= f_count and e_count >= t_count and e_count > p_count):
        return 'eco_cat'
    elif (t_count >= f_count and t_count >= e_count and t_count > p_count):
        return 'tech_cat'
    else:
        return 'pol_cat'


text_data = []
with open('C:\\\\Users\\USER\\Desktop\\SS2\\NLP\\combined.csv', encoding="utf8") as f:
    for line in f:
        tokens = prepare_text_for_lda(line)
        # if random.random() > .99:
        try:
            # print(tokens)
            text_data.append(tokens)
        except:
            continue
dictionary = corpora.Dictionary(text_data)
corpus = [dictionary.doc2bow(text) for text in text_data]
pickle.dump(corpus, open('corpus.pkl', 'wb'))
dictionary.save('dictionary.gensim')


def categorizes(input_text):
    topic = []
    model = models[2]
    # for model in models:
    ldamodel = gensim.models.ldamodel.LdaModel.load(
        "models/"+model + '.gensim')
    new_doc = input_text
    new_doc = prepare_text_for_lda(new_doc)
    new_doc_bow = dictionary.doc2bow(new_doc)
    # print(new_doc_bow)
    topics = ldamodel.get_document_topics(new_doc_bow)
    print("document topics from lda ",topics)
    if (len(topics)==1):
        print((topics[0])[0])
        modelIndex =modelsTopic.getModelIndex(model, 11)
        # print(topicsName[modelIndex-1])
        return topicsName[modelIndex-1]
    else:
        prob = getMostLikelyTopic(topics, model)
        topic.append(prob)
        print("most likely topic ",topic)
        # comparing each model result to get topic
        # topicResult = compareModelResult(topic)
        return prob

# def insertTweet(text, poster):
#     mycursor = mydb.cursor()
#     topic  = categorizes(text)
#     sql = "INSERT INTO "+topic+" (content, poster) VALUES (%s, %s)"
#     val = (text, poster)
#     mycursor.execute(sql, val)
#     mydb.commit()
#     print(mycursor.rowcount, "record inserted.")  


# for i in range(10):
    # try:
print(categorizes(
    "Here's What To Know About The 2018 Women's March,Women are dusting off their pussy hats for round two."))
# except:
# continue
