# PART 1
alpha = "abcdefghijklmnopqrstuvwxyz\n"
sum = 0
with open('./1/input.txt','r') as input:
    for line in input.readlines():
        sum += int(line.strip(alpha)[0]+line.strip(alpha)[-1])
print(sum)

# PART 2

digits = ["one","two","three","four","five","six","seven","eight","nine",'1','2','3','4','5','6','7','8','9']
digits_nums = ['1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9']
digit_dict = dict([(digits[i],digits_nums[i]) for i in range(len(digits))])

def text_to_digits(line):
    new_line = ""
    for i in range(len(line)):
        for digit in digits:
            if line[i:i+len(digit)] == digit:
                new_line += digit_dict[digit]
    return(new_line)

sum = 0
with open('./1/input.txt','r') as input:
    for line in input.readlines():
        line_to_digits = text_to_digits(line)
        sum += int(line_to_digits[0]+line_to_digits[-1])
print(sum)
