#Lista initiala
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

#Sortare lista ascendent
list_asc = sorted(my_list)

print(f'Lista ascendenta este: {list_asc}')

#Sortare lista descendent

my_list.sort(reverse=True)

print(f'Lista descendenta este: {my_list}')

#Afisarea numerelor pare din lista initiala

nr_pare = list_asc[1], list_asc[3], list_asc[5], list_asc[7], list_asc[9]

print(f'Numerele pare din lista ordonata sunt: {nr_pare}')

#Afisarea numerelor impare din lista initiala

nr_impare = list_asc[0], list_asc[2], list_asc[4], list_asc[6], list_asc[8]

print(f'Numerele impare din lista ordonata sunt: {nr_impare}')

#Afisarea multiplilor lui 3 din lista initiala

mult_3 = list_asc[2], list_asc[5], list_asc[8]

print(f'Multiplii lui 3 lista ordonata sunt: {mult_3}')