def es_palindromo(cadena):
	cadena_aux = cadena.lower()
	cadena_inversa = cadena_aux[::-1]
	return_value = True
	for i in range(len(cadena)):
		if cadena_aux[i] == cadena_inversa[i]:
			continue
		else:
			return_value = False
			break
	return return_value

