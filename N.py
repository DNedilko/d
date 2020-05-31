def shell(list):
    interval=len(list)//2 \\визначається інтервал між елементами, що ми переглядаємо
    while interval>0:
        for i in range(interval, len(list)): 
            t=int(list[i])    \\задається елемент для якого ми шукаємо місце
            j=i
            while j>=interval and int(list[j-interval])>t:\\порівнюється з тим, що стоїть на відстані інтервалу лівіше
                list[j]=list[j-interval]  \\якщо елемент лівіше більший, то менший стає на місце більшогоб а індекс зменшується на значення інтервалу
                j-=interval         \\так, поки виконується умова, що обраний індекс більший за кількість елементів в інтервалі та обраний елемент є меншим за той, що знаходиться на інтервальну відстань лівіше
            list[j]=t
        interval//=2   \\дії відбувається, поки інтервал не зменшиться до 0(коли інтервал 1 то сортування стає звичайним сотруванням вставками)
    return list



def insertion(list):    
    for i in range(len(list)):     \\для кожного елементу з інтексом і
        j = i - 1
        elem = int(list[i])
        while int(list[j]) > elem and j >= 0:   відбувається порівняння з наступним та якщо цей елемент менший, то позиція не змінюється, якщо більший, то елемент переходить уліво
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = elem
    return list

list=input("Enter the list separated by spaces").split()
choise=int(input("Choose an option shell sort(2) or insertion sort(1)"))
if choise is 2:
    print(shell(list))
else:
    print(insertion(list))
