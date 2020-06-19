import random
from time import sleep

with open('nomes_m') as names:
    names_m = names.readlines()
with open('nomes_f') as names:
    names_f = names.readlines()
with open('xingamentos_m') as xings:
    xingamentos_m = xings.readlines()
with open('xingamentos_f') as xingamentos:
    xingamentos_f = xingamentos.readlines()
with open('conjuncoes') as conjs:
    conjucoes = conjs.readlines()

def create_xing(xing_list):
    xingamentos = []
    xingaux = xing_list[:]
    for x in range(random.randrange(1, len(xing_list))):
        random.shuffle(xingaux)
        xingamentos.append(xingaux.pop())
    return xingamentos

def xingar():
    conjucao = random.choice(conjucoes)
    if random.randint(0, 1) == 0:
        name = random.choice(names_m)
        xingamentos = create_xing(xingamentos_m)

    else:
        name = random.choice(names_f)
        xingamentos = create_xing(xingamentos_f)

    return name.strip() + ' ' + conjucao.strip() + ' ' + ' '.join([x.strip() for x in xingamentos])

if __name__ == "__main__":
    while True:
        print(xingar())
        sleep(10)

