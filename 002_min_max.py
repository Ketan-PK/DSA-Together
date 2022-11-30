#User function Template for python3

def getMinMax( a, n):
    if n == 1:
        minimum = a[0]
        maximum = a[0]
        return minimum, maximum
        
    if a[0]>a[1]:
        maximum = a[0]
        minimum = a[1]
    else:
        maximum = a[1]
        minimum = a[0]
        
    for i in range(2, n):
        if a[i] > maximum:
            maximum = a[i]
        elif a[i] < minimum:
            minimum = a[i]
            
            
    return minimum, maximum
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        product = getMinMax(a, n)
        print(product[0], end=" ")
        print(product[1])

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends
