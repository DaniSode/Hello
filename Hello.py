print("Write 3 integers with the: \n")

ye = input().split(" ")
X = int(ye[0])
Y = int(ye[1])
N = int(ye[2])
aa = range(1, N+1)
for c in aa:

    if c % X == 0 and c % Y == 0:
        print("FizzBuzz")
    elif c % X == 0:
        print("Fizz")
    elif c % Y == 0:
        print("Buzz")

    elif c % X != 0 and c % Y != 0:
        print(c)
print(Yeay)