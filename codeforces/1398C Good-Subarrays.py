from collections import defaultdict
t =int(input())

for _ in range(t):
    n = int(input())
    a = input()

    arr = []
    for i in range(n):
        arr.append(int(a[i]))
    
    prefix = [0]
    cur = 0
    for i in range(n):
        cur += arr[i]
        prefix.append(cur)
    

    #map for 
    mapp = defaultdict(int)
    count = 0
    for l in range(1,len(prefix)):
        theKey = prefix[l-1] - l + 1
        mapp[theKey] += 1
        
       
        if (prefix[l] - (l)) in mapp:
            count += mapp[prefix[l] - (l)]
    
    
    
    print(count)

    

