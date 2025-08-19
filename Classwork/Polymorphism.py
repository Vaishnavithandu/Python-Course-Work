'''
Polymorphism :
1) method overloading : same method diff parameters (we don't have a concept of overloading in python)
2) Method over rinding : same name diff 

'''

class NormalUser:
    def __init__(self,username):
        self.username=username
        print(f'\n Welcome to YouTube\n {self.username} account is created')
    def playvideo(self):
        print("Ads Included")
        print("No Background play")
        print("Limited Content")
        print("Download with low quality")
        print("No YT Music")
    def profile(self):
        print("you can upload your profile")
    def multipleDevice(self):
        print("You can upload your profile")
    def MultipleDevice(self):
        print("You can login with different devices")
    def Shorts(self):
        print("You can see YT shorts")
    def Likes(self):
        print("Likes")
    def Comments(Self):
        print("Comments")
    def Share(self):
        print("Share")
    def Subscribe(self):
        print("Subscribe")


class PremiumUser(NormalUser):
    def __init__(self, username):
        super().__init__(username)
    def playvideo(self):
        print("Ads Free")
        print("You can play on Background")
        print("Exclusive Content")
        print("Download with high quality")
        print("Yt Music is available")

vaishnavi = NormalUser("Vaishnavi")
vaishnavi.playvideo()
vaishnavi.profile()
vaishnavi.MultipleDevice()
vaishnavi.Shorts()
vaishnavi.Likes()
vaishnavi.Comments()
vaishnavi.Share()

 # 1) OPerator Overloading:

class Number:
    def __init__(self,number):
        self.number=number
    def _add_(self,other):
        return self.number+other.number
    def __str__(self):
        return f'{self.number}'
    def _sub_(self,other):
        return self.number-other.number
    def __eq__(self, other):
        return self.number==other.number
    def _gt_(self,other):
        return self.number>other.number
    def _lt_(self,other):
        return self.number<other.number
    def _truediv_(self,other):
        return self.number/other.number

n1=Number(10)
n2=Number(20)

print(n1+n2) # error - we cann't add the two objects.
# To add/to perform any operations on objects we use overloading and overriding concepts

print(n1)
print(n1-n2)
print(n1==n2)
print(n1>n2)
print(n1<n2)
print(n1/n2)

