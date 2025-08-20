'''
# OOP's Concepts:

whenever we want to see the outputs different from user to user(object).Based on the user we need to define the function
 to reuse the code when we have to enhance the code
 (to see data vary from user to user)

# Drawbacks in procedural and characteristics in oops to switch to oops: #

1) Encapsulation : to restrict few variables/info
2) Abstarctions : Hiding the complex data, ex: when we have the file/image more than the fixed nd the it actomaticaly reduces the size were we can see diff in quality.it hides this thing 
3) Inheritance : when we want the properties of child class/parent class.to reuse the code 
4) Polymorphism : same method with diff functions(actions)
      ex: hotstart/utube premium and no premium account

# Features: #

1) Modularity 
2) Maintaince
3) scalability

# this is the reason that we switch to oops concepts from Procedural 

- oops is going to be run on objects and classes
- no need to rewrite the code
- we can reuse the code in diff platforms
- easier to manage and organize the code
- through encapsulation we can restrict the access to data 

1) Class : is a combination of Attributes and methods
           1) Attributes - data,varibles,properties
           2) Methods - functions

we use 'Class' to define a class
      ex: Class Instagram:

2) objects - the people who are using class are objects (Instance of class)
      ex: vaishnavi = Instagram()
          taruni = Instagram()

# defing a function: #
     
    class Instagram:
        def addingUsername(self,username):  --
            print("{username} is added") ----- this thing is method(blueprint/function)
        def uploadPost(self,posturl):
            print(f"Added the {posturl}")
    vaishnavi = Instagram()
    lakshmi = Instagram()
    taruni = Instagram()
    
    vaishnavi.addUsername("Vaishnavi")
    taruni.addUsername("taruni")

    vaishnavi.uploadPost("Vaishnavi","asdsd.png")
    lakshmi.uploadPost("taruni","adssd.png")

# How can the function/blueprint knows who called that function(who is adding the th username) - bcz of the self

self - - we need to use the self key word to reflect/to point to the current object
self is not a key word we can write anything instead of self (ex: abc) but mostly we use self key word

# Attributes : #

1) Class Attributes: The attributes which are defined by a class.fixed data/fixed calls are called class attribues

 class Shopping:
    discount=10
    cat=['men','women','skincare','footware']

2)Instant Attributes: The attributes coming from the objectsare called as Instance asttribues.data varies from user to user.It is defined from the user.
 Ex: when user defines diff products 
     
 class Shopping:
    discount=10
    cat=['men','women','skincare','footware']

     def placeorder(self,product):
        self.product=product

# Methods: #

1)Instat Methods: Any method working on the instant attribute/data.
   - in intant method we no need to mention any decorator.we define it with regular def 
   - when we have instant method we cann't access other thinggs in other methods
 
    def placeorder(self,product):
        self.product=product

2)Class Methods: whenever the method deals with the class attributes/change/modify then it's called class method. 

    @classmethod ----(these are called decorators)
    def updatediscount(cls,upd_dis):
        cls.discount=upd_dis

3)Static Method: whenever we need to do utility operations(helper function for formatting) we go with static methods.

    @staticmethod
    def formatdiscount(discount):
        print(f"{discount}% discount is available.shop now!!")


# How to access these methods: #

- Class Method: with the help of class method we can access with the methods.
we can also access it with the object name -- but not recommended

- Instant Method: only instant name/only object can access the instant method

- Static Method: 

class Shopping:
    discount=10
    cat=['men','women','skincare','footware']

def placeorder(self,product):
    self.product=product
@classmethod ----(these are called decorators)
    def updatediscount(cls,upd_dis):
        cls.discount=upd_dis

@staticmethod
    def formatdiscount(discount):
        print(f"{discount}% discount is available.shop now!!")

'''

