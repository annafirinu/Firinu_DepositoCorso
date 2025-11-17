matrice = [
[1, 2, 3], # prima riga
[4, 5, 6], # seconda riga
[7, 8, 9] # terza riga
]

elemento = matrice[0][1]
# Accesso all'elemento nella prima riga e seconda colonna
print(elemento) # Output: 2

for riga in matrice:
  for elemento in riga:
    print(elemento)
    
