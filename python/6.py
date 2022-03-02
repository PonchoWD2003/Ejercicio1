amigos = [["Susana", 18],
            ["Ruben", 19],
            ["Clara", 20],
            ["Jorge", 25]]

amigos [1][1] = 22

print(amigos[1][1])
print(amigos)

amigos.append(["Shara"])
amigos[4].append(22)
print(amigos)




for amigo in amigos:
    print("{:10}: {:2}".format(amigo[0], amigo[1]))