file = open('.notas.txt', 'r')
for line in file:
    content = line.replace('\n', '').split(',')
    nome = content[0]
    total = 0
    for nota in content[1:]:
        total += float(nota)
    media = total/(len(content) - 1)

