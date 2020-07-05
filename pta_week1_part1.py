import nltk


def main():
    path = "holmes.txt"
    with open(path, 'r') as f:
        # longest sentence
        rawText = f.read()
    long_sents = nltk.sent_tokenize(rawText)

    longest_len = max([len(s) for s in long_sents])
    longest_sentence = ([s for s in long_sents
                        if len(s) == longest_len])
    for sent in longest_sentence:
        sentence = ""
        for word in sent.split():
            sentence += " " + word
        print(sentence)

    # shortest sentence
    split_text = rawText.split(".")
    text = []
    for line in split_text:
        text.append(line)
    longstring = " ".join(text)
    short_sents = nltk.sent_tokenize(longstring)
    shortest_len = min([len(s) for s in short_sents])
    shortest_sentence = ([s for s in short_sents
                         if len(s) == shortest_len])

    for sent in shortest_sentence:
        sentence = ""
        for word in sent:
            sentence += word
        print(sentence)

    # C
    d = {}
    for i in long_sents:
        if len(i) in d:
            d[len(i)] += 1
        else:
            d[len(i)] = 1
    for key, value in sorted(d.items()):
        print("occurences of sent. length : {0} = {1}".format(key, value))

    # D
    total_length = 0

    for i, sentence in enumerate(long_sents):
        total_length += len(sentence)
    average = total_length / i
    print(average)


if __name__ == "__main__":
    main()
