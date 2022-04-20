import urllib.request

try:
    # define url
    url = "http://002-009-text-files.glitch.me/declaration.txt"

    # initial request to URL
    response = urllib.request.urlopen(url)

    # read data from URL as string
    data = response.read().decode('utf-8')
except:
    print("Couldn't get data")
else:
    print("Data found")

data = data.replace("\n", " ")
data = data.split(" ")
words = {}

for w in data:
    if w in words.keys():
        words[w] += 1
    else:
        words[w] = 1

print(words)
print(max(words, key=words.get))
