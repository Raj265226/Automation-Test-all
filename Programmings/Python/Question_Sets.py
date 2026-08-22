#1 Use lambda and List comprehension and also make it for even only - my_list = [1,2,3,4,5]
my_list = [1,2,3,4,5]
print('Use lambda :', list(map(lambda x:x**2, filter(lambda x:x%2 == 0, my_list))))
print('Use List Comprehension ', [x**2 for x in my_list if x%2 == 0])

#2 Highest and Lowest number with second one - x = [78,89,22,90,55,23]
x = [78,89,22,90,55,23]
highest_number = 0
second_highest_number = 0
lowest_number = x[0]
second_lowest_number = float('inf')

for i in x:
    if i > highest_number:
        second_highest_number = highest_number
        highest_number = i
    elif i > second_highest_number and i != highest_number:
        second_highest_number = i
print('Highest and 2nd Highest numbers are ', highest_number, second_highest_number)

for i in x:
    if i < lowest_number:
        second_lowest_number = lowest_number
        lowest_number = i
    elif i < second_lowest_number and i != lowest_number:
        second_lowest_number = i
print('Lowest and 2nd lowest numbers are ', lowest_number, second_lowest_number)

#3 Prime number check
def prime(num):
    is_Prime = True
    if num <= 1:
        is_Prime = False
    for i in range(2, num):
        if num % i == 0:
            is_Prime = False
    if is_Prime:
        print('Prime')
    else:
        print('Not Prime')
prime(int(input('Enter number ')))

#4 Prime number check between numbers
def prime(num):
    is_Prime = True
    if num <= 1:
        is_Prime = False
    for i in range(2, num):
        if num % i == 0:
            is_Prime = False
    if is_Prime:
        return num

def prime_between(n1, n2):
    y = []
    for i in range(n1, n2+1):
        if prime(i):
            y.append(i)
    print('Prime numbers are ', y)
prime_between(int(input('Enter start number ')),int(input('Enter end number ')))

#5 Permutations of string
def permutation(string, current=''):
    if len(string) == 0:
        print(current)
    for i in string:
        new_string = string.replace(i, '', 1)
        permutation(new_string, current+i)
permutation(input('Enter string '))

#6 Input = 'aaaaabbbbcccdddd' output = 'a5b4c3d4'
input = 'aaaaabbbbcccdddd'
count = 1
output = ''
for i in range(len(input)-1):
    if input[i] == input[i+1]:
        count += 1
    else:
        output += input[i] + str(count)
        count = 1
output += input[-1] + str(count)
print('output ', output)


#7 Input = 'a5b4c3d4' output = 'aaaaabbbbcccdddd'
input = 'a5b4c3d4'
output = ''
for i in range(0, len(input), 2):
    output += input[i] + str(int(input[i+1]))
print('output ', output)

#8 Fibonacci
def fib(num):
    if num <= 1:
        return num
    else:
        return fib(num-1) + fib(num-2)
print('fibonacci ', [fib(i) for i in range(10)])

#9 Anagram
words = ['listen', 'enlist', 'silent', 'banana', 'apple', 'papel']
anagram_dict = {}
for word in words:
    sorted_word = ''.join(sorted(word))
    if sorted_word in anagram_dict:
        anagram_dict[sorted_word].append(word)
    else:
        anagram_dict[sorted_word] = [word]
print('Output using values ', [ana for ana in anagram_dict.values()])
output = []
for k, v in anagram_dict.items():
    output.append(v)
print('Output using items ', output)

#10 Reverse the firstname input - 'Rohit Santra' output - 'tihoR Santra'
input = 'Rohit Santra'
output = ''
for i in input.split():
    if output == '':
        output += i[::-1]
    else:
        output += ' ' + i
print('Output using space ', output)

reverse = ''
remain = ''
is_space_found = False
for i in input:
    if not is_space_found:
        if i == ' ':
            is_space_found = True
            remain += i
        else:
            reverse = i + reverse
    else:
        remain += i
print('Without inbuilt', reverse + remain)

#11 list of repeat number input - [4,3,6,2,3,1,4] output - [4,3]
input = [4,3,6,2,3,1,4]
output = []
for i in input:
    if input.count(i) > 1 and i not in output:
        output.append(i)
print(output)

#12 input - [1,2,3,4,5,6,7,8,9,10] output - sets of number equal to 15
input = [1,2,3,4,5,6,7,8,9,10]
output = []
sum = 15
for i in range(len(input)):
    for j in range(i+1, len(input)):
        if input[i] + input[j] == sum:
            output.append((input[i], input[j]))
print(output)

#13 armstrong
def arms(num):
    sum = 0
    for i in num:
        sum += int(i)**3
    if sum == int(num):
        print('Armstrong')
    else:
        print('Not armstrong')
arms(input('Enter num '))

#14 x = 'madam' output - repeated 'ma', nonrepeated - 'd', count = {'m': 2, 'a': 2, 'd': 1}
x = 'madam'
repeated = ''
nonrepeated = ''
dict_form = {}
for i in x:
    if x.count(i) > 1 and i not in repeated:
        repeated += i
print('repeated strings ', repeated)

for i in x:
    if x.count(i) == 1 and i not in nonrepeated:
        nonrepeated += i
print('nonrepeated strings ', nonrepeated)

for i in x:
    if i in dict_form:
        dict_form[i] += 1
    else:
        dict_form[i] = 1
print(f'dict form of word {x} - ', dict_form)

#15 Print **** *** ** * and **** *** **** ***
for i in range(4):
    if i % 2 == 0:
        print('****')
    else:
        print('***')

for i in range(4, 0, -1):
    print('*' * i)

#16 input = ['Art Int', 'Test Auto', 'Roh Kum San']
# output = ['AI', 'TA', 'RKS']
input = ['Art Int', 'Test Auto', 'Roh Kum San']
output = []
print('List comprehension index ',[''.join(j[0] for j in x.split()) for x in input])
print('List comprehension upper ',[''.join(j for j in x if j.isupper()) for x in input])

for i in input:
    first_letter = ''
    for j in i.split():
        first_letter += j[0]
    output.append(first_letter)
print('Using first_letter ', output)

#17 emails = ['test@xyz.com', 'test2@abc.com'] , domains = ['xyz.com', 'abc.com']
emails = ['test@xyz.com', 'test2@abc.com']
domains = []
for email in emails:
    domains.append(email.split('@')[1])
print(domains)

#18 input = 'the dog roaming at night time' , output - largest word / roaming
input = 'the dog roaming at night time'
largest_word = ''
for i in input.split():
    if len(i) > len(largest_word):
        largest_word = i
print('largest_word - ', largest_word)

#19 input = [2,3,3,5,3,1] , use bubble sort and inbuilt method
numbers = [2,3,3,5,3,1]
print('In-built method ', sorted(numbers))
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print('Without in-built method ', numbers)

#20 words = ["apple", "ant", "banana", "ball", "cat"] , output = {'a': ['apple', 'ant'], ...}
words = ["apple", "ant", "banana", "ball", "cat"]
dict_form = {}
for word in words:
    if word[0] in dict_form:
        dict_form[word[0]].append(word)
    else:
        dict_form[word[0]] = [word]
print(dict_form)

#21 input = "Rohit123@Santra#2026!" , 
# output -> Alphabets: RohitSantra, Nos: 1232026, Spl_characters: @#!
input = "Rohit123@Santra#2026!"
Alphabets = ''
Numbers = ''
Special_characters = ''
for i in input:
    if i.isalpha():
        Alphabets += i
    elif i.isdigit():
        Numbers += i
    else:
        Special_characters += i
print('Alphabets :', Alphabets)
print('Numbers :', Numbers)
print('Special_characters :', Special_characters)

output = ""
for i in input:
    if i.isalnum():
        output += i
print(output)

#22 find largest and smallest number in array
# x = [78,89,22,90,55,23]
x = [78,89,22,90,55,23]
highest_number = 0
lowest_number = x[0]
for i in x:
    if i > highest_number:
        highest_number = i
    if i < lowest_number:
        lowest_number = i
print('highest_number', highest_number)
print('lowest_number', lowest_number)

#23.1 reverse array program 1
# Input: [1, 2, 3, 4, 5] , Output: [5, 4, 3, 2, 1]
#23.2 reverse array program 2
# Input: ["Rohit", "Santra", "QE"] , Output: ["QE", "Santra", "Rohit"]
input1 = [1, 2, 3, 4, 5]
input2 = ["Rohit", "Santra", "QE"]
output1 = []
output2 = []
for i in range(len(input1) - 1, -1, -1):
    output1.append(input1[i])
print(output1)

for i in range(len(input2) - 1, -1, -1):
    output2.append(input2[i])
print(output2)

#24 Input - "hello" , output1 - "olh" , output2 - "o*l*l*e*h*"
x = "hello"
output1 = ''
output2 = ''
for i in range(len(x) - 1, -1, -2):
    output1 += x[i]
print(output1)

for i in x:
    output2 = i + '*' + output2
print(output2)

#25. sum of alternative number
sum = 0
for i in range(1, 6):
    if i % 2 != 0:
        sum += i
print(sum)

# Ignore - Print duplicate elements of given String
# {"abc", "xyz", "avf", "vgy", "vgy", "rty"} , this is for java only

#26 Write a java program to find given String is palindrome or not , "madam" "12121"
y = "12121"
z = "madam"
def pal(x):
    if x == x[::-1]:
        return 'palindrome'
    else:
        return 'Not palindrome'
print('number-', pal(y))
print('string-', pal(z))

#27 Input: learn java programming
# Output: {'a': 4, 'r': 3, 'n': 2, 'g': 2, 'm': 2}
input = "learn java programming"
input = input.replace(' ', '')
output = {}
for i in input:
    if input.count(i) > 1 and i not in output:
        output[i] = input.count(i)
print(output)

#28 Input = "My Name is Jaya, and my role is to check quality"
# o/p = "quality kcehc ot si elor ym dna ayaJ si emaN yM"
Input = "My Name is Jaya, and my role is to check quality"
Input = Input.replace(',', '').split()
output1 = ""
output2 = []
for i in range(len(Input)):
    if i % 2 == 0:
        output1 = Input[i] + ' ' + output1
    else:
        output1 = Input[i][::-1] + ' ' + output1
print('output 1 ', output1)

for i in range(len(Input)):
    if i % 2 == 0:
        output2.append(Input[i])
    else:
        output2.append(Input[i][::-1])
print('output 2 ', ' '.join(output2[::-1]))

#29 Find the subset
# a1 = {1,2,3,2,1}, a2 = {1,2,3}
# a1 = {78,79}, a2 = {78,23,3,6,79}
# a1 = {9,11}, a2 = {78,23,3,6,79}

def subset_check(a1, a2):
    if set(a1).issubset(set(a2)) == True:
        print('a1 is the subset of a2')
    else:
        print('a1 is not the subset of a2')
    if set(a2).issubset(set(a1)) == True:
        print('a2 is the subset of a1')
    else:
        print('a2 is not the subset of a1')
a1 = {78, 79}
a2 = {78, 23, 3, 6, 79}
subset_check(a1, a2)

#30 input = "Online Java" , output = enilnO avaJ
input = "Online Java"
output = ""
for i in input.split():
    output += ' ' + i[::-1]
print(output)

#31 denominations = 500, 100, 50, 20, 10, 1
# If the user enters 951 , output = 500*1=500 100*4=400 50*1=50 1*1=1
def price(num):
    denominations = [500, 100, 50, 20, 10, 1]
    for note in denominations:
        if num >= note:
            count = num // note
            print(f'{note}*{count} = {note * count}')
            num = num % note  # update remaining amount
price(951)