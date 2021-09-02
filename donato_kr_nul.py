kvadratas = [7, 8, 9, 4, 5, 6, 1, 2, 3]
zaidejas = "X"

def atspausdinti_kvadrata():
    eile = 0
    for simbolis in kvadratas:
        print(str(simbolis) + "|", end="")
        eile += 1
        if eile == 3:
            print()
            eile = 0

laimejimai = [["+", "-", "-", "+", "-", "-", "+", "-", "-"], 
              ["-", "+", "-", "-", "+", "-", "-", "+", "-"], 
              ["-", "-", "+", "-", "-", "+", "-", "-", "+"], 
              ["+", "+", "+", "-", "-", "-", "-", "-", "-"], 
              ["-", "-", "-", "+", "+", "+", "-", "-", "-"], 
              ["-", "-", "-", "-", "-", "-", "+", "+", "+"], 
              ["+", "-", "-", "-", "+", "-", "-", "-", "+"], 
              ["-", "-", "+", "-", "+", "-", "+", "-", "-"]]

def tikrinti_laimejima():
    pakeistas = kvadratas.copy()
    for counter, x in enumerate(pakeistas):
        if x == zaidejas:
            pakeistas[counter] = "+"
        else:
            pakeistas[counter] = "-"
    return pakeistas in laimejimai

atspausdinti_kvadrata()

while True:
    print()
    pasirinkimas = int(input(f"Žaidėjas {zaidejas}: pasirinkite veiksmą"))
    if pasirinkimas in kvadratas:
        kvadratas[kvadratas.index(pasirinkimas)] = zaidejas
        atspausdinti_kvadrata()
        if tikrinti_laimejima():
            print(f"Žaidėjas {zaidejas} laimėjo!")
            break
        if zaidejas == "X":
            zaidejas = "O"
        else:
            zaidejas = "X"
    else:
        print("Nėra tokio pasirinkimo, bandykite dar kartą")