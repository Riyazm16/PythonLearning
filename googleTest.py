import  urllib.request

contents = urllib.request.urlopen("https://www.google.com/").read()

runVar = True;

while True:
    contents = urllib.request.urlopen("https://www.google.com/").read()
    print(contents)