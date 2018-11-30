# Waar is de kat geweest simulatie

from random import randint, choice

# Initialisatie
aantal_dozen = 5
doos_met_kat = randint(1, aantal_dozen)
ronde_nummer = 0
kat_gevonden = False

# Start van de simulatie
while not kat_gevonden:
  doos_te_openen = randint(1, aantal_dozen)
  ronde_nummer += 1
  if doos_te_openen == doos_met_kat:
      kat_gevonden = True
      print("Je hebt de kat gevonden in", ronde_nummer, "beurten")
  else:
      print("De kat zat niet in die doos")

def verplaats_kat():
  if doos_met_kat == 1:
	  doos_met_kat = 2
  elif doos_met_kat == aantal_dozen:
      doos_met_kat = aantal_dozen - 1
  else:
      doos_met_kat = doos_met_kat + choice([-1, 1])
