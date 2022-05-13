class Triangulo:

    def __main__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        perimetro = self.a + self.b + self.c
        return perimetro

    def tipo_lado(self):
        x = self.a + self.b + self.c
        y = x/3
        if y == self.a:
            return "equilátero"
        else:

                if self.a == self.b or self.a == self.c or self.b == self.c:
                    return "isóceles"

                else:
                    return "escaleno"
    
    
