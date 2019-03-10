import nltk,csv

uniqueNouns = []
dataNouns = []
features = []
uniqueSample = []
label = []


def parseNoun():
    datatest = []
    with open('dataset.csv') as csvfile:
        datasets = csv.reader(csvfile, delimiter='\n')

        with open('nouns.csv', mode='w', newline='') as csv_file:
            fieldnames = ['Noun']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for row in datasets:
                sentence = ''.join(row)
                sentence = sentence.split('##')
                label.append(sentence[0])
                for parseData in nltk.pos_tag(nltk.word_tokenize(sentence[1])):
                    if parseData[1] == 'NN' and parseData[0] != 'i' and parseData[0] != 's100' and parseData[0] != 'canon': #PRUNNING
                        writer.writerow({'Noun': parseData[0]})

    for row in label:
        if row == '':
            pass
        else:
            datatest.append(row)

    tempDatasetSample = []
    for row in datatest:
        tempParse = ''.join(row)
        tempParse = tempParse.split(',')
        tempDatasetSample.append(tempParse)

    tempDatasetSampled = []
    for row in tempDatasetSample:
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
            dataNouns.append(row[0])
            if any(row[0] in sublist for sublist in uniqueNouns):
                pass
            else:
                uniqueNouns.append(row[0])     
        dataNouns.pop(0)
        uniqueNouns.pop(0)

def train():
    temp = []
    for trained in uniqueNouns:
        i = 0
        for row in dataNouns:
            if trained == row:
                i = i + 1
        temp.append([i, trained])
    temp.sort(reverse=True)
    
    for row in temp:
        features.append({'noun':row[1], 'count':row[0]})

def precision():
    temp = []
    for row in label:
        temps = []
        tempLabel = ''.join(row)
        tempLabel = tempLabel.split(',')
        for rows in tempLabel:
            tempLabels = ''.join(rows)
            tempLabels = tempLabels.split('[')
            temps.append(tempLabels[0])
        temp.append(temps)
    
    i = 0
    precValue = 0
    for row in temp:
        i = i + 1
        matched = 0
        for rows in row:
            for rowss in features:
                if (rowss['noun'] == rows):
                    matched = matched + 1
        precValue = (precValue + (matched / len(row)))
    print('PRECISSION: ', precValue/3, '%')
            
if __name__ == "__main__":
    parseNoun()
    train()
    precision()
    print('Top 10 features:')
    for row in features[:10]:
        print(row['noun'], '| dengan count value sebanyak: ',row['count'])