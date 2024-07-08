import requests

def shorten_link(full_link, link_name):
    API_KEY = 'd72f3d8aaf4ddd7574d2f0c2a1689b232ff0c'
    BASE_URL = 'https://cutt.ly/api/api.php'

    payload = {'key': API_KEY, 'short': full_link, 'name': link_name}
    requests = requests.get(BASE_URL, params=payload)
    data = request.json()

    print('')

    try:
        title = data['url']['title']
        shorten_link = data['url']['shortLink']

        print('Title:', title)
        print('Link:', short_link)
    except:
        status = data['url']['status']
        print('Error Status:', status)

link = input('Enter a Link: >>')
name = input('Give Your Link a name: >>')

shorten_link(link, name)