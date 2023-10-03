import requests
from send_email import send_email

topic = "tesla"

api_key = "197e6aaaf47b4fc2a0ca11fe7629db3b"
url = "https://newsapi.org/v2/everything?"\
      f"q={topic}&from=2023-09-03&" \
      "sortBy=publishedAt"\
      "&apiKey=197e6aaaf47b4fc2a0ca11fe7629db3b&" \
      "language=en"


#make request
request = requests.get(url)

#get a dictionary iwth data
content = request.json()

#access the article titles
body = ""
for article in content['articles'][:20]:
    if article['title'] is not None:
        body = "Subject: Today's News" +  \
            "\n" + body + article["title"] + "\n" \
            + article["description"] + "\n" \
            + article["url"] + 2*"\n"
    
    
    
body = body.encode('utf-8')    
send_email(message=body)