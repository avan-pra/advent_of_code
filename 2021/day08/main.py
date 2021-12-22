fd = open('./data', 'r')

def parse_line(line: str):
    digits_str, result_str = line.strip('\n').split('|')

    digits = [tuple(sorted(c)) for c in digits_str.split(' ')]
    result = [tuple(sorted(c)) for c in result_str.split(' ')]

    return digits, result

def find_by_number_of_segments(digits, number):
    ret = []
    for digit in digits:
        if len(digit) == number:
            ret.append(digit)
    return ret

def digit_in_segment(digit, digit2):
    return all(item in digit for item in digit2)

def find_one(digits):
    return find_by_number_of_segments(digits, 2)[0]

def find_four(digits):
    return find_by_number_of_segments(digits, 4)[0]

def find_seven(digits):
    return find_by_number_of_segments(digits, 3)[0]

def find_eight(digits):
    return find_by_number_of_segments(digits, 7)[0]

def find_three(digits, one):
    for digit in find_by_number_of_segments(digits, 5):
        if digit_in_segment(digit, one):
            return digit

def find_nine(digits, three):
    for digit in find_by_number_of_segments(digits, 6):
        if digit_in_segment(digit, three):
            return digit

def find_zero_six(digits, one, nine):
    for digit in find_by_number_of_segments(digits, 6):
        if digit != nine: # because nine also has 6 segments
            if digit_in_segment(digit, one):
                zero = digit
            else:
                six = digit
    return zero, six

def find_two_five(digits, six, three):
    for digit in find_by_number_of_segments(digits, 5):
        if digit != three: # because three also has 5 segments
            if digit_in_segment(six, digit): # reverse has digit
                five = digit
            else:
                two = digit
    return two, five


solution = 0
for line in fd:
    digits, result = parse_line(line)
    
    one = find_one(digits)
    four = find_four(digits)
    seven = find_seven(digits)
    eight = find_eight(digits)
    three = find_three(digits, one)
    nine = find_nine(digits, three)
    zero, six = find_zero_six(digits, one, nine)
    two, five = find_two_five(digits, six, three)

    compare = {
        zero: '0',
        one: '1',
        two: '2',
        three: '3',
        four: '4',
        five: '5',
        six: '6',
        seven: '7',
        eight: '8',
        nine: '9'
    }
    for test_digit in result:
        out = ''
        if test_digit != ():
            if compare[test_digit] == '1' or compare[test_digit] == '4' or compare[test_digit] == '7' or compare[test_digit] == '8':
                solution += 1
print(solution)
