# Waar is de kat geweest simulatie

from random import randint, choice

# Initialisatie
aantal_dozen = 5
doos_met_kat = randint(1, aantal_dozen)
aantal_pogingen = 0
kat_gevonden = False

# Start van de simulatie
while not kat_gevonden:
  doos_te_openen = randint(1, aantal_dozen)
  aantal_pogingen += 1
  if doos_te_openen == doos_met_kat:
      kat_gevonden = True
      print("Je hebt de kat gevonden in doos", doos_te_openen, "in", aantal_pogingen, "beurten")
  else:
      print("De kat zat niet in doos", doos_te_openen)
      if doos_met_kat == 1:
          doos_met_kat = 2
      elif doos_met_kat == aantal_dozen:
          doos_met_kat = aantal_dozen - 1
      else:
          doos_met_kat = doos_met_kat + choice([-1, 1])
