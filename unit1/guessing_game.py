lower = 0
upper = 100
my_guess = (upper - lower)/2
print(my_guess)
print("Hey! Select a number between 1 - 100")
num = int(input(">>>"))
print(num)
print(type(num))
while my_guess != num:
    print(my_guess)
    if my_guess > num:
        print("My guess is too high")
        upper = my_guess
        my_guess = (upper - lower)/2 + lower
    elif my_guess < num:
        print("My guess is too low")
        lower = my_guess
        my_guess = (upper - lower)/2 + lower
print("I got it! Your number is...")
print(my_guess)