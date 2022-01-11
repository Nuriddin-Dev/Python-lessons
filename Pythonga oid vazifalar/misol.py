i = 1
bush_list = []
while i<6:
    son = int(input(f"{i} sonni kiriting: "))
    bush_list.append(son)
    i = i + 1

bush_list.sort()

print('Eng katta son ',bush_list[-1])

