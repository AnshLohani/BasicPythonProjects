def flamescount(p1,p2):
    p1l = list(p1)
    p2l = list(p2)
    for i in p1l:
        for j in p2l:
            if i == j:
                p1l.remove(f"{i}")
                p2l.remove(f"{j}")
            else:
                continue
    flames = len(p1l) + len(p2l)
    return flames

p1 = input("Enter first name: ") 
p2 = input("Enter second name: ")
flame = ['F','L','A','M','E','S']
count = flamescount(p1,p2)

while len(flame)>1:
    flame.remove(flame[(count-len(flame)-1) % len(flame)])

'''
Point to remember: The logic of the flame.remove equation where we have taken the quotient of the eqn is because it ensures that the result 
is bounded by the bounds of the length of flame at that moment in the code.
'''

result = {
    'F': 'Friends',
    'L': 'Lovers',
    'A': 'Affectionate',
    'M': 'Marriage',
    'E': 'Enemies',
    'S': 'Siblings'
}

print("Your relationship status: ",f"{result[flame[0]]}")