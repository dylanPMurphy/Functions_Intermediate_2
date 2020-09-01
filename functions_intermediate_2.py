

# 1. Update Values in Dictionaries and Lists	
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


#    Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
#   Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = "Bryant"
#    In the sports_directory, change 'Messi' to 'Andres'
sports_directory["soccer"][0] = "Andres"
#    Change the value 20 in z to 30
z[0]['y'] = 30
print(x,students,sports_directory,z)



#    2. Iterate Through a List of Dictionaries	Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(input_dict):
    for i in range(0, len(input_dict)): 
        for x, y in input_dict[i].items():
            print(x,y)


iterateDictionary(students)
#    3. Get Values From a List of Dictionaries	

def iterateDictionary2(key_value,input_dict):
    for i in range(0, len(input_dict)): 
        print(input_dict[i][key_value])

iterateDictionary2("first_name", students)


#    4. Iterate Through a Dictionary with List Values	
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(input_dict):
    
printInfo(dojo)