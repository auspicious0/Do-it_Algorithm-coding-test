#재귀적 형태로 구현해본 퀵정렬
n,k=map(int,input().split())
num=list(map(int,input().split()))
def quick(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)//2]
    lesser_arr,equal_arr,greater_arr=[],[],[]
    for num in arr:
        if num<pivot:
            lesser_arr.append(num)
        elif num>pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick(lesser_arr)+equal_arr+quick(greater_arr)
