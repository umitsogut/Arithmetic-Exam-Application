# write your code here
import random

def save_result(score,game):
    if game == 1:
        gameDesc = 'simple operations with numbers 2-9'
    elif game == 2:
        gameDesc = 'integral squares of 11-29'
    print(f'Your mark is {score}/5. Would you like to save the result? Enter yes or no.')
    userSave = input()
    if userSave in ('yes','y','Yes','YES'):
        print('What is your name?')
        name = input()
        with open("results.txt","a") as file:
            file.write(f'{name}: {score}/5 in level {game} ({gameDesc}).\n')
        print('The results are saved in "results.txt".')

score = 0
while True:
    print('''
    Which level do you want? Enter a number:
    1 - simple operations with numbers 2-9
    2 - integral squares of 11-29
    ''')

    try:
        choice = int(input())
        if choice in (1,2): break
    except ValueError:
        pass
    print('Incorrect format.')

if choice == 1:
    for _ in range(5):
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        operations = ('+','-','*')
        selectOperation = random.choice(operations)
        print(a,selectOperation,b)

        result = 0
        if selectOperation == '+':
            result = a + b
        elif selectOperation == '-':
            result = a - b
        elif selectOperation == '*':
            result = a * b

        userResult = 0
        while True:
            try:
                userResult = int(input())
                if userResult == result:
                    print('Right!')
                    score += 1
                else:
                    print('Wrong!')
                break
            except ValueError:
                print('Incorrect format.')

    save_result(score,1)

if choice == 2:
    for _ in range(5):
        a = random.randint(11,29)
        print(a)
        result = a*a
        userResult = 0
        while True:
            try:
                userResult = int(input())
                if userResult == result:
                    print('Right!')
                    score += 1
                else:
                    print('Wrong!')
                break
            except ValueError:
                print('Incorrect format.')

    save_result(score,2)

