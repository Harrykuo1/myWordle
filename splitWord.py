from fileinput import filename


src = open("words_alpha.txt", "r")
wordFile = []
for i in range(31):
    wordFile.append(open("Word/"+str(i)+".txt","w"))
i=0
try:

    while True:
        i+=1
        if(i>370103):
            break
        tmp = src.readline()
        
        tmp = ''.join(tmp).strip('\n')
        tmpLen = len(tmp)
        if(tmpLen>30):
            continue
        wordFile[tmpLen].write(tmp)
        wordFile[tmpLen].write('\n')

except EOFError:
    
    pass