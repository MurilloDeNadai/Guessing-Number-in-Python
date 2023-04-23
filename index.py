import random, time, os


def color(c):
    if c == 'gray':
        return '\033[30m'
    elif c == 'red':
        return '\033[31m'
    elif c == 'green':
        return '\033[32m'
    elif c == 'yellow':
        return '\033[33m'
    elif c == 'blue':
        return '\033[34m'
    elif c == 'pink':
        return '\033[35m'
    elif c == 'purple':
        return '\033[35m'
    else:
        return '####Erro####'
    
    
def exit_color():
    return '\033[m'

#set variables
minimum = maximum = cont = lose = win = 0
random_number = 0

#select difficulty
print('Select a difficulty:')
print(f'''
    [ 1 ] - {color('blue')}Very Easy{exit_color()};
    [ 2 ] - {color('green')}Easy{exit_color()};
    [ 3 ] - {color('yellow')}Medium{exit_color()};
    [ 4 ] - {color('red')}Hard{exit_color()};
    [ 5 ] - {color('gray')}Hardcore{exit_color()};
''')

#prevent wrong number
while True:
    difficulty = int(input("Select: "))
    if difficulty > 5 or difficulty < 1:
        print("The number entered is invalid! Try again!")
    else:
        break

print("waiting...")
time.sleep(2)

#difficulty message and add a maximum number for limeted the random
if difficulty == 1:
    print(f"You selected the difficulty {color('blue')}Very Easy{exit_color()}!")
    maximum = 10
elif difficulty == 2:
    print(f"You selected the difficulty {color('green')}Easy{exit_color()}!")
    maximum = 15
elif difficulty == 3:
    print(f"You selected the difficulty {color('yellow')}Medium{exit_color()}!")
    maximum = 20
elif difficulty == 4:
    print(f"You selected the difficulty {color('red')}Hard{exit_color()}!")
    maximum = 50
elif difficulty == 5:
    print(f"You selected the difficulty {color('gray')}Hardcore{exit_color()}!")
    maximum = 100
else:
    print("ERROR")

time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')

#hardcore mode

if difficulty == 5:
    print(f"{color('gray')}In Hardcore mode, some specific numbers have hints. Good luck!{exit_color()}")
    while True:
        ready = input(f"You ready ?! {color('gray')}[Y/N]{exit_color()}: ").upper().strip()[0]

        if ready not in 'YN':
            print("Value invalid!!! Try Again!!!")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            break

    if ready in 'Y':
        
        while True:
            cont += 1
            random_number = random.randint(minimum, maximum)
            print(f"{color('gray')}For exit the game type it the number 999{exit_color()}")

            if cont == 1:
                print(f"First number {color('pink')}generated{exit_color()}!")
            else:
                print(f"Next number {color('pink')}generated{exit_color()}!")

            if random_number == 10:
                work_list = ["I have a watch called omnitrix, and my first name is BEN:", "(25 * 5 - 25) / 10", "1000 / 100", "1.000.000 / 10^5"]
                print(work_list[random.randint(0, len(work_list))])
            elif random_number == 33:
                work_list = ["Age of Jesus", "3.3.3.3.3.3...", "30,31,32,....,34,35,36"]
                print(work_list[random.randint(0, len(work_list))])
            elif random_number == 50:
                work_list = ["100 / 2", "500 / 100", "0,5 x 100"]
                print(work_list[random.randint(0, len(work_list))])
            elif random_number == 75:
                work_list = ["3/4 of 100", "25 + 25 + 25", "100 - 25 + 25 + 0", "0.75 without the zero!"]
                print(work_list[random.randint(0, len(work_list))])
            elif random_number == 88:
                work_list = ["8.8.8.8.8.8", "100 - 12", "22 x 4"]
                print(work_list[random.randint(0, len(work_list))])
            elif random_number == 22:
                work_list = ["Two ducks in lake!!!", "Two dukes crossing the street", "Something Two Ducks"]
                print(work_list[random.randint(0, len(work_list))])
            elif random_number == 1:
                work_list = ["First Number!", "less than 2 and greater than 0", "Tomorrow is 2, Yesterday is...", "4.235.221,12^0"]
                print(work_list[random.randint(0, len(work_list))])
                
            guess_number = int(input(f"Guessing the number{color('gray')}[0 - {maximum}]{exit_color()}: "))

            if guess_number == 999 and cont == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Bye!!! See next time!!!")
                break
            elif guess_number == 999 and cont != 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Bye!!! See next time!!!")
                print(f"{color('yellow')}Win{exit_color()}: {win} / {color('yellow')}Lose{exit_color()}: {lose}")
                break

            if guess_number == random_number:
                print(f"WOOOWWW!!! You hit the number I was thinking of, {color('yellow')}congratulations{exit_color()}!!!")
                win += 1
                time.sleep(3)
            else:
                print(f"Puts!!! You {color('red')}missed{exit_color()}! I was thinking of the number: {random_number}")
                lose += 1
                time.sleep(2)
            
        
            os.system('cls' if os.name == 'nt' else 'clear')

    else:
        print("You loser, you got scared, right!")

#very easy, easy, medium and hard mode

else:
    while True:
        cont += 1
        random_number = random.randint(minimum, maximum)
        print(f"{color('gray')}For exit the game type it the number 999{exit_color()}")

        if cont == 1:
            print(f"First number {color('pink')}generated{exit_color()}!")
        else:
            print(f"Next number {color('pink')}generated{exit_color()}!")
            
        guess_number = int(input(f"Guessing the number{color('gray')}[0 - {maximum}]{exit_color()}: "))

        if guess_number == 999 and cont == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Bye!!! See next time!!!")
            break
        elif guess_number == 999 and cont != 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Bye!!! See next time!!!")
            print(f"{color('yellow')}Win{exit_color()}: {win} / {color('yellow')}Lose{exit_color()}: {lose}")
            break

        if guess_number == random_number:
            print(f"WOOOWWW!!! You hit the number I was thinking of, {color('yellow')}congratulations{exit_color()}!!!")
            win += 1
            time.sleep(3)
        else:
            print(f"Puts!!! You {color('red')}missed{exit_color()}! I was thinking of the number: {random_number}")
            lose += 1
            time.sleep(2)
        
    
        os.system('cls' if os.name == 'nt' else 'clear')