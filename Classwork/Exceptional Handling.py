'''
Exceptional handling:

compliner errors:when we get error while compling
runtime errors: the errors occured after running the progrm (ex: name error, type error, index error,value error,key error)
exceptional error: we use it to handle all the errors(runtime errors)

'''
try: # --- when we expect an error use try before the code - it exits and go's to exception instead of throwing an error
    a=10
    a=a+10
    l=[1,3,4]
    k=l[7]
except NameError:
    print("a is not defined")
except IndexError:
    print("You have entered the out of range value")

# Key error:

try:
    a=10
    a=a+10
    l=[1,2,3]
    k=l[7]
    d={1:2,2:4,3:9}
    print(d[4])
except NameError:
    print("a is not defined")
except IndexError:
    print("You have entered the out of range value")
except KeyError:
    print("key is not present")

# Value Error:

try:
    a=10
    a=a+10
    l=[1,3,4]
    k=l[2]
    d={1:2,2:4,3:9}
    print(d[4])
    b=int(input("Enter a number: "))
    print(b)

except NameError:
    print("a is not defined")
except IndexError:
    print("You have entered the out of range value")
except KeyError:
    print("key is not present")
except ValueError:
    print("Enter the proper data value")


# Type Error:

try:
    a=10
    a=a+10
    l=[1,3,4]
    k=l[2]
    d={1:2,2:4,3:9}
    print(d[4])
    b=int(input("Enter a number: "))
    print(b)
    c=1+"1"

except NameError:
    print("a is not defined")
except IndexError:
    print("You have entered the out of range value")
except KeyError:
    print("key is not present")
except ValueError:
    print("Enter the proper data value")
except TypeError:
    print("you can't add 2 diff types")

# we can write except in line line code:

try:
    a=10
    a=a+10
    l=[1,3,4]
    k=l[2]
    d={1:2,2:4,3:9}
    print(d[4])
    b=int(input("Enter a number: "))
    print(b)
    c=1+"1"

except (NameError, IndexError, KeyError, ValueError, TypeError) as e:
    print(f"Error occured: {e}")
    #  or #
'''
except Exception as e:  (it handles all run time errors when we cann't predict what errors will occure)
    print(f"Error occured: {e}")

'''
# Else:

try:
    a=10
    a=a+10
    l=[1,3,4]
    k=l[2]
    d={1:2,2:4,3:9}
    print(d[4])
    b=int(input("Enter a number: "))
    print(b)
    c=1+"1"

except Exception as e: 
    print(f"Error occured: {e}")
else: # else block occurs whenever their is no error
    print("No errors")
    print(c)

# Finally Key word:

try:
    a=10
    a=a+10
    l=[1,3,4]
    k=l[2]
    d={1:2,2:4,3:9}
    print(d[2])
    b=int(input("Enter a number: "))
    print(b)
    c=1+12

except Exception as e: 
    print(f"Error occured: {e}")
else: # else block occurs whenever their is no error
    print("No errors")
finally: # it's gonna be executed defaultly even when we have errors or no errors
    print(" code executed ")

# Raise Key word : raises an error explicitly
try:
    amount= int(input("Enter the amount "))
    if amount<0:
        raise ValueError("Enter the posistive value")
except Exception as e:
    print(f"Error occured: {e}")
else: 
    print("No errors")
    print("You can withdraw")
finally:
    print("------Remove your card-------")

