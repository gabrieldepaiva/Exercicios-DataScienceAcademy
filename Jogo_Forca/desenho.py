a ='|-----|\n' \
'|       \n' \
'|         \n' \
'|        \n' \
'|\n' \
'==============='


b ='|-----|\n' \
'|     O \n' \
'|         \n' \
'|        \n' \
'|\n' \
'==============='


c ='|-----|\n' \
'|     O \n' \
'|     |   \n' \
'|        \n' \
'|\n' \
'==============='


d ='|-----|\n' \
'|     O \n' \
'|   / |   \n' \
'|        \n' \
'|\n' \
'==============='


e ='|-----|\n' \
'|     O \n' \
'|   / | \ \n' \
'|        \n' \
'|\n' \
'==============='


f ='|-----|\n' \
'|     O \n' \
'|   / | \ \n' \
'|    /   \n' \
'|\n' \
'==============='


g ='|-----|\n' \
'|     O \n' \
'|   / T \ \n' \
'|    / \ \n' \
'|\n' \
'==============='

letras = [a, b, c, d, e, f, g]

# Dependendo da tentativa ele exibe uma etapa a mais do boneco desenhado
def tentativa (n=1):
    print(letras[n])

# Sorteio da palavra
def sorteio():

    lista = []
    f = open('palavras.txt', 'r+')
    lista.append(f.read().split('\n'))

    import random
    a = lista[0][random.randint(0,4)]
    return a





