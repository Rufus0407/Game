import random

from enum import Enum

playerDamage = 4
playerLife = 100


def find_aprox_value(value):
    lowestValue = 0.9 * value
    highestValue = 1.1 * value
    return random.randint(lowestValue, highestValue)


def weapon_hit(chance):
    if_hit = random.uniform(1, 100)
    if if_hit < chance:
        monsterLife[drawnMonster] = monsterLife[drawnMonster] - playerDamage
        print("You hit a monster and you dealt 4 damage. It has", monsterLife[drawnMonster], " life")
    else:
        print("You missed")


def monster_hit():
    global playerLife
    monsterHit = monsterDamage[drawnMonster]
    print("Monster did", monsterDamage[drawnMonster], "damage")
    playerLife = playerLife - monsterHit
    print("You have ", playerLife, "life")


Event = Enum('Event', ['Chest', 'Monster'])
Chest = Enum('Chest', {'greenChest': 'zieloną skrzynię',
                       'blueChest': 'niebieską skrzynię',
                       'violetChest': 'fioletową skrzynię',
                       'orangeChest': 'pomarańczową skrzynię'
                       })
Monster = Enum('Monster', {'Rat': 'Szczura',
                           'Bat': 'Nietoperza',
                           'GiantSpider': 'Ogromnego Pająka',
                           'Wolf': 'Wilka',
                           })

Color = Enum('Color', ['greenChest', 'blueChest', 'violetChest', 'orangeChest'])
MonsterKind = Enum('MonsterKind', ['Rat', 'Bat', 'GiantSpider', 'Wolf'])

eventDictionary = {

    Event.Chest: 0.4,
    Event.Monster: 0.6
}

eventList = list(eventDictionary.keys())
eventProbability = list(eventDictionary.values())

chestDictionary = {
    Chest.greenChest: 0.5,
    Chest.blueChest: 0.3,
    Chest.violetChest: 0.15,
    Chest.orangeChest: 0.05
}
PremiumChestDictionary = {
    Chest.blueChest: 0.5,
    Chest.violetChest: 0.35,
    Chest.orangeChest: 0.15
}

MonsterDictionary = {
    Monster.Rat: 0.5,
    Monster.Bat: 0.3,
    Monster.GiantSpider: 0.15,
    Monster.Wolf: 0.05
}

chestList = list(chestDictionary.keys())
chestProbability = list(chestDictionary.values())

MonsterList = list(MonsterDictionary.keys())
MonsterProbability = list(MonsterDictionary.values())

PremiumChestList = list(PremiumChestDictionary.keys())
PremiumChestProbability = list(PremiumChestDictionary.values())

colorValue = {
    Chest.greenChest: 1000,
    Chest.blueChest: 4000,
    Chest.violetChest: 9000,
    Chest.orangeChest: 16000
}
monsterLife = {
    Monster.Rat: 5,
    Monster.Bat: 10,
    Monster.GiantSpider: 15,
    Monster.Wolf: 30
}
monsterDamage = {
    Monster.Rat: 3,
    Monster.Bat: 5,
    Monster.GiantSpider: 8,
    Monster.Wolf: 12
}

gameLength = 10

Gold = 0

while gameLenght > 0:

    gameAnswer = input("Do you want to move forward? \n")

    if gameAnswer == "yes":
        print("Great, lets see what is inside")
        drawnEvent = random.choices(eventList, eventProbability)[0]

        if drawnEvent == Event.Chest:
            drawnChest = random.choices(chestList, chestProbability)[0]
            goldAcquire = find_aprox_Value(colorValue[drawnChest])
            print("You have find ", drawnChest.value, "inside was", goldAcquaire, "gold")
            Gold = Gold + goldAcquaire

        elif drawnEvent == Event.Monster:
            drawnMonster = random.choices(MonsterList, MonsterProbability)[0]
            print("Oh no, you have find", drawnMonster.value, "which has", monsterLife[drawnMonster],
                  "life .If you will defeat him, you will find great treasure.")
            eventAnswer = input(" What is your choice?(fight, run)")
            if eventAnswer == "fight":
                while monsterLife[drawnMonster] > 0:
                    if_hit(10)
                    if monsterLife[drawnMonster] > 0:
                        monster_hit()
                drawnPremiumChest = random.choices(PremiumChestList, PremiumChestProbability)[0]
                goldAcquire = find_aprox_value(colorValue[drawnPremiumChest])
                print("Congratulations, you have defeat a monster, and you found", drawnPremiumChest.value,
                      ", inside was", goldAcquaire, " gold")
                Gold = Gold + goldAcquaire
            elif eventAnswer == "run":
                gameLength = gameLength - 1
                print("you have successfully run")
            else:
                print("Only options is run or fight")

                continue

    else:
        print("Your only options is move forward")
        continue
gameLength = gameLength - 1

print("Congratulations you have acquired", Gold, "gold")
