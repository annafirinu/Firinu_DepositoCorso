class Punto: #Creo una classe chiamata punto
    def __init__(self, x, y):#Attributi x e y
        self.x = x
        self.y = y
    #Metodo muovi con dx e dy
    def muovi(self, dx, dy):
        self.x += dx
        self.y += dy
    #Metodo che calcola la distanza dall'origine
    def distanza_da_origine(self):
        return (self.x**2 + self.y**2) ** 0.5

    def __str__(self): #Stampo le coordinate del punto
        return f"Punto({self.x}, {self.y})"


#Utilizzo la classe
p = Punto(3, 4)
print(p) 
p.muovi(1, -2)
print(p) 
print("Distanza dall'origine:", p.distanza_da_origine())
