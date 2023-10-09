n, a, b, c = [int(i) for i in input().split()]

def re(len,count):
    print('============',len,'============')

    if len == 0:
        # print('============',count,'============')

        return(count)
    elif len < 0:
        # print('============',count,'============')
        return(-1)
    else:
        a_len =  
        return(max([
        re(len-c,count + 1),
        re(len-b,count + 1),
        re(len-a,count + 1)
        ]))
print(re(n,0))
# print(n,a,b,c)
# print(max([1,2,4]))