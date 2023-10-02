import random as r
import math
import time

def softmax(x):
    return 1 / (1 + math.exp(-x))

seconds = time.time()

fg = open('logs.txt', 'a')
fg1 = open('counter.txt', 'r')
number = int(fg1.read())+1
print("===============================================")
print("\\\Генератор историй Genitori///")
print()
print("Запуск №" + str(number) + " от:")
print(str(time.ctime(seconds)))
print()

fg.write('\t' + "===============================================" + '\n')
fg.write('\t' + "\\\Генератор историй Genitori///" + '\n')
fg.write('\n')
fg.write('\t' + "Запуск №" + str(number) + " от:" + '\n')
fg.write('\t' + str(time.ctime(seconds)) + '\n')
fg.write('\n')

fg1.close()

wordstart = input("Введи предложение: \n")
fg.write('\t' + "Введено предложение: " + wordstart + '\n')

wordinput = wordstart.lower()
fg.write('\t' + "Предложение превращено: " + wordinput + '\n')

counter = int(input("Введи количество запусков: "))
fg.write('\t' + "Ожидаемое число запусков: " + str(counter) + '\n')

print()

while counter != 0:
    
    fg.write('\t' + "\\\ГЕНЕРАЦИЯ, ВИТОК НОМЕР " + str(counter) + "///" + '\n')
    print("\\\ГЕНЕРАЦИЯ, ВИТОК НОМЕР " + str(counter) + "///" + '\n')
    
    wordstart = wordinput
    print()
    
    wordswork = wordstart.split(' ')
    wordswork = list(map(lambda x: x.replace(',', ''), wordswork))
    wordswork = list(map(lambda x: x.replace('\n', ''), wordswork))
    wordswork = list(map(lambda x: x.replace('.', ''), wordswork))
    wordswork = list(map(lambda x: x.replace(';', ''), wordswork))
    
    book = []
    f = open('library.txt', 'r')
    for line in f:
        book.append(line)
    booknew = list(map(lambda x: x.replace('\n', ''), book))
    f.close()
    
    if booknew == []:
        fg.write('\n')
        fg.write('\t' + "Словарь пуст, начинается заполнение..." + '\n')
        print("Словарь пуст и начинает заполнение...")
        f = open('library.txt', 'w')
        for i in range(len(wordswork)):
            f.write(wordswork[i] + '\n')
        f.close()
    
    f = open('library.txt', 'a')
    for i in range(len(wordswork)):
        if wordswork[i] not in booknew:
            fg.write('\t' + "!!!" + '\n')
            fg.write('\t' + "Обнаружено новое слово вне словаря:" + wordswork[i] + '\n')
            print("Пополнение словаря: " + wordswork[i])
            booknew.append(wordswork[i])
            f.write(wordswork[i] + '\n')
            fg.write('\t' + "!!!" + '\n')
    f.close()
    neuro = []
    for i in range(len(booknew)):
        if booknew[i] in wordswork:
            neuro.append(wordswork.count(booknew[i])) 
        else:
            neuro.append(0)
    #print(neuro)
    weights = []
    f = open('w.txt', 'r')
    for line in f:
        weights.append(float(line))
    f.close()
    
    if len(weights) != len(neuro):
        fg.write('\n')
        fg.write('\t' + "Длина эмбединга и весов не совпала, добавлено:" + '\n')
        f = open('w.txt', 'a')
        while len(weights) != len(neuro):
            v = r.uniform(-1, 1)
            fg.write('\t' + str(v) + '\n')
            weights.append(v)
            f.write(str(v) + '\n')         
        fg.write('\n')
    f.close()

    bias = []
    f = open('b.txt', 'r')
    for line in f:
        bias.append(float(line))
    f.close()
    if len(bias) != len(neuro):
        fg.write('\n')
        fg.write('\t' + "Длина эмбединга и смещений не совпала, добавлено:" + '\n')
        f = open('b.txt', 'a')
        while len(bias) != len(neuro):
            v = r.uniform(-1, 1)
            fg.write('\t' + str(v) + '\n')
            bias.append(v)
            f.write(str(v) + '\n')         
        fg.write('\n')
    f.close()
    
    fg.write('\n')
    fg.write('\t' + "Ввод::" + '\n')
    fg.write('\t' + str(wordswork) + '\n')
    print("Преобразованные введеные слова:")
    print(wordswork)
    print()
    
    fg.write('\n')
    fg.write('\t'+ "Словарь:" + '\n')
    fg.write('\t' + str(booknew) + '\n')
    
    fg.write('\t' + "Эмбединг:" + '\n')
    fg.write('\t' + str(neuro) + '\n')
    fg.write('\n')
    
    fg.write('\t' + "Веса:" + '\n')
    fg.write('\t' + str(weights) + '\n')
    fg.write('\n')

    fg.write('\t' + "Cмещения:" + '\n')
    fg.write('\t' + str(bias) + '\n')
    fg.write('\n')
    
    print("=============")
    print("Словарь: ") 
    print(booknew)
    print()
    print("Введено: ")
    print(wordswork)
    print()
    print("Эмбединг: ")
    print(neuro)
    print()
    print("Вес: ")
    print(weights)
    print("=============")
    
    
    output = []
    for i in range(len(neuro)):
        output.append(softmax(neuro[i]*weights[i] + bias[i]))
    
    FIN = []
    for i in range(len(output)):
        if len(FIN) == 4:
            break
        T = []
        T.append(max(output))
        T.append(output.index(T[0]))
        T.append(booknew[T[1]])
        FIN.append(T)
        output.pop(T[1])
    #print(FIN)
    
    for i in range(len(FIN)):
        fg.write('\n')
        fg.write('\t' + "===============================" + '\n')
        print("===============================")
        fg.write('\t' + "Максимальные вероятности №" + str(i+1) + ": " + '\n') 
        print("Максимальные вероятности №" + str(i+1) +": ")
        
        fg.write('\t' + "Вероятность = " + str(float(FIN[i][0]) * 100) + '%' + '\n') 
        print("Вероятность = " + str(float(FIN[i][0]) * 100) + "%")
        
        fg.write('\t' + "Вес = " + str(weights[FIN[i][1]]) + '\n') 
        print("Вес = " + str(weights[FIN[i][1]]))
        
        fg.write('\t' + "Смещение = " + str(bias[FIN[i][1]]) + '\n') 
        print("Смещение = " + str(bias[FIN[i][1]]))
        
        fg.write('\t' + "Индекс = " + str(FIN[i][1]) + '\n') 
        print("Индекс = " + str(FIN[i][1]))
        
        fg.write('\t' + "Слово = " + str(FIN[i][2]) + '\n')
        print("Слово = " + str(FIN[i][2]))
    fg.write('\t' + "===============================" + '\n')
    print("===============================")   
    
    output = []
    for i in range(len(FIN)):
        output.append(FIN[i][2])
    select = -1
    while select < 0 or not(select < len(FIN)):
        select = int(input("Выбрать вариант от 1 до " + str(len(output))))-1
    
    fg.write('\n')
    fg.write('\t' + "Выбран вариант: " + str(select) + '\n')
    fg.write('\t' + "Выбранное: " + str(output[select]) + '\n')
    
    wordinput += ' ' + output[select]
    corr = -1
    while corr not in {0, 1}:
        corr = int(input("Нужны ли корректировки весов? 1/0"))
    
    fg.write('\n')
    fg.write('\t' + "Корректировка весов: " + str(corr) + '\n')
    fg.write('\n')
    
    if corr == 1:
        for i in range(len(FIN)):
            fg.write('\t'+ "==============================="+ '\n')
            print("===============================")
            
            fg.write('\t' + "Кооректировка веса №" + str(i+1) + ": " + '\n')
            print("Кооректировка веса №" + str(i+1) +": ")
            
            fg.write('\t' + "Исходный вес: " + str(weights[FIN[i][1]]) + '\n')
            print("Вес = " + str(weights[FIN[i][1]]))
            
            fg.write('\t' + "Позиция в словаре: " + str(FIN[i][1]))
            print("Индекс = " + str(FIN[i][1]))
            
            wcorr = float(input("Введите число, на которое нужна коррекция: "))
            weights[FIN[i][1]] = weights[FIN[i][1]] + wcorr
            
            fg.write('\n')
            fg.write('\t' + "Число коррекции: " + str(wcorr) + '\n')
            fg.write('\t' + "Итоговый вес: " + str(weights[FIN[i][1]]) + '\n')
            print()
            print("Итоговый вес = " + str(weights[FIN[i][1]]))
            f = open('w.txt', 'w')
            for i in range(len(weights)):
                f.write(str(weights[i]) + '\n')
            f.close()
            fg.write('\t'+ "==============================="+ '\n')
            print("===============================")
            
    
    corr = -1
    while corr not in {0, 1}:
        corr = int(input("Нужны ли корректировки смещений? 1/0"))
    
    fg.write('\n')
    fg.write('\t' + "Корректировка смещений: " + str(corr) + '\n')
    fg.write('\n')
    
    if corr == 1:
        for i in range(len(FIN)):
            fg.write('\t'+ "==============================="+ '\n')
            print("===============================")
            
            fg.write('\t' + "Кооректировка смещения №" + str(i+1) + ": " + '\n')
            print("Кооректировка смещения №" + str(i+1) +": ")
 
            fg.write('\t' + "Исходное смещение: " + str(bias[FIN[i][1]]) + '\n')
            print("Вес = " + str(bias[FIN[i][1]]))
            
            fg.write('\t' + "Позиция в словаре: " + str(FIN[i][1]))
            print("Индекс = " + str(FIN[i][1]))
            
            bcorr = float(input("Введите число, на которое нужна коррекция: "))
            bias[FIN[i][1]] = bias[FIN[i][1]] + bcorr
            
            fg.write('\n')
            fg.write('\t' + "Число коррекции: " + str(bcorr) + '\n')
            fg.write('\t' + "Итоговый вес: " + str(bias[FIN[i][1]]) + '\n')
            print()
            print("Итоговый вес = " + str(bias[FIN[i][1]]))
            f = open('w.txt', 'w')
            for i in range(len(bias)):
                f.write(str(bias[i]) + '\n')
            f.close()
            fg.write('\t'+ "==============================="+ '\n')
            print("===============================")
    
    fg.write('\t' + "\\\КОНЕЦ ВИТКА НОМЕР " + str(counter) + "///" + '\n')
    print("\\\КОНЕЦ ВИТКА НОМЕР " + str(counter) + "///" + '\n')
    counter-=1
    
fg.write('\n')
fg.write('\t' + "Запуск №" + str(number) + " завершен." + '\n')
fg.write('\t' + str(time.ctime(seconds)) + '\n')
fg.write('\t' + "===============================================" + '\n')
fg.write('\n')
fg.close()
fg1 = open('counter.txt', 'w')
fg1.write(str(number))
fg1.close()