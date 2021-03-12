import random
from time import sleep

#карты
nominal = {
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10': 10,
    'J' : 2,
    'Q' : 3,
    'K' : 4,
    'A' : 11
}

#####
mKoloda = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
koloda = []
for m in ["♥","♦","♣","♠"]:
    for i in mKoloda:
        koloda.append(i+m)

card = None

def A(i, iPoints):
    for x in range(0,len(i)):
        if i[x][0] == "A" and iPoints[x] == 11:
            iPoints[x] = 1

    return iPoints
#####

#игра
my = [] #набор моих карт
my_points = []  #накопление моих очков
bot = []
bot_points = [] #накопление очков крупье (бота)
game = 'play'
game_bot = 'play'
#x = random.sample(koloda, 1)
#my.append(x[0])
#my_points.append(nominal.get(x[0]))
#print('вам выпало', x[0])
#####
random.shuffle(koloda)
card = koloda.pop()
my.append(card)
my_points.append(nominal.get(card[0]))
#####

print('вам выпало', card)
print(my, 'это ваш набор карт на данный момент. Очков:'+str(sum(my_points)))
while game == 'play':
    choice = input('берете еще?')
    if choice == 'да':
        #x = random.sample(koloda, 1)
        #my.append(x[0])
        #my_points.append(nominal.get(x[0]))
        #print('вам выпало', x[0])
        #####
        random.shuffle(koloda)
        card = koloda.pop()
        my.append(card)
        my_points.append(nominal.get(card[0]))
        print('вам выпало', card)
        #####
        if sum(my_points) > 21:
            my_points = A(my, my_points)
        print(my, 'это ваш набор карт на данный момент. Очков:'+str(sum(my_points)))
        if sum(my_points) > 21:
            game = 'stop'
    elif choice == 'нет':
        game = 'stop'
while game_bot == 'play':
    #y = random.sample(koloda, 1)
    #bot_points.append(nominal.get(y[0]))
    print("Крупье берет карту...")
    sleep(random.randint(100,500)/100)
    random.shuffle(koloda)
    card = koloda.pop()
    bot.append(card)
    bot_points.append(nominal.get(card[0]))


    if sum(bot_points) > 21:
        bot_points = A(bot, bot_points)
    print("Крупье выпало ", card)
    print("Его карты: ", bot, ". Очков: ", sum(bot_points))
    sleep(random.randint(10,300)/100)
    if sum(bot_points) > 15:
        game_bot = 'stop'

print("---------------")
#подсчёт очков
print("Ваши карты: ", my)
print("Крупье карты: ",  bot)
if sum(my_points) > 21:
    print('вы проиграли')
    print('ваши очки:', sum(my_points),'очки крупье:', sum(bot_points))
elif sum(bot_points) > 21:
    print('вы выиграли'),
    print('ваши очки:', sum(my_points),'очки крупье:', sum(bot_points))
else:
    if sum(my_points) > sum(bot_points):
        print('вы выиграли'),
        print('ваши очки:', sum(my_points), 'очки крупье:', sum(bot_points))
    else:
        print('вы проиграли')
        print('ваши очки:', sum(my_points), 'очки крупье:', sum(bot_points))

#"""
