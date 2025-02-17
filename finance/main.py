import os, json
from pathlib import Path
from sys import exit
try:
    import requests
except:
    print("You need the \"requests\" package.")
    exit()

# This is a program that will provide news about a ticker you are looking for.
# https://newsapi.org/
# https://polygon.io/
