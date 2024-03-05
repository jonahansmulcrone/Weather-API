

import re

# Student Name 1: Brian Sung
# Student Name 2: Emmanuel Obikwelu
# Student Name 3: Jonah Mulcrone

def countWor(lis):
    word_counts = {}
    sum = 0
    # Iterate over each string in the list
    for string in lis:
        # Split the string into words
        words = string.split()
        # Iterate over each word in the list
        for word in words:
            # Update the count for the word in the dictionary
            word_counts[word] = word_counts.get(word, 0) + 1

    # Print the word counts
    for word, count in word_counts.items():
        if count > 2:
            sum = sum + count
    return sum


class TwitterPositive():
    def __init__(self):
        # do some initialization, optional
        pass

    def evaluateTweet(self, tweet):
        # please implement this function
        # input: any tweet text
        # output: a score [0,1], 0 means it is low quality and negative, 1 means it is high quality and positive

        positive_words = [
            'good', 'excellent', 'great', 'awesome', 'fantastic',
            'amazing', 'wonderful', 'superb', 'brilliant', 'outstanding',
            'terrific', 'fabulous', 'incredible', 'perfect', 'marvelous',
            'delightful', 'splendid', 'phenomenal', 'exceptional', 'stellar',
            'remarkable', 'extraordinary', 'top-notch', 'first-rate', 'superior',
            'impressive', 'magnificent', 'glorious', 'sublime', 'majestic',
            'divine', 'exemplary', 'praiseworthy', 'admirable', 'commendable',
            'heartwarming', 'joyful', 'uplifting', 'inspiring', 'positive',
            'optimistic', 'ecstatic', 'blissful', 'euphoric', 'thrilling',
            'sensational', 'electrifying', 'captivating', 'enchanting', 'charming',
            'enticing', 'alluring', 'engaging', 'invigorating', 'refreshing',
            'energizing', 'stimulating', 'vibrant', 'dynamic', 'alive', 'radiant',
            'cheerful', 'lively', 'vivacious', 'buoyant', 'spirited', 'exhilarating',
            'festive', 'celebratory', 'jubilant', 'festive', 'gleeful', 'playful',
            'delicious', 'scrumptious', 'mouthwatering', 'tasty', 'flavorful',
            'satisfying', 'fulfilling', 'gratifying', 'nourishing', 'wholesome',
            'beneficial', 'heavenly', 'divine', 'sumptuous', 'lavish', 'opulent',
            'luxurious', 'gorgeous', 'beautiful', 'stunning', 'breathtaking',
            'mesmerizing', 'enchanting', 'fascinating', 'captivating', 'hypnotic',
            'bewitching', 'enticing', 'spellbinding', 'charismatic', 'alluring', 'wonderful'
        ]

        negative_words = [
            'bad', 'poor', 'terrible', 'horrible', 'awful',
            'mediocre', 'subpar', 'inferior', 'unsatisfactory', 'disappointing',
            'unpleasant', 'unfavorable', 'negative', 'dreadful', 'lousy',
            'abysmal', 'atrocious', 'ghastly', 'miserable', 'wretched',
            'deplorable', 'appalling', 'disgusting', 'repulsive', 'revolting',
            'offensive', 'vile', 'disgraceful', 'shameful', 'abominable',
            'detestable', 'horrifying', 'repugnant', 'odious', 'noxious',
            'repellent', 'unsavory', 'distasteful', 'unwelcome', 'unwanted',
            'disheartening', 'discouraging', 'demoralizing', 'depressing', 'gloomy',
            'melancholy', 'dreary', 'sorrowful', 'mournful', 'bleak',
            'despondent', 'dismal', 'grievous', 'tragic', 'pitiful',
            'heartbreaking', 'heart-wrenching', 'saddening', 'tearful', 'unfortunate',
            'unlucky', 'troublesome', 'problematic', 'difficult', 'challenging',
            'frustrating', 'annoying', 'irritating', 'exasperating', 'aggravating',
            'bothersome', 'disruptive', 'displeasing', 'discontented', 'disgruntled',
            'grumpy', 'miserable', 'crummy', 'irksome', 'pesty', 'vexing',
            'maddening', 'provoking', 'enraging', 'infuriating', 'outrageous',
            'intolerable', 'unbearable', 'exasperating', 'anger-inducing', 'irksome',
            'troublesome', 'annoying', 'bothersome', 'irritating', 'frustrating',
            'aggravating', 'infuriating', 'vexing', 'maddening', 'galling',
            'exasperating', 'peeving', 'perturbing', 'trying', 'nagging'
        ]


        delimiters = "[,;|\\s]+"

        words = re.split(delimiters, tweet)

        two_gram = TwitterPositive.twoGram(words)

        num_positive_words = sum(4 for word in tweet.split() if word.lower() in positive_words)
        num_negative_words = sum(1 for word in tweet.split() if word.lower() in negative_words)
        #print(num_positive_words)
       # print(num_negative_words)

        total_words = len(tweet.split())
       # print(total_words)
        if total_words == 0:
            return 0.0
        else:
            positive_ratio = num_positive_words / total_words

        occu = countWor(two_gram)


        #print(occu)


        score = positive_ratio - ((occu+num_negative_words) / total_words)


        score = max(0, min(score, 1))


        #print(two_gram)

        return score
    
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
if obj.evaluateTweet("DATA 233 is a bad good good class class!") >= 0.5:
    print("Great, it is positive")
else:
    print("negative")

    
