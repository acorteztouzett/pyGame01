import random

player= input("Escribe tu nombre de usuario: ").upper()

game=["Piedra", "Papel", "Tijera"]

computer=c=0
command=p=0

print(f"Score: PC->", c, player,"-->",p)

run=True
while run:
    pc_pick= random.choice(game)
    command = input("Piedra, Papel, Tijera o Quit: ").capitalize()
    if command == pc_pick:
        print("EMPATE")

    elif command=="Piedra":
        if pc_pick == "Tijera":
            print(player,"ganó")
            p+=1
        else:
            print("La PC ganó")
            c+=1
    elif command=="Papel":
        if pc_pick== "Piedra":
            print(player, "ganó")
            p+=1
        else:
            print("La PC ganó")
            c+=1
    elif command=="Tijera":
        if pc_pick=="Papel":
            print(player,"ganó")
            p+=1
        else:
            print("La PC ganó")
            c+=1
    elif command=="Quit":
        break
    else:
        print("COMANDO EQUIVOCADO")

    print(player,":",command)
    print("PC:", pc_pick)
    print("")
    print("Score: PC->", c, player,"-->",p)
    print("")
