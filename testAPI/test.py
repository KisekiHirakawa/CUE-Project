#Kindly add the functions that you think will be helpful. 

#Importing necessary modules
import urllib.request, json
from bs4 import BeautifulSoup
import re

api_key ='Your API key'

#This Function gets the keywords that are needed for the routes
def getKeywordsFromRoute(origin, destination):
    """
    Parameters:
        origin (str): contains the origin location
        destination (str): contains the destination location
        
    Output:
        word_list (list): Contains the directions, road names, etc sequentially
    """
    
    # NOTE: Found that this API doesn't work well with origin/destination strings that have spaces in them
    # and so need to replace the spaces by a '+'
    origin = origin.replace(' ', '+')
    destination = destination.replace(' ', '+')
    
    #Google Maps Ddirections API endpoint
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    
    #Building the URL for the request
    nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
    request = endpoint + nav_request
    
    #Sends the request and reads the response.
    response = urllib.request.urlopen(request).read()
    
    #Loads response as JSON
    directions = json.loads(response)
    
    #Word list that stores all the keywords assosicated with a route
    word_list = []
    
    parsers = ['lxml', 'html.parser'] 
    # @Kiseki, I think lxml worked for you, but wasn't for me so I added html.parser
    
    #This step extracts the keywords which are within the <b></b> hashtag
    for step in directions["routes"][0]["legs"][0]["steps"]:
        soup = BeautifulSoup(step["html_instructions"], parsers[1])
        for node in soup.findAll('b'):
            word_list.append((''.join(node.findAll(text=True))))
            
    return word_list 






#This function gets the tweets from the keyword
def getTweetsFromKeywords(keyword, no_of_tweets, location, range):
    return 0

#A function for relating the image to the keywords (from the exif data, etc)
def getKeywordsFromImage():
    return 0

#This function obtains the location from the tweet
def getLocationFromTweet():
    return 0

#This function compares the tweet location and cross-checks whether the tweet posted is geographically relevant to the keyword
def verfiyTweetLocationWithKeyword():
    return 0

#This function categorises the tweet depending on its content
def categoriseTweet(flood, traffic, roadblock):
    return 0

#
