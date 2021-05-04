#chatbot
import pickle
import random
a=open('Dictionary','rb')
successorlist=pickle.load(a)
a.close()
def nextword(a):
    if a in successorlist:
        return random.choice(successorlist[a])
    else:
        return 'a'
question=''
while question!='quit':
    question=input('\nWhat Do you want to Know?')
    s=random.choice(question.split())
    response=''
    while True:
        neword=nextword(s)
        response+=' '+neword
        s=neword
        if neword[-1] in ',?!.':
            break
    print(response)