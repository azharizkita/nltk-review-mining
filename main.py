import nltk,csv

uniqueNouns = []
dataNouns = []
features = []

def parseNoun():
    with open('dataset.csv', newline='') as csvfile:
        datasets = csv.reader(csvfile, delimiter='\n')
        i = 1

        with open('nouns.csv', mode='w') as csv_file:
            fieldnames = ['Noun']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for row in datasets:
                sentence = ''.join(row)
                sentence = sentence.split('##')
                for parseData in nltk.pos_tag(nltk.word_tokenize(sentence[1])):
                    if parseData[1] == 'NN' and parseData[0] != 'i':
                        writer.writerow({'Noun': parseData[0]})

    with open('nouns.csv', newline='') as csvfile:
        nouns = csv.reader(csvfile, delimiter='\n')
        for row in nouns:
            dataNouns.append([row[0]])
            if any(row[0] in sublist for sublist in uniqueNouns):
                pass
            else:
                uniqueNouns.append([row[0]])         

def train():
    for trained in uniqueNouns:
        i = 0
        for row in dataNouns:
            if trained[0] == row[0]:
                i = i + 1
        features.append([i, trained])

    features.sort(reverse=True)

if __name__ == "__main__":
    parseNoun()
    train()
    for row in features[:20]:
        print(row)