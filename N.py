def shell(list):
    interval=len(list)//2
    while interval>0:
        for i in range(interval, len(list)):
            t=int(list[i])
            j=i
            while j>=interval and int(list[j-interval])>t:
                list[j]=list[j-interval]
                j-=interval
            list[j]=t
        interval//=2
    return list



def insertion(list):
    for i in range(len(list)):
        j = i - 1
        elem = int(list[i])
        while int(list[j]) > elem and j >= 0:
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