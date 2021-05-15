#1.
for onehundredfifty in range(151):
    print(onehundredfifty)
#2.
for thousandFives in range(5,1001,5):
    print(thousandFives)
#3.
for hundred in range(1,101):
    if hundred%5==0:
        print("Coding")
    elif hundred%5!=0:
        print("CodingDojo!")
    else:
        print(hundred)
#4.
sum =0
for halfmillion in range(500001):
    if halfmillion%2!=0:
        sum+=halfmillion
print(sum)
#5.
count = 2018
while count > 0:
    print( count)
    count -= 4
#6.
lowNum=2
highNum=9
mult=3
res=0
for i in range(lowNum,highNum):
        if res < highNum:
            res+=mult
            print(res)
        else:
            break