#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import requests
import json

# API from https://github.com/public-apis/public-apis#health
# API documenation https://www.tvmaze.com/api#show-cast

app = FastAPI()

@app.get("/") 
def read_root():
    return {"Welcome! This API is here to give you information about your favorite TV shows. If you want a show summary add /Summary/SHOW to the url. If you want to know if a show is still on air or if it has ended add /ShowStatus/SHOW to the url. If you want a summary of a particular episode of a show add /EpisodeSummary/SHOW/SEASON/EPISODE to the url. If you want a list of the show's cast add /Cast/SHOW to the url. NOTE: This API will accept numbers because some TV shows contain numbers in the titles but if a number if entered that is not a tv show title (like 90210) the information of the show connected to the ID number in the backend of the source API will be shown."}



#headers = {'Content-Type': 'application/json'}
url_base = "http://api.tvmaze.com"
 
# https://realpython.com/api-integration-in-python/
# https://www.digitalocean.com/community/tutorials/how-to-use-web-apis-in-python-3
# https://www.digitalocean.com/community/tutorials/getting-started-with-python-requests-get-requests
# https://www.geeksforgeeks.org/how-to-parse-data-from-json-into-python/

@app.get("/Summary/{show}")
def showSummary(show: str):
    url = url_base + "/singlesearch/shows?q=:" + show
    response = requests.get(url)
    responseText = (response.text)
    responseTextDict = json.loads(responseText)
    if response.status_code != 200:
        return{"I'm sorry! You have either not entered a TV show or information on this show is not available. Please try another."}
    else:
        return(responseTextDict["summary"])

@app.get("/ShowStatus/{show}")
def showStatus(show: str):
    url = url_base + "/singlesearch/shows?q=:" + show
    response = requests.get(url)
    responseText = (response.text)
    responseTextDict = json.loads(responseText)
    if response.status_code != 200:
        return{"I'm sorry! You have either not entered a TV show or information on this show is not available. Please try another."}
    else:
        return(responseTextDict["status"])

@app.get("/EpisodeSummary/{show}/{season}/{episode}")
def SummaryByEpisode(show: str, season: int, episode: int):
    url = url_base + "/singlesearch/shows?q=:" + show
    response = requests.get(url)
    if response.status_code != 200:
        return{"I'm sorry! You have either not entered a TV show or information on this show is not available. Please try another."}
    else:
        responseText = (response.text)
        responseTextDict = json.loads(responseText)
        showID = (responseTextDict["id"])
        url2 = url_base + "/shows/" + str(showID) + "/episodebynumber?season=" + str(season) + "&number=" + str(episode)
        response2 = requests.get(url2)
        if response2.status_code != 200:
            return{"Oh no! I don't think that episode or season exists. Please try another."}
        else:
            responseText2 = (response2.text)
            responseText2Dict = json.loads(responseText2)
            return(responseText2Dict["summary"])

@app.get("/Cast/{show}")
def CastList(show: str):
    url = url_base + "/singlesearch/shows?q=:" + show
    response = requests.get(url)
    if response.status_code != 200:
        return{"I'm sorry! You have either not entered a TV show or information on this show is not available. Please try another."}
    else:
        responseText = (response.text)
        responseTextDict = json.loads(responseText)
        showID = (responseTextDict["id"])
        url2 = url_base + "/shows/" + str(showID) + "/cast"
        response2 = requests.get(url2)
        responseText2 = (response2.text)
        responseText2Dict = json.loads(responseText2)
        cast = []
        for i in range(len(responseText2Dict)):
            cast.append((responseText2Dict[i]['person']['name']) + " as " + (responseText2Dict[i]['character']['name']))
        return(cast)

# https://careerkarma.com/blog/python-typeerror-list-indices-must-be-integers-or-slices-not-str/