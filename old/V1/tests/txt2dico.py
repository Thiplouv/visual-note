eleves=open('C:/Users/Thibault/Desktop/projet-python/data_matieres.txt','r')
datamat =dict()
ligne = eleves.readline()
while ligne != "" :
    A = str(ligne[0:-1])
    B = A.split(":")
    cle=B[0]
    data=B[1].split(",")
    datamat[cle]=data
    ligne = eleves.readline()

print (datamat)