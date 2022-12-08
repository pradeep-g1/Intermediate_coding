def bubble_sort(arr,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                print("each iteration\n",arr)
    return arr
arr=list(map(int,input("enter the elements: ").split(",")))
print("before bubble: ",arr)
print("after bubblesort: ")
print(bubble_sort(arr,len(arr)))