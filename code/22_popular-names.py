import urllib.request

try:
    # define url
    url = "http://002-009-text-files.glitch.me/girl-names.txt"

    # initial request to URL
    response = urllib.request.urlopen(url)

    # read data from URL as string
    data = response.read().decode('utf-8')
except:
    print("Couldn't get data")
else:
    print(data)

# ask user for name
name = input("Enter a name: ")

if name in data:
    print("Found", name, "in list of popular girl's names")
else:
    try:
        # define url
        url = "http://002-009-text-files.glitch.me/boy-names.txt"

        # initial request to URL
        response = urllib.request.urlopen(url)

        # read data from URL as string
        data = response.read().decode('utf-8')
    except:
        print("Couldn't get data")
    else:
        print(data)
        if name in data:
            print("Found!")
        else:
            print("Name not found")
            
        
