#In python 2 we can do divsion as following
a = 4.0/2
print(a)

#In Python 3 we can do division as following
b = 4/2
print(b)

#In python 2 syntax for print is as following
#print 'Hello World'

#in Python 3 syntax for print is as following
print("Hello World")
#Python 2 supports ASCII whereas Python 3 supports unicode
#In Python 2 Unicode and str are different whereas in python 3 unicode and str are same
print(type('default string'))
print(type(b'string with b'))

#in python 2 rang() and xrange is used
for x in range(1, 5):
    print(x)
#whereas in Python 3 only range is used

#for x in xrange(1, 5):
#print(x)

#Local Namespace and global namespace std
c = 45
#The above value is global varriable and namespace
def my_function(d = 54):
    print(d)
    
#Indentation
site = 'Tell'
if site == 'Tell':
    print("The Word is correct")
else:
    print("Incorrect")
print("All set.")

#Comment
#This is single line comment
"""This is multi line comment
    This is used for long paragraph of comment
"""