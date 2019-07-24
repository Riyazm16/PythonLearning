from urllib.request import Request, urlopen

# contents = urllib.request.urlopen("https://www.udemy.com/").read()

runVar = True;

while True:
    # contents = urllib.request.urlopen("https://www.udemy.com/python-core-and-advanced/learn/lecture/8255406",headers={'User-Agent': 'Mozilla/5.0'}).read()

	req = Request("https://www.udemy.com/python-core-and-advanced/learn/lecture/8255406", headers={'User-Agent': 'Mozilla/5.0'})
	webpage = urlopen(req).read()
	print(webpage)