import desenho
palavra = desenho.sorteio()
cont = 0
g = 0
lcorreta = []
lerrada = []
p = ('_'*len(palavra))

while cont < 6 and '_' in p:
    #Impressão das boas vindas do jogo
    print(f'{"=" * 10} Jogo da Forca {"=" * 10}')
    desenho.tentativa(cont)
    print(p)

    # Listagem de letras que foram tentadas
    if len(lcorreta) > 0:
        print('Letras corretas - ',end='')
        for t in lcorreta:
            print(t, end=' ')
        print()

    if len(lerrada) > 0:
        print('Letras erradas - ', end='')
        for t in lerrada:
            print(t, end=' ')
        print()

    #Tentativa e validação do dado digitado
    l = (input('Letra - ')).strip().lower()[0]
    while True:
        if l in lcorreta or l in lerrada:
            l = (input('Você já digitou essa. Digite outra - ')).strip().lower()[0]
            continue
        else:
            break

    #Colocar a letra na lista a que pertence, se for na certa colocar na lcorreta, se for errada colocar na lerrada

    if l in palavra:
        g += 1
        lcorreta.append(l)

    else:
        cont += 1
        lerrada.append(l)

    #Substitui o espaço em branco por uma letra ou mantem o espaço em branco
    p = ''

    for letra in palavra:
        if letra in lcorreta:
            p += letra
        else:
            p += '_'

    continue

#Finalização do jogo com a mensagem de vitória ou derrota.
if cont == 6:
    desenho.tentativa(6)
    print('Letras corretas - ', end='')
    for t in lcorreta:
        print(t, end=' ')
    print()
    print('Letras erradas - ', end='')
    for t in lerrada:
        print(t, end=' ')
    print()
    print(f'Você Perdeu! A palavra era {palavra}.')

else:
    desenho.tentativa(cont)
    print('Letras corretas - ', end='')
    for t in lcorreta:
        print(t, end=' ')
    print()
    print('Letras erradas - ', end='')
    for t in lerrada:
        print(t, end=' ')
    print()
    print(palavra)
    print('Você ganhou! Meus Parabéns')
