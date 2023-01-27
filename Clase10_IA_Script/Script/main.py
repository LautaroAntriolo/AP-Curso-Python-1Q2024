
def quiniela(dic):
    dia = str(datetime.datetime.now().date())
    dic[dia] = []
    for i in range(0,len(N10)):
        dic[dia].append(N10[i])
    return dic

dic ={'2023-01-26': [39, 55, 18, 47, 63, 46, 80, 69, 65, 31]}

if __name__ == '__main__':
    from numeros import N10
    import datetime
    # quiniela(dic)
    print(quiniela(dic))
    
