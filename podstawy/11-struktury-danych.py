# names_list = []
# names_list.append("Kamil")
# names_list.append("Mariusz")

names_list = ["Kamil", "Mariusz", "Grzesiek", "Kamil"]

# names_list.reverse()
# names_list.sort()

# okreslony element z listy
# print(names_list[0])

# for name in names_list:
#     print(name)

# print(names_list.count("Kamil"))

# długosc list - len
# print(len(names_list))


# # usuwa z listy i zwraca ten element
# print(names_list)
# print()
# print(names_list.pop(2))
# print()
# print(names_list)

lista1_list = ["Jan", "Andrzej", "Marek", "Wojciech"]

# # # lista1_list.remove("Jan")
# # # lista1_list.clear()

lista3_list = names_list + lista1_list 
# lista3_list.sort(reverse=True)
# print(lista3_list)

# Krotka

krotka1 = ("Kamil", "Mariusz", "Grzesiek", "Kamil")
# print(krotka1)

person = ("Grzesiek", "Szuper", 21, "Wrocław")

# print(len(person))
# print(person.count("Grzesiek"))

# imiona_set = {"Kamil", "Mariusz", "Grzesiek", "Kamil"}
# pusty_set = set()
# pusty_set.add("Grzesiek")

# jesli nie ma elementu w liscie a uzyjemy remove to bedzie bład za to 
# przy discard po prostu nic sie nie stanie 

# imiona_set.remove("Mariusz")
# imiona_set.discard("Grzesiek")

# print(imiona_set)
# print(pusty_set)

# for name in imiona_set:
#     print(imiona_set)

auta_set = {"Audi", "Bmw", "Porsche"}
auta2_set = {"Kombi"}

auta3_set = auta_set.union(auta2_set)

# for name in auta3_set:
#     print(name)

liczby_set = {1,2,3,4,5}
liczby2_set = {4,5,6,7,8}

liczby2_set.add(10)
liczby2_set.add(11)

# rozne_set = liczby_set.difference(liczby2_set)  
rozne1_set = liczby_set.intersection(liczby2_set) #czesci wspolne
# poza wspolnymi liczbami
rozne2_set = liczby_set.symmetric_difference(liczby2_set)
print (rozne2_set)

