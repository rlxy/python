def jiujiu():
    print('九九乘法表')
    for o in range (1,10):
        for i in range (1,o+1):
            print( o * i , end='  ')
        print()
    return None
jiujiu()