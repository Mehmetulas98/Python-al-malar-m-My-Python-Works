#with this codes,we can find the sum of all multiples below number we want
#for example=  mainnumer=10  multiplenumber=2 and 1.multiple 3 and 2.multiple 5.we find
#3,5,6, and 9.Sum of these numbers is 23.


mainnumber=int(input("Enter main number:"))
multiplenumber=int(input("How many do you want multiple?:"))
total=0
while True:
    multiple=int(input("please enter multiple(For Exit Enter '0'):"))
    if(multiple>0):
        for i in range(1,mainnumber-1):
            if(multiple*i<mainnumber):
                a=i*multiple
                total+=a
            else:
                pass
    else:
        break
print(total)