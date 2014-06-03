import requests as r

URL = "https://api.instagram.com/v1/tags/%s/media/recent?client_id=%s"

def get_tags(client_id, q=q):
    response = r.get(URL % (q, client_id))
    
    return response.json()
    
