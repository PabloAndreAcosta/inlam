# Anders N.
# funktioner
# medel(in1)
# input lista med tal
# output medelvärden av talet i listan

def medelvärde (a):
    sum = 0
    antal = len(a)
    for i in range (0,len(a)):
        sum = sum + a[i]
    return sum/len(a)
print(medelvärde([2,4,6,8]))