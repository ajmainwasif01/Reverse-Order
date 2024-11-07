
def count_digits(number):
    count = 0
    while number != 0:
        number //= 10  
        count += 1     
    return count
number = int(input("Enter a number: "))

if number == 0:
    print("The number has 1 digit.")
else:
    digit_count = number  
    print("The total number of digits in the number is:" , digit_count)
