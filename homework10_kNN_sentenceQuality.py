# name 1:
# name 2:
# name 3:


class kNNsentenceQuality():
    def __init__(self):
        # do some initialization, optional
        pass
    def trainkNN(self, trainingData, kNNmodel):
        # traing a kNN model on the training dataset, your group should find a training dataset with three different qualities

        pass

    def Quality_kNN(self, sentence, kNNmodel):
        # please implement this function to classify the sentence into three different classes: high, low, and medium quality. Using the kNNmodel trained by kNN
        # Input: sentence
        # output: -1 means low quality, 0 means medium quality, 1 means high quality
        # notes: You may reuse your previous homework, and calculate the features for each input sentence, and then use kNN to classify the input sentence

        return 0
        pass


# this is for testing only
obj = kNNsentenceQuality()
s = "DATA 233 is a wonderful class!"

print("The final quality for your input using kNN is " + str(obj.Quality_kNN(s)))
