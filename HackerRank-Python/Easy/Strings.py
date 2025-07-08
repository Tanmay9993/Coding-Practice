
# 1. sWAP
def swap_case(s):
    output = ""
    for i in s:
        if ord(i) >= 65 and ord(i) <= 90:
            output = output + (i.lower())
        else:
            output = output + (i.upper())
    return output


# 2. String Split and Join
def split_and_join(line):
    list_line = line.split(" ")
    output = "-".join(list_line)
    return output


# 3. What's your name
def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")


# 4. Mutation
def mutate_string(string, position, character):
    new_string = string[:position] + character + string[position+1:]
    return new_string

    
# 5. Find a string
def count_substring(string, sub_string):
    counter = 0
    for i in range(0,len(string)-len(sub_string)+1):
        if string[i:i+len(sub_string)] == sub_string:
            counter = counter + 1
    return counter


# 6. String Validators
if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))    # Alphanumeric
    print(any(c.isalpha() for c in s))    # Alphabetical
    print(any(c.isdigit() for c in s))    # Digits
    print(any(c.islower() for c in s))    # Lowercase
    print(any(c.isupper() for c in s))    # Uppercase
