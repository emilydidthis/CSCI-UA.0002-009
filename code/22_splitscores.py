scores = "95,100,67,33,88"

# splits scores into list of data
split_scores = scores.split(",")
print(split_scores)

# total number of scores
print("Total scores:", len(split_scores))

# convert list elements into numbers
for i in range(len(split_scores)):
    split_scores[i] = int(split_scores[i])
print(split_scores)

# average score
print("Average score:", sum(split_scores)/len(split_scores))

# highest and lowest scores
print("Highest score:", max(split_scores))
print("Lowest score:", min(split_scores))

# drop the lowest score
split_scores.remove(min(split_scores))
# new average
print("Average score:", sum(split_scores)/len(split_scores))
