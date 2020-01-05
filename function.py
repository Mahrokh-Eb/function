# # function definition
def sumMulti():
     print(50 + 1 + (12 ** 5))
sumMulti()  # calling funtion

# #mking another function
def Frank(attribiute):
     print("Frank is" +" "+ attribiute)
Frank("smart")

#function for sorting
items= [3,15,9,8,5,8,2,1]
def bubblesort(seq):
    length = len(seq)
    for i in range (1, length):
        if seq[i]> seq[i-1]:
            seq[i-1],  seq[i]= seq[i], seq[i-1]
    return seq
y= bubblesort(items)
print(y)