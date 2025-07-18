# 1. Runner-Up Score
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_list = list(set(arr))
    arr_list.sort()
    print(arr_list[-2])


# 2. Nested List
if __name__ == '__main__':
    
    # Build nested list
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        
    # Get unique score and secon lowest
    all_scores = sorted(set([score for name, score in students]))
    second_lowest_score = all_scores[1]

    # Get names who have second highest score
    second_lowest_name = [name for name, score in students if score == second_lowest_score]
    
    # Sort and print
    second_lowest_name.sort()
    for i in second_lowest_name:
        print(i)

if __name__ == '__main__':
    name_list = []
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        name_list.append(name)
        score_list.append(score)
        
    name_score_pair = list(zip(score_list,name_list))
    
    score_val = list(set(score_list))
    score_val.sort()
    second_num = score_val[1]
    
    get_second = [name for score, name in name_score_pair if score == second_num]
    get_second.sort()
    
    for name in get_second:
        print(name)
    

# 3. Find the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    
    # Take Input
    for _ in range(n):
        name, *line = input().split()        #  "John 78 89 90" → splits into ['John', '78', '89', '90'] ;  name, *line unpacks: name = 'John' and line = ['78', '89', '90']
        scores = list(map(float, line))      #  map(float, line) converts the score strings to floats.
        student_marks[name] = scores         #  student_marks['John'] = [78.0, 89.0, 90.0]
    query_name = input()
    
    # Calculate Avg
    scores = student_marks[query_name]
    average = sum(scores) / len(scores)
    print(f"{average:.2f}")
       

# 4. Lists
if __name__ == '__main__':
    N = int(input())
    output = []
    
    for _ in range(N):
        command = input().split()
        action = command[0]
        
        if action == 'insert':
            i = int(command[1])
            e = int(command[2])
            output.insert(i,e)
        elif action == 'print':
            print(output)
        elif action == 'remove':
            e = int(command[1])
            output.remove(e)
        elif action == 'append':
            e = int(command[1])
            output.append(e)
        elif action == 'sort':
            output.sort()
        elif action == 'pop':
            output.pop()
        elif action == 'reverse':
            output.reverse()
        else:
            pass
            

# 5. Tuple
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    value = hash(tuple(integer_list))
    print(value)


# 6. List Comprehension
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    # Generate all possible [i, j, k] combinations where 0 ≤ i ≤ x, 0 ≤ j ≤ y, 0 ≤ k ≤ z
    # Include only those where the sum i + j + k is not equal to n
    result = [[i, j, k] 
              for i in range(x + 1) 
              for j in range(y + 1) 
              for k in range(z + 1) 
              if (i + j + k) != n]

    print(result)


