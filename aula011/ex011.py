largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura 
print('Sua área tem a dimensão de {}x{} e sua área é de {}m²'.format(largura,altura ,area))
tinta = area / 2 
print('Para pintar sua parede você precisa de {}L de tinta'.format(tinta))