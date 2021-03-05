def skip_elements(elements):
	# code goes here
    #inicializa nova lista
    new_list = []
    #Loop enumerate pra percorrer a lista
    for index, element in enumerate(elements):
    #Checa se o indice é par    
        if index % 2 == 0:
    #Cria nova lista com itens de indice par         
            new_list.append(elements[index])
    return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))