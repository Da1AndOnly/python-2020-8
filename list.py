a = int(input("Whole class population:"))
list_score = []
name = []
for i in range(a):
    name_input = input('put your name here:')
    score = int(input())
    if score not in list_score:
        list_score.append(score)
        name.append(name_input)
sum_score = sum(list_score)
print("class average:",sum_score/a)
highest = 0
lowest = 100
for n in range(a):
    if list_score[n] > highest:
        highest = list_score[n]
        high_name = name[n]
print("Highest",highest,high_name)
for n in range(a):
    if list_score[n] < lowest:
        lowest = list_score[n]
        low_name = name[n]
 
print("lowest",lowest,low_name)





















































































































































































































































































