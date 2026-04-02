import pandas as pd
import numpy as np
from tkinter import *
from tkinter import filedialog


window = Tk()
window.title("creating AA consensus")
window.geometry('1024x512')
window.config(bg='White smoke')
lbl = Label(window, text="1. Chosee your file for work", font=("Arial Bold", 12))                       #текст для GUI
lbl.grid(column=0, row=0, sticky='w')  
lbl3 = Label(window, text='3. Click button for create consensus', font=("Arial Bold", 12))
lbl3.grid(column=0, row=2, sticky='w')

def clicked():              #функция для нажатия кнопки (возвращает путь к файлу)
    global s1
    s1=filedialog.askopenfilename()

btn = Button(window, text="choose file", command=clicked)  
btn.grid(column=0, row=1, sticky='w')


def clicked2():   #функция для нажатия кнопки запускает код
    a={}
    k=''
    s=''                          #cоздать запись в словаре с ключем
    with open (s1) as file:
      for row in file:
        if row[0]== '>':
          k = row.split()[0][1:]            #создаём словарь где ключ это заголовок, а значение последовательность АК
          s=''
        else:
          s+=row.strip() 
        a[k]=s


    c = [''] * 379              #создаём пустые списки для матрицы
    c = np.array(c).reshape((1,379))        #создаём матрицу
    df=pd.DataFrame(data=c, columns = [i for i in range(1,380)])        #создаём датафрейм

    for key, val in a.items():          #цикл для вписывания последовательносцей по строкам
        df=np.vstack([df,list(val)])

    df=pd.DataFrame(data=df, columns = [i for i in range(1,380)])   #создаём датафрейм, в котором строки это - последовательности, а столбцы - номера позиций АК в каждой последовательности
    df.tail(-1)  #убираем колонку №0,чтобы первая АК соответствовала первому столбцу

    hop=[]          #cоздаём список, в котором будут лежать списки последовательностей
    for i in df:    #ходим по строкам датафрейм 
      temp = df[i]
      hop.append(temp.tolist())  #вписываем списки поледовательностей, где каждая АК имеет тип str, в список


    spisok=[]       #создаём новый список, где будет каждая последовательность в процентном соотношении
    for i in range(379):    #ходим по каждой последовательности и смотрим какая это АК
      I=hop[i].count('I')
      V=hop[i].count('V')
      L=hop[i].count('L')
      M=hop[i].count('M')
      S=hop[i].count('S')
      P=hop[i].count('P')
      T=hop[i].count('T')
      A=hop[i].count('A')
      Y=hop[i].count('Y')
      H=hop[i].count('H')
      N=hop[i].count('N')
      D=hop[i].count('D')
      Q=hop[i].count('Q')
      K=hop[i].count('K')
      E=hop[i].count('E')
      C=hop[i].count('C')
      R=hop[i].count('R')
      G=hop[i].count('G')
      W=hop[i].count('W')
      F=hop[i].count('F')
      spisok.append([I/len(a),V/len(a),L/len(a),M/len(a),S/len(a),P/len(a),T/len(a),A/len(a),Y/len(a),H/len(a),N/len(a),D/len(a),Q/len(a),K/len(a),E/len(a),C/len(a),R/len(a),G/len(a),W/len(a),F/len(a)])  #записываем список с процентным соотношением АК
      I=0
      V=0
      L=0
      M=0
      S=0
      P=0    #обнуляем каждую АК для следующий списков
      T=0
      A=0
      Y=0
      H=0
      N=0
      D=0
      Q=0
      K=0
      E=0
      C=0
      R=0
      S=0
      G=0
      W=0
      F=0

    list_values = ['I','V','L','M','S','P','T','A','Y','H','N','D','Q','K','E','C','R','G','W','F']  #список АК для индексов датафрейма

    df2=pd.DataFrame((spisok))  #заполняем датафрейм последовательностями, где каждая АК в процентном соотношении
    df2=df2.T       #переворачиваем ДФ, чтобы последовательности были строками
    df2.index=list_values       #вписываем вместо индексов АК
    df2.columns=np.arange(1,380)    #создаём 379 столбцов

    consen2=df2.idxmax().to_string(min_rows=None)     #находим каждую АК, у которой наивысший процент встречаемости и её колонку 

    consen=''       #создаём список для записи консенсуса
    for i in consen2:   #ищем АК и добавляем их в список - будующий консенсус
      if i == 'I':
        consen+=i
      if i == 'V':
        consen+=i
      if i == 'L':
        consen+=i
      if i == 'M':
        consen+=i
      if i == 'S':
        consen+=i
      if i == 'P':
        consen+=i
      if i == 'T':
        consen+=i
      if i == 'A':
        consen+=i
      if i == 'Y':
        consen+=i
      if i == 'H':
        consen+=i
      if i == 'N':
        consen+=i
      if i == 'D':
        consen+=i
      if i == 'Q':
        consen+=i
      if i == 'K':
        consen+=i
      if i == 'E':
        consen+=i
      if i == 'C':
        consen+=i
      if i == 'R':
        consen+=i
      if i == 'G':
        consen+=i
      if i == 'W':
        consen+=i 
      if i == 'F':
        consen+=i


    naivish=[]      #создаём список для добавления АК, у которых процент>0.9 
    for i in df2:       #ходим по столбцам ДФ в поисках АК, у которых процент>0.9 
      if df2[i].max()>=0.9:  #если значение процента >= 0.9, то вписываем его в список
        naivish.append(i)       #число = номеру АК в консенсусе

    def find_sequences(naivish):
        sequences = []          # список для хранения найденных последовательностей

        start_index = None      # создаём переменную для хранения индекса первого числа в последовательности
        end_index = None    # сщздаём переменную для хранения индекса последнего числа в последовательности

        for i in range(len(naivish)):       #ходим по списку чисел
            if naivish[i] - naivish[i - 1] != 1:        # Последовательность прервалась
                if start_index is not None and end_index - start_index + 1 >= 8:         #запоминаем начало координат последовательности, где 8 или более АК, у которых процент встречаемости >=0.9, идут подряд 
                    sequences.append((start_index, end_index))

                start_index = None
                end_index = None

            if start_index is None:
                start_index = i # Запоминаем индекс первого числа в последовательности
            end_index = i       # Запоминаем индекс последнего числа в последовательности

        if start_index is not None and end_index - start_index + 1 >= 8:    #добавляем идексы первых и последних  чисел в виде кортежей в список
            sequences.append((start_index, end_index))
        return sequences    #возвращаем список для запоминания всех координат

    sequences = find_sequences(naivish)     #задаём список координат функции в новую переменную 
    print(consen)
    print(sequences)

    with open ('consensus.fasta','a') as fp:        #записываем всё в файл

        fp.write(consen)
        for t in sequences:     #ходим по списку кортежей
          fp.write('\n' + ' '.join(str(s) for s in t) + ', ')  #записываем их в файл в виде строчек      

btn = Button(window, text="create consensus", command=clicked2)  
btn.grid(column=0, row=5, sticky='w')


window.mainloop()
