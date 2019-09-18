a,b,c = map(int,input('输入三个数:').split(','))
while(a!=0 and b!=0 and c!=0 and c<=100 ):
    print(round(a/b,c))
    # print('{:.c}'.format(a/b))
    a, b, c = map(int, input('输入三个数:').split(','))