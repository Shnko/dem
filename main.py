def 
print("Меню")
menu = """
    Создать новую заметку              -[1]
    Редактировать существующую заметку -[2]
    Удалить существующую заметку       -[3]
    Открыть существующую заметку       -[4]
"""
print(menu)
a = int(input())
while a == 1:
    print("Придумайте название для заметки, нажмите [X], когда захотите выйти")
    my_file = open(input() + '.txt', "w")
    print("Введите текст")
    filetext = "b"
    while filetext != "X":
        filetext = input()
        my_file.write(filetext)
    print("Желаете закончить?")
    otvet = """
    Закрыть и сохранить           -[1]
    Просто выйти зачем сохранять  -[2]
    """
    print(otvet)
    otvet = int(input())
    if otvet == 1:
        my_file.close()
        print("Ваш ответ сохранен")
        a = 0
    else:
        break
