

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
students[0].first_name = "Bryant"
#    In the sports_directory, change 'Messi' to 'Andres'
sports_directory["soccer"][0] = "Andres"
#    Change the value 20 in z to 30
z[0]['y'] = 30
print(x,students,sports_directory,z)



#    2. Iterate Through a List of Dictionaries	

#    3. Get Values From a List of Dictionaries	

#    4. Iterate Through a Dictionary with List Values	