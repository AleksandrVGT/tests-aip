def task_1(two_dim_words):
    """
        Здесь должен быть ваш код.
        Переменная two_dim_words - ваш двумерный список.
        Заполнять список значениями не нужно.
        Финальное значение должно быть помещено в переменную sorted_words.
        """
   
    sorted_words = []
    for i in two_dim_words:
        for j in i:
            sorted_words.append(j)
    sorted_words.sort()
    sorted_words.sort(key=len, reverse=True)


    return sorted_words


def task_3(numbers):
    """
        Здесь должен быть ваш код.
        Переменная numbers - ваша строка чисел.
        Финальное значение должно быть помещено в переменную dict_min.
        """
    c = []
    dict_min = {}
    r = 0
    v = 0
    q = 0
    a = 0
    z = []
    x = []
    t = {}
    lst_1 = []
    lst_2 = []
    w = 0


    for i in range(len(numbers)):
        if numbers[i] in c:
            continue
        else:
            x.append(numbers.count(numbers[i]))
            c.append(numbers[i])
    for s in c:
        t[s] = x[w]
        w += 1

    new_1 = t.copy()
    p = max(new_1.values())
    for i, j in new_1.items():
        if j == p:
            q = i
            lst_1.append(int(i))
            lst_2.append(int(j))
    new_2 = t.copy()
    new_2.pop(q)
    d = max(new_2.values(), default=0)
    for i, j in new_2.items():
        if j == d:
            lst_1.append(int(i))
            lst_2.append(int(j))
            a = i

    new_3 = new_2.copy()
    new_3.pop(a)
    k = max(new_3.values())
    for i, j in new_3.items():
        if j == k:
            lst_1.append(int(i))
            lst_2.append(int(j))

    for o in lst_1:
        dict_min[o] = lst_2[v]
        v += 1

        
    return dict_min


def task_4_1(f):
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res
        """

    b=[]
    c=set()
    p=['e','u','o','a','i','y']
    q=[]

    for i in f:
        m = i.lower()
        if m.count('a')>=2:
            b.append(m.count('a')**2)
        else:
            continue
    res = tuple(b)
    return res


def task_4_2(f):  # можно сделать тесты
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """
    
    b=[]
    c=set()
    p=['e','u','o','a','i','y']
    q=[]

    for i in f:
        if len(i)>3:
            c.add(len(i))
    res=c

    return res


def task_4_3(f):
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """

    b=[]
    c=set()
    p=['e','u','o','a','i','y']
    l=0
    qr=0
    v=0
    mm=[]
    total=[]
    ar=[]
    letters_1=0
    letters_2=0
    letters_3=0
   
    q=[]

    
    for i in f:
        l = i.lower()
        if l.endswith('a'):
            for j in l:
                if j not in p and v == 0:
                    letters_1 += 1
                if j not in p and v == 1:
                    letters_2 += 1
                if j not in p and v == 2:
                    letters_3 += 1
            v += 1


    for i in f:
        l = i.lower()
        if l.endswith('a'):
            for j in l:
                if j not in p:
                    if qr < letters_1:
                        q.append(j)

                    if qr >= letters_1 and qr < (letters_1 + letters_2):
                        mm.append(j)

                    if qr >= (letters_1 + letters_2):
                        ar.append(j)
                    qr += 1

    total.append(''.join(q))
    total.append(''.join(mm))
    total.append(''.join(ar))
    print(total)
    return total


def task_5(lst1, lst2):
    """
        Здесь должен быть ваш код.
        Переменные lst1 и lst2 - два данных списка.
        Финальное значение должно быть помещено в переменную diff.
        """

    lst3 = set(lst1)
    lst4 = set(lst2)
    diff = []
    d = lst4.intersection(lst3, lst4)
    for i in lst3:
        if i not in d:
            diff.append(i)
    print(diff)
    c = sorted(diff)

    return c


def task_6(c):
    """
        Здесь должен быть ваш код.
        Переменная lst - ваш список.
        Финальное значение должно быть помещено в переменную res.
        """
    
    
    d = set(c)
    res = (tuple(sorted(d, reverse=True)))

    return res
