def poly_add2(poly1, poly2):
   sum = [ ]
   sum.append(poly1[0] + poly2[0])
   sum.append(poly1[1] + poly2[1])
   sum.append(poly1[2] + poly2[2])
   return sum

def poly_mult2(p1, p2):
   print(p1)
   print(p2)
   deg0 = p1[0]*p2[0]
   deg1 = (p1[0]*p2[1]) + (p1[1]*p2[0])
   deg2 = (p1[0]*p2[2]) + (p1[1]*p2[1]) +(p1[2]*p2[0])
   deg3 = (p1[1]*p2[2]) + (p1[2]*p2[1])
   deg4 = p1[2]*p2[2]
   p3 = [deg0, deg1, deg2, deg3, deg4]
   print(p3)
   return p3


