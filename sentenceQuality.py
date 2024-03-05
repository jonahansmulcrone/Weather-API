# Student Name 1: Brian Sung
# Student Name 2: Emmanuel Obikwelu
# Student Name 3: Jonah Mulcrone

from textblob import TextBlob

class sentenceQuality():
    def __init__(self):
        # do some initialization, optional
        pass

    def count_letters_and_numbers(input_string):
        count = 0
        for char in input_string:
            if char.isalnum():
                count += 1
        return count

    def calculateScores(self, tweet):
        # please implement this function
        # input: any tweet text
        # output: a list of scores for the tweet, it must include: score for length, score for Polarity, score for Subjectivity, and at least one score of the following:
        # https://en.wikipedia.org/wiki/Automated_readability_index
        # https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests
        # https://en.wikipedia.org/wiki/Gunning_fog_index
        # https://en.wikipedia.org/wiki/SMOG
        # https://en.wikipedia.org/wiki/Fry_readability_formula
        # https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index
        # You should implement at least one score

        texts = TextBlob(tweet)

        print(texts.sentiment)

        subj = texts.sentiment.subjectivity
        polar = texts.sentiment.polarity

        charater = float(sentenceQuality.count_letters_and_numbers(tweet))
        words = float(len(texts.words))
        num_sentens = len(texts.sentences)
        print(words)
        print(charater)
        automated = float(4.71*(charater/words) + 0.5*(words/num_sentens) - 21.73)


        return [len(tweet)/100, polar, subj, automated]
        pass

    def calculateQuality(self, scores):
        # please implement this function to calculate a final quality score between 0 and 1
        # Input: a list of scores, which is the output of calculateScores
        # output: 0 means low quality, 1 mean high quality

        return sum(scores)/len(scores)
        pass


# this is for testing only
obj = sentenceQuality()
s = "DATA 233 is a wonderful class!"

print("The scores for your input is " + str(obj.calculateScores(s)))

print("The final quality for your input is " + str(obj.calculateQuality(obj.calculateScores(s))))
