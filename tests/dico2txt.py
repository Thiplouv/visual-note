fruits = {'poire' : ['comice','conférence'], 'Pomme' : ['golden','chantecler'],'Cerise' : ['burlat','reverchon', 'summit']}
fr=open('C:/Users/Thibault/Desktop/projet-python/fruits.txt','a')
for (cle,data) in fruits.items() :
    fr.write(cle+":"+data[0])
    for i in range (1,len(data)):
        fr.write(","+data[i])
    fr.write("\n")
    
fr.close()
 