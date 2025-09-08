'''class, objects 
> Create class and show multilevel inheritance 
> Show overloading and overriding in python'''

'Multilevel inheritance'
# class animal1:
#     def dog (self):
#         print("dog berks")

# class animal2(animal1):
#     def cat (self):
#         print("cat meows")

# class animal(animal2):
#     def duck (self):
#         print("duck quack")

# animals = animal()

# animals.dog()
# animals.cat()
# animals.duck()        


'Overloading'
# class addition:
#     def __init__(self, a=0, b=0, c=0):
#         self.a = a
#         self.b = b
#         self.c = c
#         print (f"sum of {a} , {b} , {c} is {a+b+c}")

# obj = addition(9,4)
#or
# class addition:
#     def add(self, *args):
#         print("sum is =" , sum(args))

# obj = addition()
# obj.add(1,2,3,4,3,21,2)


'overriding'
# class Animal:
#     def speak(self):
#         print("animal sound")

# class DogSound(Animal):
#     def speak(self):
#         print("dog barks")

# animals = [Animal(), DogSound()]

# for a in animals:
#     a.speak()

''' 
 	
array, tuple, functions, dictionary
    > Remove even number and double odd number in array of random numbers using list comprehession.
        e.g.: [1,2,3,4,5,6,7,8,9] => [2,6,10,14,18]
    > Write a functions to convert tupple to list, list to set, set to tuple.
    > Write a function that will convert list inside list to dictionary
        e.g.: [['name', 'Deepak'], ['number', 23], ['class', '10th']] => {'name': 'Deepak', 'number': 23, 'class': '10th'}'''


'Remove even number and double odd number'
# a = [1,2,3,4,5,6,7,8,9] 
# b = [x * 2 for x in a if x%2 != 0]
# print(b)

'convert tupple to list, list to set, set to tuple'
# a = (1,"ram", 45, "priya")
# print(a)
# print(type(a))
# b = list(a)
# print(b)
# print(type(b))
# c = set(b)
# print(c)
# print(type(c))
# d = tuple(c)
# print(d)
# print(type(d))

'Write a function that will convert list inside list to dictionary'
# def list_inli_dict(listdict):
#     a = {}
#     for item in listdict:
#         if len(item) == 2:
#             a[item [0]] = item[1]
#     return a
# listdict = [['name', 'Deepak'], ['number', 23], ['class', '10th']]
# print(list_inli_dict(listdict))


'''
Pattern Question
input: 6
output:
            6
            5,6
            4,5,6
            3,4,5,6
            2,3,4,5,6
            1,2,3,4,5,6
            '''

# n = 6 
# for i in range(n,0,-1):

#     for j in range(i,n+1):
#         if i != j :
#             print(",",end='')
#         print(j, end='')


#     print()


''' 
 	
Searching and Sorting Problem: > Create a function that will sort the array of string based on the length of string. e.g.: ['deepak', 'aman', 'sam', 'naman', 'mohit'] => ['sam', 'aman', 'naman', 'mohit', 'deepak'] > use sorted, lambda function'''

# def len_sort(array_sort):
#     print (sorted(array_sort, key= lambda x : len (x)))

# array_sort = ['deepak', 'aman', 'sam', 'naman', 'mohit']
# len_sort(array_sort)


