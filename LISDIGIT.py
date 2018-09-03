#def lis(arr):
#    stack = [arr[0]]
#    maxstack = 0
#    index = 0
#    for i, j in enumerate(arr):
#        counter = len(stack)
#        for a in range(i, len(arr)):
#            if arr[a] > stack[len(stack)-1]:
#                stack.append(arr[a])
#                counter += 1
#                index += 1
#        for _ in range(index-1):
#            stack.pop()
#        
#        if maxstack < counter:
#            maxstack = counter
#    
#    return maxstack
#
#arr = [1,7,3,0,4,1,8]
#
#print(lis(arr))
#for _ in range(int(input())):
#    n = int(input())
#    arr = list(map(int,input().split()))
#    x = '1'
# for i, j in enumerate(arr):
for i in range(int(input())):
    input()
    print(''.join(input().split()))