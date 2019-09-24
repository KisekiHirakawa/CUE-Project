import pprint as pp
try:
    import credentials as cred
except:
    print('NO CREDENTIALS!!')
import tweepy

try:
    import json
except ImportError:
    import simplejson as json
    

def isGeoEnabled(tweet):
    """
    This function checks if a tweet has the geo feature enabled to pin point the exact 
    latitude and longitude of the tweet
    
    Parameters:
        tweet (tweepy.models.Status): tweepy.models.Status object. Decided against something like tweet ID since that would involve calling an API again
        
    Output:
        geo (bool): True or False
    """
    if tweet._json['geo']==None:
        return False
    else:
        return True
    
def isPlaceEnabled(tweet):
    """
    This function checks if a tweet has the place parameter enabled. Place is different from geo in that it is something
    
    Parameters:
        tweet (tweepy.models.Status): tweepy.models.Status object. Decided against something like tweet ID since that would involve calling an API again
        
    Output:
        geo (bool): True or False
    """
    if tweet._json['place']==None:
        return False
    else:
        return True

if __name__ == "__main__":
    # This part of the code is just to try out the functions written before---
    
    
    # Setup tweepy to authenticate with Twitter credentials:
    auth = tweepy.OAuthHandler(cred.CONSUMER_KEY, cred.CONSUMER_SECRET)
    auth.set_access_token(cred.ACCESS_TOKEN, cred.ACCESS_SECRET)
    
    # Create the api to connect to twitter with your credentials
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
    
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
        
    # ----------------------------------------
    # A code snippet to get some tweets    
    #places = api.geo_search(query='Japan', granularity='country')
    #place_id = places[0].id
    
    tweets = tweepy.Cursor(api.search,
                        #q=['place:%s AND delay' % place_id],
                        q='Elephant',
                        lang='en', 
                        tweet_mode='extended',
                        extended_entities=True).items(3)
    # ----------------------------------------
    
    
    tweets = list(tweets)   # converted to list for easier handling
    
    for tweet in tweets:
        print('\n\n===================================')
        print(isGeoEnabled(tweet))
        print('-------------------------------')
        pp.pprint(tweet._json)
        
   
        