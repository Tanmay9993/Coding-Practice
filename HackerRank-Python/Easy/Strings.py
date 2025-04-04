
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


# 4. 
