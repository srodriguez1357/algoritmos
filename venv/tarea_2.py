L1 = eval(input("Ingrese el largo del primer lado: "))
L2 = eval(input("Ingrese el largo del segundo lado: "))
L3 = eval(input("Ingrese el largo del tercer lado: "))
if L1+L2>L3 and L1+L3>L2:
	if L2+L3>L1:
		p = L1+L2+L3
		print(("El perímetro es de",p,"cm."))
	else:
		print(("Triángulo no válido"))
else:
	print(("Triángulo no válido"))



