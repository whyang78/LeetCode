

n,m = map(int,input('请从小到大输入两个不为0整数，用空格隔开：').split())
while((n*m)!=0 and n < m ):
    sum = 0
    for i in range(int(n), int(m) + 1, 1):
        sum += (1 / pow(i, 2))
    print('{:.5}'.format(sum))
    n, m = map(int, input('请从小到大输入两个不为0整数，用空格隔开：').split())