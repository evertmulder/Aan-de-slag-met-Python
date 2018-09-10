doorgaan = True
while doorgaan:
  dier = input("Voer een dier in, of geef <enter> om af te sluiten: ")
  if len(dier) == 0:
    doorgaan = False
    print("Ok, tot ziens")
    break
  print("Uw invoer is", len(dier), "lang")
