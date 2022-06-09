for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    if i %2 is not 0:
        print(i, '홀수')
    else:
        print(i, '짝수')


price = [23, 40, 67]
for i in price:
    print(i * 1.1)
    
 def service_price():
        service = input('서비스 종류를 입력하세요, a/b/c: ')
        valueAdded = input("부가세를 포함합니까? y/n: ")
        if valueAdded == 'y':
            if service == 'a':
                result = 23 * 1.1
            if service == 'b':
                result = 40 * 1.1
            if service == 'c':
                result = 67 * 1.1
        if valueAdded == 'n':
            if service == 'a':
                result = 23
            if service =='b':
                result = 40
            if service == 'c':
                result = 67
        print(round(result, 1), '만 원입니다')
service_price()
        
서비스 종류를 입력하세요, a/b/c: b
부가세를 포함합니다? y/n: y
44.0만 원입니다
service_price()
서비스 종류를 입력하세요, a/b/c: c
부가세를 포함합니까? y/n: n
67만 원입니다

