import urllib.request

try:
    # define url
    url = "http://002-009-text-files.glitch.me/test-scores.txt"

    # initial request to URL
    response = urllib.request.urlopen(url)

    # read data from URL as string
    data = response.read().decode('utf-8')
except:
    print("Couldn't get data")
else:
    print("Data found")
    # print(data)

data = data.split("\n")

name = data[0]
score1 = float(data[1])
score2 = float(data[2])
score3 = float(data[3])

average = (score1 + score2 + score3)/3
print(name + "'s", "average score :", format(average, ".2f"))




