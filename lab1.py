import requests
response = requests.get("https://github.com/JuliusSneezer/CMPUT404/raw/master/lab1.py")
print response.text
