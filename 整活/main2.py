with open("data.txt","r",encoding="utf-8") as file:
    content = file.read()
chars = list(set(content))
n_chars = len(chars)
char_indices = dict((c,i) for i,c in enumerate(chars))
indices_chars = dict((i,c) for i,c in enumerate(chars))


maxlen=20
step=3
'''
sentences = []
next_chars = []
for i in range(0,len(content)-maxlen,step):
    sentences.append(content[i:i+maxlen])
    next_chars.append(content[i+maxlen])
'''
import numpy as np
from keras.models import load_model
model = load_model("models.LSTM")

def sample(preds,rate=1.0):
    preds = np.asarray(preds).astype("float64")
    preds = np.log(preds)/rate
    exp_preds = np.exp(preds)
    preds = exp_preds/np.sum(exp_preds)
    probas = np.random.multinomial(n=1,pvals=preds,size=1)
    return np.argmax(probas)

def creater(inputs,length=30,rate=0.9):
    words = ""
    for i in range(length):
        x_preds = np.zeros((1,maxlen,n_chars))
        for i,chars in enumerate(inputs):
            x_preds[0,i,char_indices[chars]]=1
        preds = model.predict(x_preds,verbose=0)[0]
        next_index = sample(preds,rate)
        next_char = indices_chars[next_index]
        words += next_char
        inputs = inputs[1:] + next_char
    return words
import random
def main():
    while True:
        try:
            #inputs = input(">>>")
            start=random.randint(0,len(content)-maxlen)
            inputs=content[start:start+maxlen]
            print(">>>:"+inputs+"<<<")
            print("---:"+creater(inputs))
        except Exception as e:
            print("ERROR",e)
main()
