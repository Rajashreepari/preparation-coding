def is_happynumber(num):
    seen = set()

    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))

    return num == 1

n=int(input("Enter number:"))
if is_happynumber(n):
    print(f"{n} is happy number 😊")
else:
    print(f"{n} is not happy number 😒")