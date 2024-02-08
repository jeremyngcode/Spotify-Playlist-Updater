import json
import base64
from os import path
import requests
from requests.exceptions import Timeout

from oauth import retrieve_token_info
from settings import custom_printer
# -------------------------------------------------------------------------------------------------

# Spotify Web API
BASE_API_URL = "https://api.spotify.com/v1"

def _get(url, **kwargs):
	access_token = retrieve_token_info()['access_token']
	headers = {'Authorization': f'Bearer {access_token}'}

	try:
		response = requests.get(url, headers=headers, params=kwargs, timeout=5)
	except Timeout:
		print('[UNSUCCESSFUL RETRIEVAL - Timed out..]')
	else:		
		if response.status_code == 200:
			data = response.json()
			print('[200 OK - SUCCESSFUL RETRIEVAL]')
			print('-' * 100)
			return data
		else:
			print(f'[{response.status_code} {response.reason}]')
	print('-' * 100)

def get_playlist(playlist_id, fields=None, market=None):
	url = BASE_API_URL + f"/playlists/{playlist_id}"
	params = {
		'fields': fields,
		'market': market
	}

	print(f'get_playlist({playlist_id}):')
	return _get(url, **params)

def change_playlist_details(playlist_id,
	name=None, description=None, public=None, collaborative=None):

	url = BASE_API_URL + f"/playlists/{playlist_id}"

	access_token = retrieve_token_info()['access_token']
	headers = {
		'Authorization': f'Bearer {access_token}',
		'Content-Type': 'application/json'
	}

	input_details = {
		'name': name,
		'description': description
	}
	data = {
		key: value for (key, value) in input_details.items()
		if value is not None
	}

	print(f'change_playlist_details({playlist_id}):')
	try:
		response = requests.put(
			url, headers=headers, data=json.dumps(data), timeout=5
		)
	except Timeout:
		print('[UNSUCCESSFUL REQUEST - Timed out..]')
	else:		
		if response.status_code == 200:
			custom_printer.pprint(data)
			print('[200 OK - PLAYLIST UPDATED]')
			print('-' * 100)
			return data
		else:
			custom_printer.pprint(response.json())
	print('-' * 100)

def add_custom_playlist_cover_image(playlist_id, img_filename):
	url = BASE_API_URL + f"/playlists/{playlist_id}/images"

	access_token = retrieve_token_info()['access_token']
	headers = {
		'Authorization': f'Bearer {access_token}',
		'Content-Type': 'image/jpeg'
	}

	img_file_path = path.join(
		path.dirname(__file__), f"playlist_cover_images/{img_filename}"
	)

	with open(img_file_path, 'rb') as img_file:
		img_encoded = base64.b64encode(img_file.read())

	print(f'add_custom_playlist_cover_image({playlist_id}):')
	try:
		response = requests.put(
			url, headers=headers, data=img_encoded, timeout=5
		)
	except Timeout:
		print('[UNSUCCESSFUL REQUEST - Timed out..]')
	else:
		if response.status_code == 202:
			print('[202 ACCEPTED - IMAGE UPLOADED]')
		else:
			custom_printer.pprint(response.json())
	print('-' * 100)
