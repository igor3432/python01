nome = input ('Qual é o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))
print('='*100)

###########

n1 = int(input('Um valor: '))
n2 = int(input('Outro vamor:'))
s = n1 + n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma é {}, o produto é {} e a divisão é {}'.format(s,m,di))
print('Divisão inteira {} e potência {}'.format(di,e))
#print('soma vale {}'.format(n1+n2))
print('='*100)