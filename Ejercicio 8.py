def superposicion(list_a, list_b):
	aux_list = []
	for item in list_a:
		for item_b in list_b:
			if item == item_b:
				aux_list.append(item)
	if len(aux_list) > 0:
		return True
	else:
		return False
