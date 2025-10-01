from fastapi import FastAPI

app=FastAPI()

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
    return user_data


@app.get("/leetcode-stats/{username}")
def get_leetcode_stats(username):
    """
    api to get the solutionCountDifference
    """
    import requests
    data=requests.get("https://leetcode-api-pied.vercel.app/user/"+username)
    store=data.json()
    return (store["submitStats"]['acSubmissionNum'][0])

@app.get("/hackerank-stats/{username}")
def get_hackerank_stats(username):
    """
    api to get hackerank questions solved
    """
    import requests
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }
    data = requests.get("https://www.hackerrank.com/rest/hackers/" + username + "/badges", headers=headers)
    store=data.json()
    return store["models"][0]["solved"]





