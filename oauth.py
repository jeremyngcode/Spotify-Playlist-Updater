from os import path
import sys
import time
import base64
import webbrowser
from urllib.parse import urlencode
import json

import requests
from requests.exceptions import Timeout

from settings import (
	CLIENT_ID, CLIENT_SECRET, redirect_uri,
	custom_printer
)
# -------------------------------------------------------------------------------------------------

encoded_credentials = base64.b64encode(
	f'{CLIENT_ID}:{CLIENT_SECRET}'.encode()
).decode()

# Constants
OAUTH_AUTHORIZE_URL = "https://accounts.spotify.com/authorize"
OAUTH_TOKEN_URL = "https://accounts.spotify.com/api/token"

# For access token info
token_cache_json = path.join(path.dirname(__file__), "token.json")

# OAuth functions ---------------------------------------------------------------------------------
def get_user_authorization(*scopes):
	scope_list = ' '.join(scopes)

	params = {
		'client_id': CLIENT_ID,
		'response_type': 'code',
		'redirect_uri': redirect_uri
	}
	if scope_list:
		params['scope'] = scope_list

	auth_url = f'{OAUTH_AUTHORIZE_URL}?{urlencode(params)}'

	print(f'Opening web browser: {auth_url} \n')
	webbrowser.open(auth_url)

def get_access_token(code):
	headers = {
		'Authorization': f'Basic {encoded_credentials}',
		'Content-Type': 'application/x-www-form-urlencoded'
	}
	data = {
		'grant_type': 'authorization_code',
		'code': code,
		'redirect_uri': redirect_uri
	}

	now = time.time()
	response = requests.post(
		OAUTH_TOKEN_URL, headers=headers, data=data
	)
	if response.status_code != 200:
		custom_printer.pprint(response.json())
		return

	expiry_time = {
		'expiry_time': now + response.json()['expires_in']
	}
	new_token_info = response.json() | expiry_time

	custom_printer.pprint(new_token_info)
	print()

	print(f'Saving new token info to "{token_cache_json}"..')
	with open(token_cache_json, 'w') as f:
		json.dump(new_token_info, f, indent=4)

	print('[TOKEN INFO SUCCESSFULLY SAVED]\n')
	return new_token_info

def retrieve_token_info():
	with open(token_cache_json) as f:
		token_cache = json.load(f)

	now = time.time()
	if now < token_cache['expiry_time']:
		return token_cache

	else:
		print('Refreshing access token..')

		headers = {
			'Authorization': f'Basic {encoded_credentials}',
			'Content-Type': 'application/x-www-form-urlencoded'
		}
		data = {
			'grant_type': 'refresh_token',
			'refresh_token': token_cache['refresh_token']
		}

		response = requests.post(
			OAUTH_TOKEN_URL, headers=headers, data=data
		)
		if response.status_code != 200:
			custom_printer.pprint(response.json())
			return

		expiry_time = {
			'expiry_time': now + response.json()['expires_in']
		}
		updated_token_info = token_cache | response.json() | expiry_time

		custom_printer.pprint(updated_token_info)
		print()

		print(f'Saving updated token info to "{token_cache_json}"..')
		with open(token_cache_json, 'w') as f:
			json.dump(updated_token_info, f, indent=4)

		print('[TOKEN INFO SUCCESSFULLY SAVED]\n')
		return updated_token_info

# -------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	get_user_authorization('playlist-modify-public', 'ugc-image-upload')

	try:
		auth_code = input('Enter authorization code: ')
		get_access_token(auth_code)

	except KeyboardInterrupt:
		sys.exit()
