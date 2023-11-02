file = open("countries_and_capitols.txt","w+")

countries_and_capitols = {'Poland': 'Warsaw', 'Czechia': 'Praga',
                           'Germany':'Berlin'}

for country, capital in countries_and_capitols.items():
    file.write(country + "-" + capital + "\n")

file.close()

###

file = open("countries_and_capitols.txt")

for line in file.readlines():
    print(line.strip())

file.close()
