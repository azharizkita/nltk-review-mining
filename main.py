import nltk,csv

uniqueNouns = []
dataNouns = []
features = []
tempDataset = []
datatest = []
tempDatasetSample = []
tempDatasetSamples = []
tempDatasetSampled = []
uniqueSample = []


def parseNoun():
    with open('dataset.csv') as csvfile:
        datasets = csv.reader(csvfile, delimiter='\n')

        with open('nouns.csv', mode='w', newline='') as csv_file:
            fieldnames = ['Noun']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for row in datasets:
                sentence = ''.join(row)
                sentence = sentence.split('##')
                tempDataset.append(sentence[0])
                for parseData in nltk.pos_tag(nltk.word_tokenize(sentence[1])):
                    if parseData[1] == 'NN' and parseData[0] != 'i' and parseData[0] != 's100' and parseData[0] != 'canon': #PRUNNING
                        writer.writerow({'Noun': parseData[0]})

    for row in tempDataset:
        if row == '':
            pass
        else:
            datatest.append(row)

    for row in datatest:
        tempParse = ''.join(row)
        tempParse = tempParse.split(',')
        tempDatasetSample.append(tempParse)

    for row in tempDatasetSample:
        for data in row:
            tempDatasetSamples.append(data)

    for row in tempDatasetSamples:
        tempParse = ''.join(row)
        tempParse = tempParse.split('[')
        tempDatasetSampled.append(tempParse[0])
        for row in tempDatasetSampled:
            if any(row in sublist for sublist in uniqueSample):
                pass
            else:
                uniqueSample.append(row) 

    with open('nouns.csv') as csvfile:
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
    
def accuracy(x):
    totalFeature = 0
    matched = 0
    for row in features[:x]:
        totalFeature = totalFeature + 1
        for rows in uniqueSample:
            if rows in row[1]:
                matched = matched + 1
    return [matched, totalFeature]
            
if __name__ == "__main__":
    parseNoun()
    train()

    totalUniqueSample = 0
    for row in uniqueSample:
        totalUniqueSample = totalUniqueSample + 1
    
    print('total unique samples: ', totalUniqueSample)
    finalResult = accuracy(10)
    print(finalResult[0],' / ',finalResult[1])
    print('Accuracy = ',(finalResult[0] / finalResult[1]) * 100, '%')
    print('Extracted features:')
    for row in features[:10]:
        print(row)