for i in range(int(input())):
    x = input()
    if x == 'b' or x == 'B':
        print("BattleShip")
    elif x == 'c' or x == 'C':
        print("Cruiser")
    elif x == 'd' or x == 'D':
        print("Destroyer")
    else:
        print("Frigate")