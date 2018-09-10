jongensnamen = set(('koos','jaap','francis','sam','robin','pieter'))
meisjesnamen = {'saartje','nora','amber','sam','petra','robin'}

print(jongensnamen.union(meisjesnamen))
print(jongensnamen.difference(meisjesnamen))
print(meisjesnamen.difference(jongensnamen))
print(meisjesnamen.intersection(jongensnamen))

jongensnamen.add('anne')

meisjesnamen.clear()
