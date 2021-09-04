import sys, os
from dotenv import load_dotenv
from bottle import route, redirect, run, request, static_file, template, TEMPLATES
from urllib.parse import unquote
from ITAD import ITAD

load_dotenv()
dirname = sys.path[0] + '/'

itad = ITAD(
    'https://api.isthereanydeal.com',
    os.getenv('ITAD_API_KEY'),
    'us',
    'US'
)

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=dirname + '/static')

@route('/')
def index():
    return template('index', game_name='')

@route('/results', method='GET')
def redirect_to_index():
    redirect('/')

@route('/results', method='POST')
def results():
    game_exists = True
    game_name = request.forms.get('game_name')
    plain_id = request.forms.get('plain_id')
    game_title = game_name
    prices = []

    if game_name.strip() == '':
        redirect('/')

    # `plain_id` is an input element that is added dynamically via javascript in `app.js`
    # `plain_id` is only passed when the user selects from the autocomplete dropdown
    # if `plain_id` is set, that means we can skip searching
    # because we essentially have already searched and retrieved a `plain_id` that ITAD understands
    if not plain_id:
        search_results = itad.search(game_name.strip())
        search_results = search_results['data']['results']
        if (len(search_results) < 1):
            game_exists = False
        else:
            plain_id = search_results[0]['plain']
            game_title = search_results[0]['title']

    if game_exists:
        res = itad.getPrices(plain_id)
        prices = res['data']

    # remove ad tracker from gog URL
    gog_price_idx = findIndex(lambda x: x['shop']['id'] == 'gog', prices)

    if gog_price_idx != -1:
        gog_price = prices[gog_price_idx]
        endpoint = unquote(gog_price['url'].split('www.gog.com')[1]) # unquote decodes uri components
        url = 'https://www.gog.com' + endpoint
        gog_price['url'] = url

    return template('results',
        game_exists=game_exists,
        game_name=game_name,
        game_title=game_title,
        plain_id=plain_id,
        prices=prices
    )

@route('/search/<name>')
def search(name):
    return itad.search(name.strip())

# findIndex util
def findIndex(fn, xs):
    for i, v in enumerate(xs):
        if fn(v):
            return i
    return -1

run(host=os.getenv('HOST'), port=os.getenv('PORT'))