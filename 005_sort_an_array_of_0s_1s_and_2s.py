#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        
        count_zero = 0
        count_one = 0
        count_two = 0
        
        for i in arr:
            if i == 0:
                count_zero += 1
                
        for i in arr:
            if i == 1:
                count_one += 1
                
        for i in arr:
            if i == 2:
                count_two += 1
        
        del arr[:]
        
        for i in range(count_zero):
            arr.append(0)
        
        for i in range(count_one):
            arr.append(1)
        
        for i in range(count_two):
            arr.append(2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends
