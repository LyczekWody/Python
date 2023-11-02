# number = 1

# while number < 6:
#     print(number)
#     number += 1

# break - przerywa wykonanie petli
# continue - nie wywołuje określonej petli ale nie stopuje reszty

for number in range(0, 20, 2):
    if(number == 6):
        break
    print(number)