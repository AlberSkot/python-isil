class triangulo:
	def __init__(self, p2x, p1x, p2y, p1y):
		self.p2x = p2x
		self.p1x = p1x
		self.p2y = p2y
		self.p1y = p1y
	def perimetro(self):
		return self.p2x+self.p1x+self.p2y+self.p1y
obj = triangulo(10,0,0,0)
print ('La suma de la distancia entre los puntos es: ',obj.perimetro())