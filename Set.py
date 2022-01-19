#StudentName :Yash KOladiya
#Studentid   :20CS028
#Aim         :learn Set,Dictionary,Tuple
#link(Github): https://github.com/Ashy09/python-Assignment

#following program for Set

#Que1:Write a python program to add members in a set and clear a set
set_01={'nisarg','jack','denial'}
set_01.add('messi')          #use add() function to add element
print(set_01)
set_01.clear()               #after use clear() function set is empty
print(set_01)


#Que2:Write a python program to remove item from a set if it's present in set
set_02={0,23,45,3,6}
set_02.remove(45)            #use remove() function to remove those element
print(set_02)                #after use print 0,3,6,23


#Que3:Write a python program to an intersection,Union,difference of set
set_31={0,1,2,4,6,8}          
set_32={1,3,5,7,9}            # (| for union.)(& for intersection.)(– for difference)
print("union: ",set_31|set_32)
print("intersection: ",set_31&set_32)
print("difference: ",set_31-set_32)


#Que4:Write a python program to fine maximun and minimum vaiue in set
set_04={2,4,46,78}
print(max(set_04))            #use max() function to find maximum number
print(min(set_04))            #use min() function to find minimum number


#Que5:Write a python program to find the most common elements their counts from list,tuple,dictionary
def most_frequent(List):
    return max(set(List), key = List.count)
 
List = [2, 1, 2, 2, 1, 3]
print(most_frequent(List))

