import urllib.request as req

openURL = req.urlopen("https://www.google.com/")
print(openURL.read()) # read source code

