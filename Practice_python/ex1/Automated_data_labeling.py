with open("C:\\Users\\Thang Laptop\\Desktop\\output.txt",mode = 'w') as output_file:
    while True:
        sentence = input("Enter a sentence: ")
        if sentence == 'N':
            break;
        entities = []
        keywords = []
        labels = []

        while True:
            keyword = input("Enter a keyword: ")
            keywords.append(keyword)
            if keyword == '0':
                break;
            label = input("Enter a label: ")
            labels.append(label)
        for i in range(0,len(keywords)-1):
            index = 0;
            index = sentence.find(keywords[i])
            entities.append((index, index + len(keywords[i]), labels[i]))

        output = {'entities' : entities}
        #print(sentence,output)
        output_file.write(f"{sentence} : {output}")
