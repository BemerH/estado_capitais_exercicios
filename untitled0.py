estadosLis = ['Bahia','Maranhão','Piauí','Ceará','Rio Grande do Norte',
              'Paraíba','Pernambuco','Alagoas','Sergipe','Minas Gerais',
              'Espirito Santo','São Paulo','Rio de Janeiro']

capitaisLis = ['Salvador','São Luis','Teresina','Fortaleza'
               ,'Natal','João Pessoa','Recife','Maceió','Aracajú',
               'Belo Horizonte','Vitória','São Paulo','Rio de Janeiro']

print("Seja bem vindo!\n")
print("Através deste algoritmo você pode aprender os estados")
print("e capitais do Brasil!\n")
print("Digite o estado no qual deseja saber a capital ou")
print("digite a capital para saber o estado!\n")
print("Digite 0 se você quiser sair\n")

aux = None

while(not aux):
    
    palavra = input('Digite um estado ou capital:\n')
    
    if palavra == '0':
        break
    else:
        for i in range(len(estadosLis)):
            if estadosLis[i] == palavra: #or capitaisLis[i] == palavra:
                print('Estado: '+estadosLis[i]+'\nCapital: '+capitaisLis[i])
                #break
            elif capitaisLis[i] == palavra:
                print('Estado: '+estadosLis[i]+'\nCapital: '+capitaisLis[i])
                #break
            #else:
            #   print("Entreda incorreta! Tente novamente")
            #print()
            #break
print('\nObrigado, volte sempre')    