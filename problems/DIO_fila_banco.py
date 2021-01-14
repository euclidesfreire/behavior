import sys

entrada = sys.stdin.readline()

entrada = [int(x) for x in entrada.split(" ")]

lenString = 0
a = 0

for c in range(entrada[0]):
    clientes = []
    clientes_new = []

    a += 1 + lenString
    b = a + entrada[a]        

    lenString = entrada[a]

    for x in range(a+1,b+1):
        clientes.append(entrada[x])

    clientes_new = clientes.copy()
    clientes_new.sort(reverse=True)
    print(clientes)
    print(clientes_new)

    naoTrocar = 0

    for i in range(len(clientes)):
        if clientes[i] == clientes_new[i]:
            naoTrocar +=1

    print(naoTrocar)