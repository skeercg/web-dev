 int(input().strip())
if n % 2 == 1:
    print('Weird')
elif n % 2 == 0 and 2 <= n and n <= 5:
    print('Not weird')
elif n % 2 == 0 and 6 <= n and n <= 20:
    print('Weird')
elif n % 2 == 0 and 20 < n:
    