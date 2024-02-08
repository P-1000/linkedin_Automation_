import requests

def create_image(query) :
    reqUrl = "https://api.unsplash.com/search/photos?client_id=3HroJRx-sIURgv-eUs7IsA71YsixIgQVVvhpkSg_OcM&query="+ query
    response = requests.request("GET", reqUrl)
    red = response.json()['results'][0]['urls']['full']
    req = requests.request("GET" , red)
    return req.content
