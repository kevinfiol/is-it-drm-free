import sys, os
from dotenv import load_dotenv
from bottle import route, redirect, run, request, static_file, template, TEMPLATES
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
    prices = []

    if not plain_id:
        search_results = itad.search(game_name.strip())
        search_results = search_results['data']['results']
        if (len(search_results) < 1):
            game_exists = False
        else:
            plain_id = search_results[0]['plain']

    if game_exists:
        res = itad.getPrices(plain_id)
        prices = res['data']

    return template('results',
        game_exists=game_exists,
        game_name=game_name,
        plain_id=plain_id,
        prices=prices
    )

@route('/search/<name>')
def search(name):
    return itad.search(name.strip())

run(host=os.getenv('HOST'), port=os.getenv('PORT'))