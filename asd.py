liste = [3,1,7,2,8,5]
yeniliste = []
for i in range(len(liste)):
    yeniliste.append(min(liste))
    liste.remove(min(liste))
    
print(yeniliste)
    
