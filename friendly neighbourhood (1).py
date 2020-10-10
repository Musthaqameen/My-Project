
neighbourArr = [10,3,2,5,7,1]

copyneighbourArr = list(neighbourArr)

copyneighbourArr.sort(reverse=True)

length = len(neighbourArr)

non = 0

for n in copyneighbourArr :
    non += n
    x = neighbourArr.index(n)
    p = x-1
    q = x+1
    if p >= 0:
        if neighbourArr[p] in copyneighbourArr:     
            copyneighbourArr.remove(neighbourArr[p])
    if q <= (length - 1):
        if neighbourArr[q] in copyneighbourArr:
            copyneighbourArr.remove(neighbourArr[q])


print(non)
        
    
        


