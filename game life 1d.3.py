print("Приветствую, вас в игре 'жизнь'")
print("Для создания мира пожалуйста ответься на последующие вопросы или сразу напишите рандом")
print("при выбор еокманды рамдом вам будет предоставлен мир с случайными настройками")
print("введите размер мира, тоесть его длину")
dlina = input()
while dlina.isdigit() == False:
    print("введите число")
    dlina = input()
print("введите количество живых клеток меньшее или равное размеру мира")
cletochki = input()
while cletochki.isdigit() == False:
    print("введите число")
    cletochki = input()
print("введите количество дней (всю информацию можно найти в описании репозитория), максимально 20")
povtorenie = input()
while povtorenie.isdigit() == False:
    print("введите число")
    povtorenie = input()
set_life = set()
if int(cletochki) <= int(dlina):
    for i in range(int(cletochki)):
        set_life.add("*")
    for i in range(int(dlina) - int(cletochki)):
        set_life.add("_")
list_life = []
for i in set_life:
    list_life.append(i)
for h in range(int(povtorenie)):
    list_lifeinprint = []
    for i in range(len(list_life)):
        if i == len(list_life) - 1:
            if (list_life[0] == "*" and list_life[i - 1] == "_") or (list_life[i - 1] == "*" and list_life[0] == "_"):
                list_lifeinprint.append("*")
            else:
                list_lifeinprint.append("_")
        elif (list_life[i - 1] == "*" and list_life[i + 1] == "_") or (list_life[i - 1] == "_" and list_life[i + 1] == "*"):
            list_lifeinprint.append("*")
        else:
            list_lifeinprint.append("_")
    print("".join(list_lifeinprint))
    list_life = list_lifeinprint
