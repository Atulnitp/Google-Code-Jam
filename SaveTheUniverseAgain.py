import string
def universe(arr,damage):
    #print(arr)
    swap = 0
    d1 = calDamage(arr)
    while d1 > damage:
        rev = arr[::-1]
        if rev.find('SC') != -1:
            i = rev.find('SC')
            rev = rev[:i]+'CS'+rev[i+2:]
            swap += 1
        else:
            swap = -1
            break
        arr = rev[::-1]
        d1 = calDamage(arr)
        print(d1,swap,arr)
    return swap
        
def calDamage(arr):
    beam = 1
    d = 0
    for i in range(len(arr)):
        if arr[i] == 'S':
            d += beam
        else:
            beam = beam*2
    return d
        
                
            
            
        


if __name__ == '__main__':
    t = int(input())
    for k in range(t):
        d,ar = input().split()
        d = int(d)
        res = universe(ar,d)
        string = 'Case #'+str(k+1)+': '
        if res == -1:
            string = string + 'IMPOSSIBLE'
        else:
            string = string + str(res)
            
        print(string)
    
    
