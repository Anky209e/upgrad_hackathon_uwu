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
with tf.device('/cpu:0'):
    tokenizer = Tokenizer(oov_token="<OOV>")


with open('data/fake_news.json','r') as f:
    datastore = json.load(f)

sentences = datastore["inputs"]
labels = datastore["targets"]

with tf.device('/cpu:0'):
    tokenizer.fit_on_texts(sentences)

vocab_size = 10000
embedding_dim = 16
max_length = 100
trunc_type='post'
padding_type='post'
oov_tok = "<OOV>"
training_size = 20000

def is_trainable():
    with open('data/retrain_news.json','r') as f:
        datastore = json.load(f)
    if (datastore["fake_targets"] >= 50) and (datastore["real_targets"] >= 50):
        return True
    return False
    

def get_retrain_data(input,target):
    with open('data/retrain_news.json','r') as f:
        datastore = json.load(f)

    datastore["inputs"].append(input)
    datastore["target"].append(target)
    datastore["fake_targets"]+=1
    datastore["real_targets"]+=1
    json_object = json.dumps(datastore, indent=4)

    with open("data/retrain_news.json", "w") as outfile:
        outfile.write(json_object)


def predict(text):
    with tf.device('/cpu:0'):
        model = load_model("weights/fake_news_99.h5")
        test = [text]
        test_seq = tokenizer.texts_to_sequences(test)

        for i in range(len(test_seq[0])):
            if test_seq[0][i]>10000:
                test_seq[0][i] = 1

        print(test_seq[:30])

        test_pad = pad_sequences(test_seq,maxlen=max_length,padding=padding_type,truncating=trunc_type)

        padded = np.array(test_pad)
        print(len(padded))

        result = model.predict(padded)

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