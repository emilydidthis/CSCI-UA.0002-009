import urllib.request

try:
    # define url
    url = "http://002-009-text-files.glitch.me/world-series.txt"

    # initial request to URL
    response = urllib.request.urlopen(url)

    # read data from URL as string
    data = response.read().decode('utf-8')
except:
    print("Couldn't get data")
else:
    print("Data found")

# Step 1: Split the data into a list
# Step 2: Create just a list of teams
# Step 3: Count occurrences of each time in data list --> create a new list of win numbers
# Step 4: Find the max number of wins in win list
# Step 5: Use that index and find the matching winning team


data = data.split("\n")
#print(data)

teams_only = []

for t in data:
    if t in teams_only:
        continue
    else:
        teams_only.append(t)

print(teams_only)

win_counts = []
for t in teams_only:
    wins = data.count(t)
    win_counts.append(wins)
print(win_counts)

most_wins_index = win_counts.index(max(win_counts))
print(most_wins_index)

winner = teams_only[most_wins_index]
print("World Series champ:", winner)

