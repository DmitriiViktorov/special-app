def projectIsland():
  for i in range(100, 0, -1):
    print('На дереве сидели', i, 'обезьян, но тут пришел тигр и их осталось', i - 1)
  print('Кажется всех съели')
text = input('Какое животное живет на дереве и ест бананы?')

if text == 'обезъяна' or text == 'обезъяны':
  projectIsland()
  
