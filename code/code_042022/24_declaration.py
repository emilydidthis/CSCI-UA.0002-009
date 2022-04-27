import urllib.request

try:
    # define url
    url = "http://002-009-text-files.glitch.me/declaration.txt"

    # initial request to URL
    response = urllib.request.urlopen(url)

    # read data from URL as string
    data = response.read().decode("utf-8")
except:
    print("Couldn't get data")
else:
    print("Data found")
    #print(data)

# replace new lines with spaces
data = data.replace("\n", " ")

# essentailly delete punctuation  
data = data.replace(",", "")
data = data.replace(";", "")
data = data.replace(".", "")
data = data.split(" ")
print(data)

words = {}

for w in data:
    if w.lower() in words.keys():
        words[w.lower()] += 1
    else:
        words[w.lower()] = 1

print(words)
print(max(words, key=words.get))
