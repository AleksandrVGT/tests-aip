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
            break
    new_2 = t.copy()
    new_2.pop(q)
    d = max(new_2.values())
    for i, j in new_2.items():
        if j == d:
            a = i
            break
    new_3 = new_2.copy()
    new_3.pop(a)
    k = max(new_3.values())
    for i, j in new_3.items():
        if j == k:
            r = i
            break
    lst_1 = [q, a, p]
    lst_2 = [p, d, r]
    for o in lst_1:
        dict_min[o] = lst_2[v]
        v += 1
    returndict_min


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
    res = tuple(b))
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
   
    q=[]

    for i in f:
        l=i.lower()
        if l.endswith('a'):
            for j in l:
                if j not in p:
                    q.append(j)
    res=q

    return res


def task_5(lst1, lst2):
    """
        Здесь должен быть ваш код.
        Переменные lst1 и lst2 - два данных списка.
        Финальное значение должно быть помещено в переменную diff.
        """

    diff1 = []

    d = lst2.intersection(lst1, lst2)
    for i in lst1:
        if i not in d:
            diff1.append(i)
    diff = sorted(diff1)

    return diff


def task_6(c):
    """
        Здесь должен быть ваш код.
        Переменная lst - ваш список.
        Финальное значение должно быть помещено в переменную res.
        """
    
    c =[int(i) for i in input().split()]
    d=[]
    for i in c:
        if c.count(i)==1:
            d.append(i)
    res = tuple(sorted(d, reverse=True))
    return res
