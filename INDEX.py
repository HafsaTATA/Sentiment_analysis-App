from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

from logger import Logger
from tweet import Tweet
from excel import Excel


log = Logger()

def main(keyword: str, conf: dict):
    global log
    log.warning("Loading configurations...")
    if not conf["token"]:
        log.warning("Please set your access token in './files/conf.json' file")
        input("\n\tPress any key to exit...")
        return

    driver = open_driver(conf["headless"], conf["userAgent"])
    driver.get("https://twitter.com/")
    set_token(driver, conf["token"])
    driver.get("https://twitter.com/")

    log.warning("Starting...")
    data = profile_search(driver, keyword)

    log.warning("Saving...")
    Excel(data, conf["output_form"])


def profile_search(
        driver: webdriver.Chrome,keyword: str
):
    url = "https://twitter.com/search?q="+keyword
    num = 400
    driver.get(url)

    log.warning("Fetching...")
    Ad = []
    results = []
    while len(results) < num:
        tweet = Tweet(driver, Ad)

        data = {}

        data["URL"] = tweet.get_url()
        data["Date"] = tweet.get_date()
        data["Text"] = tweet.get_text()
        data["Lang"] = tweet.get_lang()
        data["Likes"] = tweet.get_num_likes()
        data["Retweets"] = tweet.get_num_retweet()
        data["Replies"] = tweet.get_num_reply()

        results.append(data)

        json.dump(results, open("./files/temp.json", "w"))
        
        log.info(f"{len(results) + 1} : {data['URL']}")

    return results

#creates and configures a Chrome WebDriver instance
def open_driver(headless: bool, agent: str) -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3')
    options.add_argument('ignore-certificate-errors')

    if headless:
        options.add_argument('--headless')

    options.add_argument(f'user-agent={agent}')

    driver = webdriver.Chrome(options=options)
    return driver



def set_token(
        driver: webdriver.Chrome,
        token: str
) -> None:
    src = f"""
            let date = new Date();
            date.setTime(date.getTime() + (7*24*60*60*1000));
            let expires = "; expires=" + date.toUTCString();

            document.cookie = "auth_token={token}"  + expires + "; path=/";
        """
    driver.execute_script(src)

def load_conf() -> dict:
    with open("./files/conf.json", "r") as file:
        return json.loads(file.read())




