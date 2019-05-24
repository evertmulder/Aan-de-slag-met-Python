import json
with open('kennis.json', 'r') as fp:
    kennis = json.load(fp)

def stel_vraag(node):
    answer = input(node["vraag"].capitalize() + "? ").lower()[:1]
    if answer in ["y","j"]:
        next_key = "ja"
    else:
        next_key = "nee"
    
    if type(node[next_key]) is str :
        current_dier = node[next_key]
        answer2= input("Is het een {}? ".format(current_dier)).lower()[:1]
        if answer2 in ["y","j"]:
            print("Ik wist het wel!")
            return True
        elif answer2 == "n":
            dier = input("Welk dier is het dan wel? ")
            vraag = input("Welke vraag had ik moeten stellen? ")
            new_node  = {
                "nee": current_dier,
                "ja": dier.lower(),
                "vraag": vraag.lower().rstrip("?").strip()
            }
            node[next_key] = new_node
            return True
        else:
            print("Invalid input (y/n)")
    else:
        return stel_vraag(node[next_key])

geraden = False
while not geraden:
    geraden = stel_vraag(kennis)

with open('kennis.json', 'w') as fp:
    json.dump(kennis, fp)