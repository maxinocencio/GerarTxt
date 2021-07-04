lista = []

#print('-='*30)

entry = input('Digite algo: ')
lista.append(entry)

with open('texto.txt', "w") as writer:
    for x in lista:
        writer.write(x+'\n')

print('')
print('Seu txt foi criado')