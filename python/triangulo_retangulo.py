class triangulo:

    def __main__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def retangulo(self):
        lista = [self.a, self.b, self.c]
        hipotenusa = max(lista)
        
        if self.a == hipotenusa:
            if self.a*self.a == (self.b * self.b) + (self.c * self.c):
                return true
            else:
                return false

        if self.b == hipotenusa:
            if self.b*self.b == (self.a * self.a) + (self.c * self.c):
                return true
            else:
                return false
        
        if self.c == hipotenusa:
            if self.c*self.c == (self.a * self.a) + (self.b * self.b):
                return true
            else:
                return false
                    
