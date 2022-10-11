from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
import json
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional

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

def retrain(datastore):
    train_sentences = datastore["inputs"]
    train_targets = datastore["targets"]
    train_sequences = tokenizer.texts_to_sequences(train_sentences)
    train_padded = pad_sequences(train_sequences)
    training_size = 40

    training_sentences = train_sentences[0:training_size]
    testing_sentences = train_sentences[training_size:]

    training_labels = train_targets[0:training_size]
    testing_labels = train_targets[training_size:]
    training_sequences = tokenizer.texts_to_sequences(training_sentences)
    training_padded = pad_sequences(training_sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)

    testing_sequences = tokenizer.texts_to_sequences(testing_sentences)
    testing_padded = pad_sequences(testing_sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)
    training_padded = np.array(training_padded)
    training_labels = np.array(training_labels)
    testing_padded = np.array(testing_padded)
    testing_labels = np.array(testing_labels)
    print("Loading Model for retraining..")
    model = load_model("weights/fake_news_lstm_r2.h5")
    history = model.fit(training_padded, training_labels, epochs=3, validation_data=(testing_padded, testing_labels), verbose=2)
    print("Saving new retrained weights..")
    model.save('weights/fake_news_lstm_r2.h5')
    print(history)
    
    

def get_retrain_data(input,target):
    with open('data/retrain_news.json','r') as f:
        datastore = json.load(f)

    if datastore["real_targets"] < 50:
        if target:
            datastore["inputs"].append(input)
            datastore["target"].append(target)
            datastore["real_targets"]+=1
    elif datastore["fake_targets"] < 50:
        if not target:
            datastore["inputs"].append(input)
            datastore["target"].append(target)
            datastore["fake_targets"]+=1
    else:
        retrain(datastore)


    json_object = json.dumps(datastore, indent=4)

    with open("data/retrain_news.json", "w") as outfile:
        outfile.write(json_object)


def predict(text):
    with tf.device('/cpu:0'):
        model = load_model("weights/fake_news_lstm_r2.h5")
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