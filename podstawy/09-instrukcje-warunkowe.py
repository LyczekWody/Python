light = input("Jakie jest światło? (red, green, yellow) ")

# if str(light).startswith("r") or light == "red":
#     print("czekaj!")
# elif light == 'yellow':
#     print("przygotuj się!")
# elif light == 'green':
#     print("jedź!")
# else:
#     print("Niewłaściwa wartość")

print("Jedź") if light == "green" else print("czekaj")