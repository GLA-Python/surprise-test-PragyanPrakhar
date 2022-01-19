n = int(input().split())
def expanding():
    for i in n:
        difference= i[1] - i[0]
        if i[2]-i[1]>difference:
            return True
        else:
            return False
        
expanding()        