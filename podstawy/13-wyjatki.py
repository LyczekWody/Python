countries_and_capitols = {'Poland': 'Warsaw', 'Czechia': 'Praga',
                           'Germany':'Berlin'}

try:    
    # print(countries_and_capitols['USA'])
    print(2/0)
# except KeyError:
#     print("Klucz nie został znaleziony")
except ZeroDivisionError:
    print("Dzilisz przez 0 nie nie nie")
finally:
    print("To wykona sie zawsze!")

print("Jestem tutaj")