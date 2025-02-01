#program that simulates death saves
#find probability one dies, stabilizes, or revives

import random
success = 0
failure = 0

die = 0
stable = 0
revive = 0

total_turn = 100000
for turn in range(total_turn):
    turn += 1
    throw = random.randint(1, 20)
    if throw == 1: failure += 2
    elif 1< throw < 10: failure += 1
    elif 10 <= throw < 20: success += 1
    elif throw == 20: #revive
        revive += 1
        failure = 0
        success = 0
    if failure >= 3: #die
        die += 1
        failure = 0
        success = 0
    elif success >=3: #stable
        stable += 1
        failure = 0
        success = 0
print(die/total_turn, stable/total_turn, revive/total_turn)

#better and more correct version, with help of chatGPT
def simulation():
    failure = 0
    success = 0
    while True:
        throw = random.randint(1, 20)
        if throw == 1:
            failure += 2
        elif 1 < throw < 10:
            failure += 1
        elif 10 <= throw < 20:
            success += 1
        elif throw == 20:
            return 'revive'

        if failure >= 3:
            return 'die'
        elif success >= 3:
            return 'stable'

def deathsave_result(total_turn):
    revive = 0
    die = 0
    success = 0

    for turn in range(total_turn):
        result = simulation()
        if result == 'revive': revive += 1
        elif result == 'die': die += 1
        elif result == 'stable': success += 1

    return revive/total_turn, die/total_turn, success/total_turn
print(deathsave_result(10000))





