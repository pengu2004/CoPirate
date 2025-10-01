from fastapi import FastAPI
from db import init_db, insert_stat, get_stats

app=FastAPI()
init_db()

@app.get("/")
def welcome():
    return "Hello World"

@app.get("/twitter-stats/{username}")
def get_twitter_stats(username):
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from bs4 import BeautifulSoup



    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36") 

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service,options=options)

    driver.get("http://nitter.net/" + username)
    page_source = driver.page_source
    driver.quit()
    soup = BeautifulSoup(page_source, "html.parser")

    data = soup.find_all("span", class_="profile-stat-num")
    user_data = {}

    Labels = ["Tweets", "Followers", "Following", "Likes"]

    for i, label in enumerate(Labels):
        user_data[label] = int(data[i].get_text().replace(",", ""))
        insert_stat(username, "twitter", label, user_data[label])
    return user_data


@app.get("/leetcode-stats/{username}")
def get_leetcode_stats(username):

    import requests
    data=requests.get("https://leetcode-api-pied.vercel.app/user/"+username)
    store=data.json()
    solved = store["submitStats"]['acSubmissionNum'][0]['count']
    # store in DB
    insert_stat(username, "leetcode", "ProblemsSolved", solved)
    return {"ProblemsSolved": solved}

