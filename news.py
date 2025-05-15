import requests

# f"https://newsapi.org/v2/everything?q={+Keypoint}&country={Country}&domains=bbc.co.uk, techcrunch.com, engadget.com&from=2025-01-16&sortBy=popularity&apiKey=01d9fb367f194326926fe4419f94f985"

topic=input("Which topic are you intrested:")
domain=input("Which new channel website you like most:")
response=requests.get(F"https://newsapi.org/v2/everything?q={topic}&domains={domain}&from=2025-01-01&pageSize=3&sortBy=popularity&apiKey=01d9fb367f194326926fe4419f94f985")
data = response.json()

articles = data["articles"]

if(len(articles) ==0):
    print("sorry no news found under your search conditions")
    quit()

for i in range(len(articles)):
    a=(articles[i])
    for u in range(len(articles)):
        ui=dict(articles[u])
        print(F"The title of the article is:{ui["title"]}")

o=input("Which title no. you wanna read:")
o=int(o)-1
a=False
for i in range(len(articles)):
    a=(articles[i])
    for u in range(len(a)):
        ui=dict(articles[u])
        if(u==o):
            print(F"The description of the article is:{ui["description"]}\n")
            print(F"The content of the article is:{ui["content"]}\n for more reading please got to {ui["url"]}")
            a=True
            break
    if a==True:
        break
