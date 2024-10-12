from model.Classifier_API import sentimentAnalysis
import numpy as np

fname='test.txt'

with open(fname,'r+',encoding='utf-8') as f:
    # for line in f.readlines():
        # print(line[:-1].split(','))
    s = [i[:-1].split(',') for i in f.readlines()]
    s = np.squeeze(np.array(s))

print(s.size)
predSentiment=np.zeros((len(s)))
for i in range(len(s)):
    predSentiment[i]=sentimentAnalysis(s[i])
    print(f'{s[i]} sentiment:{predSentiment[i]}')

