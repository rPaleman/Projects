import string
import nltk


def char_topgrams(raw):
    # remove punctuation
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    text = tokenizer.tokenize(raw)
    text = ''.join(text)
    text.replace(" ", "")
    grams = {}
    for n in 1, 2, 3:
        grams[n] = nltk.FreqDist(nltk.ngrams(text, n))
    print("Unigram Characters: {0}" .format(grams[1].most_common(20)))
    print("Bigram Characters: {0}" .format(grams[2].most_common(20)))
    print("Trigram Characters: {0}" .format(grams[3].most_common(20)))

    # This information could be useful to quickly spot what prefixes,
    # suffixes and verb forms are used in a text


def word_topgrams(raw):
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    # remove punctuation
    words = tokenizer.tokenize(raw)
    grams = {}
    for n in 1, 2, 3:
        grams[n] = nltk.FreqDist(nltk.ngrams(words, n))
    print("Unigram Words: {0}" .format(grams[1].most_common(20)))
    print("Bigram Words: {0}" .format(grams[2].most_common(20)))
    print("Trigram Words: {0}" .format(grams[3].most_common(20)))

    # This information could be useful to spot what kind of words
    # are used in a text. Could be used to see how difficult the
    # text is or in what language it is written


def main():
    path = "holmes.txt"
    with open(path, 'r') as f:
        # longest sentence
        rawText = f.read()
        long_sents = nltk.sent_tokenize(rawText)

    # 2A
    chars = set()
    for line in long_sents:
        chars.update([char for char in line])
    print(len(chars))
    print(sorted(chars))

    # 2B
    words_in_text = nltk.word_tokenize(rawText)
    words = set()

    words.update([word for word in words_in_text
                 if word not in string.punctuation])

    print(len(words))

    # 2C
    char_topgrams(rawText)

    # 2D
    word_topgrams(rawText)


if __name__ == '__main__':
    main()
