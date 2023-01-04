def interval_even_numbers(num1, num2):
    INTERVAL_NUMB = list(range(num1, int(num2+1)))
    print(sum([i for i in INTERVAL_NUMB if i % 2 ==0]))

interval_even_numbers(1, 4)
