def binarySearch (arr, l, r, x):
    if r >= l:
 
        mid = l + (r - l)/2
 

        if arr[mid] == x:
            return mid
         


        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
 


        else:
            return binarySearch(arr, mid+1, r, x)
 
    else:
        return -1
 
def main():

    #arr = [ 2, 3, 4, 10, 40 ]
    x = 11
    arr=[]
    n=input("Enter the no of array elements:")
    for i in range (0,n):
        el=input("Enter the element:")
        arr.append(el)
    print(arr)
    x=input("Enter the element to search:")
    #print(x)
    result = binarySearch(arr, 0, len(arr)-1, x)
 
    if result != -1:
    	print "Element is present at index %d" % result
    else:
        print "Element is not present in array"
 	  

if __name__ == '__main__':
    main()
