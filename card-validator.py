def check(card_number):
    '''
    Takes a single positive integer and returns True is it is a valid credit card number and returns False if not.
    '''
    card_number_str = str(card_number)
    start_even = (card_number_str[-1::-2])
    sum_even = 0
    for x in start_even:
        sum_even += int(x)
    start_odd = (card_number_str[-2::-2])
    odd_digits = ""
    sum_odd = 0
    for x in start_odd:
        doubled = int(x) * 2
        doubled_str = str(doubled)
        odd_digits += doubled_str
    start_doubled_odd = (odd_digits[::])
    for x in start_doubled_odd:
        sum_odd += int(x)
    total = sum_even + sum_odd
    if total % 10 == 0:
        return total
