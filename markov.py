import numpy as np
from random import seed
from random import randint

def markovData():
    file = open("clean.txt", encoding = "ISO-8859-1").read()

    corpus = file.split()

    def make_pairs(corpus):
        for i in range(len(corpus)-1):
            yield (corpus[i], corpus[i+1])
            
    pairs = make_pairs(corpus)

    word_dict = {}

    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]

    first_word = np.random.choice(corpus)

    chain = [first_word]

    num_words = randint(5, 12)

    for i in range(num_words):
        chain.append(np.random.choice(word_dict[chain[-1]]))

    res = ' '.join(chain)

    punctuation = ['.', '!', '?', '...']

    rand_punctuation = randint(0, 3)
    open('clean.txt', 'w').close()


    return(res.capitalize() + punctuation[rand_punctuation])

if __name__ == "__main__":
    markovData()