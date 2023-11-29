import math

def median (a):
    sort_list = sorted(a)
    antal = len(sort_list)
    if antal % 2 == 0:
      # jämt antal element
      return (sort_list[antal/2-1] + sort_list[antal//2])/ 2
    else:
       # udda antal element
       return sort_list[antal//2]