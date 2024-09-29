from collections import Counter

with open('file.txt', 'w') as file:
    pass
    k = 0
    item = input ("Введите пункт номера:")
    if item == '1':
        for a in ('12345678'):
            for b in ('12345678'):
                for c in ('12345678'):
                    for d in ('12345678'):
                        for e in ('12345678'):
                            s=str(a+b+c+d+e)
                            k+=1
                            file.writelines(s + '\n')
    elif item == '2':
        for a in ('12345678'):
            for b in ('12345678'):
                for c in ('12345678'):
                    for d in ('12345678'):
                        for e in ('12345678'):
                            for f in ('12345678'):
                                for g in ('12345678'):
                                    s=str(a+b+c+d+e+f+g)
                                    count = Counter(s)
                                    values = sorted(count.values(), reverse=True)
                                    if values == [3, 2, 1, 1]:
                                        k+=1
                                        file.writelines(s + '\n')
    elif item == '3':
        for a in ('12345678'):
            for b in ('12345678'):
                for c in ('12345678'):
                    for d in ('12345678'):
                        for e in ('12345678'):
                            for f in ('12345678'):
                                s = str(a + b + c + d + e + f)
                                if s.count('2') == 3:
                                    k+=1
                                    file.writelines(s + '\n')
    else:
        print("Error")
    file.writelines('\n'+ "Count - " + str(k))
    file.close()
