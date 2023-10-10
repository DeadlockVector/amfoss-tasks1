from bs4 import BeautifulSoup
from datetime import datetime
import requests
from csv import writer

def assignInfo(html):
    team = "-"
    score = "-"
    overs = "-"

    if html.div is not None:
        team = html.div.text

    if html.strong is not None:
        score = html.strong.text
    
    if html.span is not None:
        overs = html.span.text

    return team, score, overs

def clearCsv():
    with open('task-06/info.csv', 'w') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(["Team1", "Team2", "Score(Team1)", "Score(Team2)", "Timestamp"])
        f_object.close()

def getliveScore(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html5lib')

        checkLive = (soup.find('span', attrs={'class':'ds-text-tight-xs ds-font-bold ds-uppercase ds-leading-5'})).text
        if checkLive == "Live" or checkLive == "Innings break":
            livefeed = soup.find('div', attrs={'class':'ds-flex ds-flex-col ds-mt-2 ds-mb-2'})

            html1 = livefeed.contents[0]
            html2 = livefeed.contents[1]

            team1, score1, overs1 = assignInfo(html1)
            team2, score2, overs2 = assignInfo(html2)
            summary = soup.find('p', attrs={'class':'ds-text-tight-s ds-font-regular ds-truncate ds-text-typo'})

            message = {}
            message["team1"] = [team1, overs1, score1]
            message["team2"] = [team2, overs2, score2]
            message["summary"] = summary.text

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            list_info = [team1, team2, score1, score2, dt_string]
            with open('task-06/info.csv', 'a') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(list_info)
                f_object.close()

            return message

        else:
            return "No Live Matches"
    except:
        return "ESPN error"

def getResult(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html5lib')

    aboutMatch = (soup.find('div', attrs={'class':'ds-text-tight-xs ds-truncate ds-text-typo-mid3'})).text
    result = (soup.find('p', attrs={'class':'ds-text-tight-s ds-font-regular ds-truncate ds-text-typo'})).text
    message = [aboutMatch, result]

    return message

