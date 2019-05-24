# encoding: utf-8
dset = ['foods', 'politics', 'tech', 'economics']
file = open('combined.csv', 'w+')
for d in dset:
    file.write("--------------------------------------------"+d+'---------------------------------------------')
    size = 0
    with open('C:\\\\Users\\USER\\Desktop\\SS2\\NLP\\training_data\\'+d+'.csv',encoding="utf8") as f:
        for line in f:
            if size == 2805:
                break
            try:
                file.write(line)
            except:
                continue
            size = size+1
file.close