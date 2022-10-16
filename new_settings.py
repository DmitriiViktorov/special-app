def projectIsland():
  for i in range(100, 0, -1):
    print('На дереве сидели', i, 'кошки , но тут пришел тигр и их осталось', i - 1)
  print('Кажется всех съели')
text = input('Какое животное живет на дереве и ест бананы?')
print('1234567890')
if text == 'кошка' or text == 'кот':
  projectIsland()
  
