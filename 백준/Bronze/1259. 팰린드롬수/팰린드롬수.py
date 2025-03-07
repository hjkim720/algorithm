while True:
    n=list(map(str,input()))
    if n==['0']:
        break
    else:
        if n==n[::-1]:
            print('yes')
        else:
            print('no')