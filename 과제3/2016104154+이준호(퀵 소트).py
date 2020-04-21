def partition(s,low,high):
    pivot = s[low]
    j = low
    for i in range(low+1,high+1):
        if(s[i] < pivot):
            j+=1
            s[i],s[j] = s[j],s[i] 
    pivot = j
    s[low],s[pivot] = s[pivot],s[low]
    return pivot

def quicksort(s,low,high):
    if(high>low):
        pivot = partition(s,low,high)
        quicksort(s,low,pivot-1)
        quicksort(s,pivot+1,high)

s=[3,5,2,9,10,14,4,8]
print("before sorting: ",s)
quicksort(s,0,7)
print("after sorting: ",s)