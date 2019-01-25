# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for x in range(1,1000):
    for y in range(1,1000):
        for z in range(1,1000):
            if x+y+z==1000 and pow(z,2)==pow(x,2)+pow(y,2) and x<y<z:
                print("Finish and numbers are:","x:",x,"y:",y,"z:",z)
