# def binarySearch(arr, target, start, end):
#   if start > end:
#     return None
  
#   mid = (start + end) // 2
#   if arr[mid] == target:
#     return mid 
#   elif arr[mid] > target:
#     return binarySearch(arr, target, start, mid - 1)
#   else:
#     return binarySearch(arr, target, mid + 1, end)

# t = int(input())
# for i in range(t):
#     arr = list(map(int, input().split()))
#     target = list(map(int, input().split()))
#     res = binarySearch(arr, target, 0, len(target) - 1)

#     if target in arr:
#       print(arr.index(i))
#     else:
#       print(-1)

t = int(input())

for _ in range(t) :
    data = list(map(int, input().split()))  
    query = list(map(int, input().split()))   
    answer = []
    
    for q in query :
        left = 0
        right = len(data) - 1
        
        while left <= right :
            mid = (left + right) // 2
            
            if data[mid] == q :
                break
            elif data[mid] > q :
                right = mid - 1
            elif data[mid] < q :
                left = mid + 1
            left += 1
            
            
            
        if left > right :
            answer.append(-1)
        else :
            answer.append(mid)
            
    print(answer)