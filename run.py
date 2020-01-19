import requests
import urllib.parse
from googlesearch import search

search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"
subscription_key = "31ee3ab950c7497db8275830a30a7e0c"
assert subscription_key

print("Welcome to Seach Engine Dorker!!!")
print("Select the search engine...")
print("1. Bing")
print("2. Google")
choice = int(input("Choice: "))

if choice == 1:

    search_term = str(input("Enter the search term: "))
    count = input("Enter number of results you want: ")
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {"q": search_term, "textDecorations": True, "textFormat": "HTML", "count": count}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    for v in search_results["webPages"]["value"]:
        print(urllib.parse.unquote(v.get("url","")))

elif choice == 2:
    search_term = str(input("Enter the search term: "))
    count = int(input("Enter number of results you want: "))
    for i in search(search_term, tld="co.in", stop=count, pause=2, user_agent="Mozilla/5.0"): 
        print(urllib.parse.unquote(i))

else:
    print("Enter a valid choice!!!")
