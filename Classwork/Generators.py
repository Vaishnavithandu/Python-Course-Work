# Generators

# -memory efficiency
# -to save the memory we are switching from functions to generators
# - we don't have a return value we have a yield keyword
# - yield: untill an unless my sequence is don eit's going to show all the seq.
# - yield doesn't stop iterating it shows the 1st output,then when we call next(variable) it gives all other output
# by pausing the output after giving one output.

'''
def show_feed(l):
    for i in l:
        yield i
reels=['1...100','101...200','201...300','301...400','401...500']
nextfeed=show_feed(reels)
  # |
# variable
print(next(nextfeed))
print(next(nextfeed))
print(next(nextfeed))
print(next(nextfeed))
print(next(nextfeed))

# the main code:

def show_feed(l):
    for i in l:
        yield i
reels=['1...100','101...200','201...300','301...400','401...500','501...600','601..700','701...800','801...900','901...1000']
nextfeed=show_feed(reels)
  # |
# variable

while True:
    scroll=input("[c]ontinue / [e]xit")
    if scroll=='c':
        print(next(nextfeed))
    else:
        break
'''

#
def show_feed(l):
    for i in l:
        start,end=i.split('...')
        reelssofi={f'{i}-[like],[share],[comment]' for i in range(int(start),int(end))}
        yield i
reels=['1...100','101...200','201...300','301...400','401...500','501...600','601..700','701...800','801...900','901...1000']
nextfeed=show_feed(reels)
  # |
# variable

while True:
    scroll=input("[c]ontinue / [e]xit")
    if scroll=='c':
        print(next(nextfeed))
    else:
        break