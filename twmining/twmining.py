import twitter

from twitter import OAuth

def oauth_login(oauth_token, oauth_token_secret, consumer_key, consumer_secret):
    '''
    login and auth twitter based on token and secret.
    '''
    auth = twitter.oauth.OAuth(oauth_token,
                               oauth_token_secret,
                               consumer_key,
                               consumer_secret)
    
    
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

def twitter_search(twitter_api, q, max_results=200, **kw):
    results = twitter_api.search.tweets(q=q, count=100, **kw)
    statuses = results['statuses']
    max_results = min(1000, max_results)
    
    for _ in range(10):
        try:
            next_results = search_results['search_metadata']['next_results']
        except KeyError, e: # No more results when next_results doesn't exist
            break
            
        kwargs = dict([ kv.split('=') 
                        for kv in next_results[1:].split("&") ])
        
        search_results = twitter_api.search.tweets(**kwargs)
        statuses += search_results['statuses']
        
        if len(statuses) > max_results: 
            break
            
    return statuses
