a,b,c = map(float,input().split(" "))

triangulo = (a*c)/2
circulo = 3.14159*c**2
trapezio = ((a+b)*c)/2
quadrado = b**2
retangulo = a*b

print(str("TRIANGULO: ")+str("{:.3f}".format(triangulo)))
print(str("CIRCULO: ")+str("{:.3f}".format(circulo)))
print(str("TRAPEZIO: ")+str("{:.3f}".format(trapezio)))
print(str("QUADRADO: ")+str("{:.3f}".format(quadrado)))
print(str("RETANGULO: ")+str("{:.3f}".format(retangulo)))