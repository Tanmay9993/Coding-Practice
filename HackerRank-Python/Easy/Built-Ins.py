
### 1. Zipped


num_scores, records = map(int, input().split())
all_score = []
for i in range(0,records):
    values = list(map(float, input().split()))
    all_score.append(values)    

# Calculate Avg Method - 1
transpose= list(zip(*all_score))
for i in transpose:
    value = sum(i)/records
    print(value)


# Calculate Avg Method - 2
for i in range(0,num_scores):
    sums = 0
    for j in range(0, records):
        sums = sums + all_score[j][i]
    avg = round((sums/records),1)
    print(avg)


