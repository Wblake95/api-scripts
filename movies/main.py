# API to seach a movies name and if where to watch it (netflix, etc)
# https://api.watchmode.com/

# argparse, requests.
import argparse, requests

# Take request and parse.
parser = argparse.ArgumentParser(
        prog="WhatPlatform",
        description="Find what platform a movie is playing on",
        epilog="Change me!"
        )
# The arguments.
parser.add_argument("movieName")
#parser.add_argument("-p","--platform")
# SUB NOTE: add stdin / stdout
args = parser.parse_args()

#NOTE: Get API Key (temporary)
# SUB NOTE: make this a environment variable or something.
with open("api.txt","r") as file:
    temp = file.readlines()
    for i in temp: 
        if "watchmode" in i:
            API = "apikey=" + i[i.rfind(" ")+1:]

#NOTE: build api request
url = "https://api.watchmode.com/v1/"

url = url + "search/?" + args.movieName + "&" + API

r = requests.get(url)

result = url.json()

#NOTE: filter results

#NOTE: return results
