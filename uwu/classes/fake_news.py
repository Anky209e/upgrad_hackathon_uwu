from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
import json
import numpy as np
from tensorflow.keras.models import load_model

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

tokenizer = Tokenizer(oov_token="<OOV>")


with open('data/fake_news.json','r') as f:
    datastore = json.load(f)

sentences = datastore["inputs"]
labels = datastore["targets"]


tokenizer.fit_on_texts(sentences)

model = load_model("weights/fake_news_99.h5")
vocab_size = 10000
embedding_dim = 16
max_length = 100
trunc_type='post'
padding_type='post'
oov_tok = "<OOV>"
training_size = 20000

def is_trainable():
    pass

def get_retrain_data(input,target):
    
    with open('data_pr.json','r') as f:
        datastore = json.load(f)
    



def predict_fake_news(text):
    
    test = [text]
    test_seq = tokenizer.texts_to_sequences(test)
    test_pad = pad_sequences(test_seq,maxlen=max_length,padding=padding_type,truncating=trunc_type)

    result = model.predict(np.array(test_pad))
    value = result[0][0]
    other_val = 1-value
    final_array = np.array([value,other_val])
    softmaxed_ar = softmax(final_array)

    classes = ['Fake','Real']
    final = list(zip(classes, softmaxed_ar))
    final.sort(key = lambda x: x[1],reverse=True)

    print(final)
    return final

if __name__=="__main__":
    print(get_retrain_data(2,3))