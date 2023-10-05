import random as r
import math
import time
import os

def softmax(x):
    return 1 / (1 + math.exp(-x))

# потенциально: сделать аналогичную функцию, как внизу, только для списков
def texteditor(text):    
    listwords = text.split(' ')
    listwords = list(map(lambda x: x.replace(',', ''), listwords))
    listwords = list(map(lambda x: x.replace('\n', ''), listwords))
    listwords = list(map(lambda x: x.replace('.', ''), listwords))
    listwords = list(map(lambda x: x.replace(';', ''), listwords))
    
    for i in range(listwords.count('и')):
        listwords.remove('и')   
    for i in range(listwords.count('как')):
        listwords.remove('как')
    for i in range(listwords.count('или')):
        listwords.remove('или')
    for i in range(listwords.count('но')):
        listwords.remove('но')
    for i in range(listwords.count('а')):
        listwords.remove('а')
    
    return listwords

seconds = time.time()
#specialwords = ['и', 'как', 'или', 'но', 'a']
dtf = list(map(lambda x: x.replace(':', '-'), time.ctime(seconds)))
dateformat = ""
for i in dtf:
    dateformat+=i

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

counter = 6
fg.write('\t' + "Ожидаемое число запусков: " + str(counter) + '\n')

print()

while counter != 0:
    
    fg.write('\t' + "\\\ГЕНЕРАЦИЯ, ВИТОК НОМЕР " + str(counter) + "///" + '\n')
    print("\\\ГЕНЕРАЦИЯ, ВИТОК НОМЕР " + str(counter) + "///" + '\n')
    
    wordstart = wordinput
    wordswork = texteditor(wordstart)
    #print(wordswork)
    print(wordstart)
    print()
    
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
        f = open('library.txt', 'a')
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
    
    neuro = [[], []]
    for i in range(len(booknew)):
        if booknew[i] in wordswork:
            neuro[0].append(wordswork.count(booknew[i])) 
        else:
            neuro[0].append(0)
        neuro[1].append(0)
    
    f = open('w.txt', 'r')
    weights = []
    for i in range(len(neuro[0])):
        T = []
        w = f.readline()
        w = w.split(';')
        w = list(map(lambda x: x.replace('\n', ''), w))
        for g in range(w.count('')):
            w.remove('')
        w = list(map(lambda x: float(x), w))
        for j in range(len(neuro[1])):
            try:
                T.append(w[j])
            except IndexError:
                fg.write('\n')
                fg.write('\t' + "Длина эмбединга и весов не совпала, добавлено:" + '\n')
                v = r.uniform(-1, 1)
                T.append(v)
                fg.write('\t' + str(v) + '\n')
        weights.append(T)            
    f.close()

    f = open('b.txt', 'r')
    bias = []
    for i in range(len(neuro[0])):
        T = []
        b = f.readline()
        b = b.split(';')
        b = list(map(lambda x: x.replace('\n', ''), b))
        for g in range(b.count('')):
            b.remove('')
        b = list(map(lambda x: float(x), b))
        for j in range(len(neuro[1])):
            try:
                T.append(b[j])
            except IndexError:
                fg.write('\n')
                fg.write('\t' + "Длина эмбединга и весов не совпала, добавлено:" + '\n')
                v = r.uniform(-1, 1)
                T.append(v)
                fg.write('\t' + str(v) + '\n')
        bias.append(T)            
    f.close()
    
    fg.write('\n')
    fg.write('\t' + "Ввод:" + '\n')
    fg.write('\t' + str(wordswork) + '\n')
    print("Преобразованные введеные слова:")
    print(wordswork)
    print()
    
    fg.write('\n')
    fg.write('\t'+ "Словарь:" + '\n')
    fg.write('\t' + str(booknew) + '\n')
    
    fg.write('\t' + "Эмбединг:" + '\n')
    for i in range(len(neuro)):
        fg.write('\t' + str(i) + " cлой:" + str(neuro[i]) + '\n')
        fg.write('\n')
    fg.write('\n')
    
    fg.write('\t' + "Веса:" + '\n')
    for i in range(len(weights)):
        fg.write('\t' + "Вес " + str(i) + " нейрона" + str(weights[i]) + '\n')
        fg.write('\n')
    fg.write('\n')
    
    fg.write('\t' + "Cмещения:" + '\n')
    for i in range(len(bias)):
        fg.write('\t' + "Смещение " + str(i) + " нейрона" + str(bias[i]) + '\n')
        fg.write('\n')
    fg.write('\n')


    for i in range(len(neuro[0])):
        for j in range(len(weights[i])):
            neuro[1][i]+=neuro[0][i] * weights[i][j] + bias[i][j]
        neuro[1][i] = softmax(neuro[1][i])
    
    FIN = []
    output = neuro[1]
    for i in range(len(output)):
        if len(FIN) == 4:
            break
        T = []
        T.append(max(output))
        T.append(output.index(T[0]))
        T.append(booknew[T[1]])
        FIN.append(T)
        output.pop(T[1])
    
    for i in range(len(FIN)):
        fg.write('\n')
        fg.write('\t' + "===============================" + '\n')
        print("===============================")
        fg.write('\t' + "Максимальные вероятности №" + str(i+1) + ": " + '\n') 
        print("Максимальные вероятности №" + str(i+1) +": ")
        
        fg.write('\t' + "Вероятность = " + str(float(FIN[i][0]) * 100) + '%' + '\n') 
        print("Вероятность = " + str(float(FIN[i][0]) * 100) + "%")
        
        fg.write('\t' + "Строка весов:" + '\n')
        fg.write('\t' + str(weights[FIN[i][1]]) + '\n')
        print("Строка весов:")
        print(str(weights[FIN[i][1]]))

        fg.write('\t' + "Строка смещений:" + '\n')
        fg.write('\t' + str(bias[FIN[i][1]]) + '\n')
        print("Строка смещений:")
        print(str(bias[FIN[i][1]]))
        
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
    while select not in {0, 1, 2, 3, 4, 5}:
        select = int(input("Выбрать вариант от 1 до " + str(len(output)) + '(5 - остановка)'))-1
    try:
        fg.write('\n')
        fg.write('\t' + 'Выбран вариант #' + str(select) + ':\n')
        fg.write('\t' + output[select] + '\n')
        
        wordinput += ' ' + output[select]
        fg.write('\t' + 'Итоговый текст:' + '\n')
        fg.write('\t' + wordinput + '\n')
        print()
        print("Итоговый текст:")
        print(wordinput)
        
        fg.write('\n')
        fg.write('\t' + 'Корректировка весов и смещений:' + '\n')
        fg.write('\n')
        
        matrixhist = open('matrixhistory/matrixhistory' + dateformat + '.txt', 'w')
        mhcounter = open('matrixhistory/counterhistory.txt', 'r')
        mh = int(mhcounter.read())+1
        mhcounter.close()
        mhcounter = open('counterhistory.txt', 'w')
        matrixhist.write('\t' + "===============================================" + '\n')
        matrixhist.write('\t' + "Корректировка весов и смещений №" + str(mh) + '\n')
        mhcounter.write(str(mh))
        mhcounter.close()
        matrixhist.write('\n')
        matrixhist.write('\t' + time.ctime() + '\n')
        
        fg.write('\n')
        fg.write('\t' + "Исходный массив весов:" + '\n')
        for i in weights:
            fg.write('\t' + "[ ")
            for j in range(len(i)):
                fg.write(str(i[j]) + ' ; ')
            fg.write(" ]" + '\n')
        
        matrixhist.write('\n')
        matrixhist.write('\t' + "Исходный массив весов:" + '\n')
        for i in weights:
            matrixhist.write('\t' + "[ ")
            for j in range(len(i)):
                matrixhist.write(str(i[j]) + ' ; ')
            matrixhist.write(" ]" + '\n')
            
        fg.write('\n')
        fg.write('\t' + "Исходный массив смещений:" + '\n')
        for i in bias:
            fg.write('\t' + "[ ")
            for j in range(len(i)):
                fg.write(str(i[j]) + ' ; ')
            fg.write(" ]" + '\n')
            
        matrixhist.write('\n')
        matrixhist.write('\t' + "Исходный массив смещений:" + '\n')
        for i in bias:
            matrixhist.write('\t' + "[ ")
            for j in range(len(i)):
                matrixhist.write(str(i[j]) + ' ; ')
            matrixhist.write(" ]" + '\n')
        
        for i in range(len(FIN)):
            if i != select:
                for j in range(len(weights[FIN[i][1]])):
                    weights[FIN[i][1]][j]-=0.1
                for j in range(len(bias[FIN[i][1]])):
                    bias[FIN[i][1]][j]-=0.1
            else:
                for j in range(len(weights[FIN[i][1]])):
                    weights[FIN[i][1]][j]+=0.1
                for j in range(len(bias[FIN[i][1]])):
                    bias[FIN[i][1]][j]+=0.1

        fg.write('\n')
        fg.write('\t' + "Полученный массив весов:" + '\n')
        for i in weights:
            fg.write('\t' + "[ ")
            for j in range(len(i)):
                fg.write(str(i[j]) + ' ; ')
            fg.write(" ]" + '\n')
        
        matrixhist.write('\n')
        matrixhist.write('\t' + "Полученный массив весов:" + '\n')
        for i in weights:
            matrixhist.write('\t' + "[ ")
            for j in range(len(i)):
                matrixhist.write(str(i[j]) + ' ; ')
            matrixhist.write(" ]" + '\n')
        
        fg.write('\n')
        fg.write('\t' + "Полученный массив смещений:" + '\n')
        for i in bias:
            fg.write('\t' + "[ ")
            for j in range(len(i)):
                fg.write(str(i[j]) + ' ; ')
            fg.write(" ]" + '\n')
        
        matrixhist.write('\n')
        matrixhist.write('\t' + "Полученный массив смещений:" + '\n')
        for i in bias:
            matrixhist.write('\t' + "[ ")
            for j in range(len(i)):
                matrixhist.write(str(i[j]) + ' ; ')
            matrixhist.write(" ]" + '\n')
        
        matrixhist.write('\t' + "Корректировка весов и смещений №" + str(mh) + '\n')    
        matrixhist.write('\t' + "===============================================" + '\n')
        matrixhist.close()
        
        f = open('w.txt', 'w')
        for i in range(len(weights)):
            for j in range(len(weights[i])):
                f.write(str(weights[i][j]) + ';')
            f.write('\n')
        f.close()
        
        f = open('b.txt', 'w')
        for i in range(len(bias)):
            for j in range(len(bias[i])):
                f.write(str(bias[i][j]) + ';')
            f.write('\n')
        f.close()  
        
        fg.write('\t' + "\\\КОНЕЦ ВИТКА НОМЕР " + str(counter) + "///" + '\n')
        print("\\\КОНЕЦ ВИТКА НОМЕР " + str(counter) + "///" + '\n')
        counter-=1
    except IndexError:
        fg.write('\n')
        fg.write('\t' + 'Остановка на шаге' + str(counter) + ':\n')
        
        fg.write('\t' + 'Итоговый текст:' + '\n')
        fg.write('\t' + wordinput + '\n')
        print()
        print("Итоговый текст:")
        print(wordinput)
        
        fg.write('\t' + "\\\КОНЕЦ ВИТКА НОМЕР " + str(counter) + "///" + '\n')
        print("\\\КОНЕЦ ВИТКА НОМЕР " + str(counter) + "///" + '\n')

        fg.write('\n')
        fg.write('\t' + "Запуск №" + str(number) + " завершен." + '\n')
        fg.write('\t' + str(time.ctime(seconds)) + '\n')
        fg.write('\t' + "===============================================" + '\n')
        fg.write('\n')
        fg.close()
        fg1 = open('counter.txt', 'w')
        fg1.write(str(number))
        fg1.close()
        exit()
    
fg.write('\n')
fg.write('\t' + "Запуск №" + str(number) + " завершен." + '\n')
fg.write('\t' + str(time.ctime(seconds)) + '\n')
fg.write('\t' + "===============================================" + '\n')
fg.write('\n')
fg.close()
fg1 = open('counter.txt', 'w')
fg1.write(str(number))
fg1.close()