for i in range(int(input())):
    n,p=input().split()
    a = list(map(int,input().split()))
    print('Dee' if a[0]%2==0 and p=='Dee' and n=='1' else 'Dum')
