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


# 3. 
       




