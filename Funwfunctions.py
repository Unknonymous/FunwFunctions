def odd_even():                         #function counts 1 - 2000  & specifies whether the current number is odd or even.
    for i in range (1, 2001):
        if i % 2 == 1:                  #checks if even or odd
            j = " an odd number."       # lines 4 - 6 
        else:
            j = " an even number"
        print "Number is", i,".", "This is" + j
#odd_even()                                #calls the function when not commented out



def multiply( a , m):                   #multiplies eacch value in a list by the 2nd arguement
    i = 0
    for i in range (0, len(a)):                         #loops through a
        a[i] *= m                          #multiplies by 2nd argument
#    print a                             #prints altered list when not commented out, replaced with 'return(a)' for use in layered_multiples() 
    return a

a = [2, 4, 10, 16]                      #intializing test case list

#multiply(a, 5)                          #calls the multiply() function when not commented out

def layered_multiples(arr):             #returns a list of lists of one 1 for each count in the list of ints input as an argument
    i = 0
    new_array = []                      #initializing variables to be processed
    for i in range (0, len(arr)):       #loops through the input list of ints
        cont = []                       #creates a container list to be used in the following loop
        for h in range (0, arr[i]):     #loops over the value of the current int
            cont.append(1)              #appends 1s equal to the value of arr[i] to a container list, would probably be broken by a negative int or a float
        new_array.append(cont)          #appends the container list to the new_array
    return new_array                    #returns the new array

x = layered_multiples(multiply([2,4,5],3))      #calls the function and inputs the function multiply() as an argument & set the returned value equal to x

print x                                 #prints x




    
