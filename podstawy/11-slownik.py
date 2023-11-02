counties_and_capitols = {"Poland":"Warsaw", "Germany":"Berlin"}

counties_and_capitols['Czechia'] = "Prague"

# print(counties_and_capitols)

# jako funkcje mozemy dac np: key(panstwa),values(stolice),(items do wszystko)
# for country, capitol in counties_and_capitols.items():
    # print(country + "-" + capital)

# jesli nie ma rekordu error
# print(counties_and_capitols["Poland"])
# #przy get jesli rekordu nie bedzie to wynik = none 
# print(counties_and_capitols.get("Poland"))

# print(counties_and_capitols.setdefault("USA", "Washington"))
# print(counties_and_capitols)

# usuniecie klucza poland z słownika
# counties_and_capitols.pop("Poland")
# print(counties_and_capitols)

# popitem usuwa ostatni dodany rekord do słownika
# counties_and_capitols.popitem()
# print(counties_and_capitols)

# sprawdzanie czy klucz istnieje w słowniku
# print(counties_and_capitols)

if "Poland" in counties_and_capitols:
    print("Znaleziono")
else:
    print("Nie ma w słowniku")

# wyczyszczenie słownika
# print(counties_and_capitols.clear())
