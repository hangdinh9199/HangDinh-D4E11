import random
word_list = ['cream', 'cheese', 'cake']
n = random.choice(word_list)
x = list(n)
random.shuffle(x)
#print(x)
for i in range(len(x)):
    print(x[i].upper(), end='')

guess_what = input('What is your answer?')
if guess_what == n:
    print('Bingo')
else:
    print('Game over')