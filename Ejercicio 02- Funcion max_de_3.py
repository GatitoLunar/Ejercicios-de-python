#Definir una función max_de_tres(), que tome tres números
#como argumentos y devuelva el mayor de ellos.

def max_de_tres(value_a, value_b, value_c):
	aux_a = max(value_a,value_b)
	aux_b = max(aux_a, value_c)
	return aux_b
