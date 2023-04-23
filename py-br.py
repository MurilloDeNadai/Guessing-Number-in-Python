import random, time, os

#set variables
minimum = maximum = cont = lose = win = 0
random_number = 0

#select difficulty
print('Selecione a Dificuldade:')
print(f'''
    [ 1 ] - Muito Fácil;
    [ 2 ] - Fácil;
    [ 3 ] - Médio;
    [ 4 ] - Difícil;
    [ 5 ] - Hardcore;
''')

#prevent wrong number
while True:
    difficulty = int(input("Selecione: "))
    if difficulty > 5 or difficulty < 1:
        print("Opção inválida, tente novamente!")
    else:
        break

print("Aguarde...")
time.sleep(2)

#difficulty message and add a maximum number for limeted the random
if difficulty == 1:
    print(f"Você selecionou a dificuldade Muito Fácil!")
    maximum = 10
elif difficulty == 2:
    print(f"Você selecionou a dificuldade Fácil!")
    maximum = 15
elif difficulty == 3:
    print(f"Você selecionou a dificuldade Médio!")
    maximum = 20
elif difficulty == 4:
    print(f"Você selecionou a dificuldade Difícil!")
    maximum = 50
elif difficulty == 5:
    print(f"Você selecionou a dificuldade Hardcore!")
    maximum = 100
else:
    print("ERROR")

time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')

#hardcore mode

if difficulty == 5:
    print(f"No modo Hardicore, alguns números vem junto de uma dica. Boa Sorte!")
    while True:
        ready = input(f"Preparado ?! [S/N]: ").upper().strip()[0]

        if ready not in 'SN':
            print("Valor inválido!!! Tente novamente!!!")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            break

    if ready in 'S':
        
        while True:
            cont += 1
            random_number = random.randint(minimum, maximum)
            print(f"Para sair digite 999")

            if cont == 1:
                print(f"Primeiro número gerado!")
            else:
                print(f"Próximo número gerado!")

            if random_number == 10:
                work_list = ["Eu tenho um relógio chamado omnitrix, e meu primeiro nome é BEN:", "(25 * 5 - 25) / 10", "1000 / 100", "1.000.000 / 10^5"]
                print(work_list[random.randint(0, len(work_list))])
            elif random_number == 33:
                work_list = ["Idade de Jesus", "3.3.3.3.3.3...", "30,31,32,....,34,35,36"]
                print(work_list[random.randint(0, len(work_list))])
            elif random_number == 50:
                work_list = ["100 / 2", "500 / 100", "0,5 x 100"]
                print(work_list[random.randint(0, len(work_list))])
            elif random_number == 75:
                work_list = ["3/4 de 100", "25 + 25 + 25", "100 - 25 + 25 + 0", "0.75 sem o 0!"]
                print(work_list[random.randint(0, len(work_list))])
            elif random_number == 88:
                work_list = ["8.8.8.8.8.8", "100 - 12", "22 x 4"]
                print(work_list[random.randint(0, len(work_list))])
            elif random_number == 22:
                work_list = ["Dois patos na lagoa!!!", "Dois patos atravessando a rua!!!", "Somente dois patos!"]
                print(work_list[random.randint(0, len(work_list))])
            elif random_number == 1:
                work_list = ["Primeiro número!", "Menor que 2 porém maior que 0", "Amanhã é 2, então hoje é....", "4.235.221,12^0"]
                print(work_list[random.randint(0, len(work_list))])
                
            guess_number = int(input(f"Acerte o número[0 - {maximum}]: "))

            if guess_number == 999 and cont == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Tchau! Até logo!!!")
                break
            elif guess_number == 999 and cont != 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Tchau! Até logo!!!")
                print(f"Vitórias: {win} / Derrotas: {lose}")
                break

            if guess_number == random_number:
                print(f"WOOOWWW!!! Acertou o número que eu estava pensando, parabéns!!!")
                win += 1
                time.sleep(3)
            else:
                print(f"Puts!!! Você perdeu! Eu estava pensando no número: {random_number}")
                lose += 1
                time.sleep(2)
            
        
            os.system('cls' if os.name == 'nt' else 'clear')

    else:
        print("Seu perdedor, você ficou com medo!")

#very easy, easy, medium and hard mode

else:
    while True:
        cont += 1
        random_number = random.randint(minimum, maximum)
        print(f"Para sair digite 999")

        if cont == 1:
            print(f"Primeiro número gerado!")
        else:
            print(f"Próximo número gerado!")
            
        guess_number = int(input(f"Acerte o número[0 - {maximum}]: "))

        if guess_number == 999 and cont == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Tchau! Até logo!!!")
            break
        elif guess_number == 999 and cont != 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Tchau! Até logo!!!")
            print(f"Vitórias: {win} / Derrotas: {lose}")
            break

        if guess_number == random_number:
            print(f"WOOOWWW!!! Acertou o número que eu estava pensando, parabéns!!!")
            win += 1
            time.sleep(3)
        else:
            print(f"Puts!!! Você perdeu! Eu estava pensando no número: {random_number}")
            lose += 1
            time.sleep(2)
        
    
        os.system('cls' if os.name == 'nt' else 'clear')