
# coding: utf-8

# In[20]:


n = int(input())

# Виды абонементов
typesOfTickets = (60, 10, 1)

# Словарь вида 'колво поездок': стоимость абонемента
tickets = {'typesOfTickets[0]': 440, 
           'typesOfTickets[1]': 125, 
           'typesOfTickets[2]': 15}

# Минимальное количество абонементов, с которого
# выгоднее покупать следующий по стоимости абонемент
minCount = (int((typesOfTickets[1] * 
                 tickets['typesOfTickets[0]'] / 
                 tickets['typesOfTickets[1]']) // 1 + 1), 
            tickets['typesOfTickets[1]'] // 
                 tickets['typesOfTickets[2]'] + 1, 
            1)

# Сколько надо купить
count = [0 for x in range(len(typesOfTickets))]

while n > 0:    
    if (n >= minCount[0]):
        count[0] += 1
        n -= typesOfTickets[0]
        
    elif (n >= minCount[1]):
        count[1] += 1
        n -= typesOfTickets[1]
        
    else:
        count[2] += 1
        n -= typesOfTickets[2]
        
# Вывод на экран
for x in range(len(count)):
    print(count[x], end = ' ')

