

import re

class TwitterPositive():
    def __init__(self):
        # do some initialization, optional
        pass

    def evaluateTweet(self, tweet):
        # please implement this function
        # input: any tweet text
        # output: a score [0,1], 0 means it is low quality and negative, 1 means it is high quality and positive

        delimiters = "[,;|\\s]+"

        words = re.split(delimiters, tweet)

        two_gram = TwitterPositive.twoGram(words)
        print(two_gram)

        return 0.5
    
    def twoGram(lis):

        result = []

        for i in range(len(lis)):
            if i == len(lis)-1:
                break
            else:
                result.append(lis[i] + " " + lis[i+1])
            
        return result
                


# this is for testing only
obj = TwitterPositive()
if obj.evaluateTweet("DATA 233 is a wonderful class!") >= 0.5:
    print("Great, it is positive")
else:
    print("negative")

    
