import sys
import csv
from os import path
from datetime import datetime
from time import sleep

from settings import (
	playlists_for_automation,
	frequency
)
from functions import (
	get_playlist,
	change_playlist_details,
	add_custom_playlist_cover_image
)
# -------------------------------------------------------------------------------------------------

# Create a csv data file for writing the result of each check
data_file = path.join(path.dirname(__file__), "data.csv")
column_names = ['date', 'time', 'spotify uri', 'reported?']

if not path.exists(data_file):
	print('Creating data file..\n')

	with open(data_file, 'w', newline='') as f:
		dictwriter = csv.DictWriter(f, fieldnames=column_names)
		dictwriter.writeheader()

# The interval between each check in seconds
freq = frequency * 60

playlists_for_automation = [
	playlist for playlist in playlists_for_automation
	if playlist.spotify_id is not None
]

# Begin automation
while True:
	try:
		for playlist in playlists_for_automation:
			data = get_playlist(playlist.spotify_id)
			now = datetime.now()

			if not data:
				sys.exit()

			row = {
				'date': now.strftime('%Y-%m-%d'),
				'time': now.strftime('%H:%M:%S'),
				'spotify uri': data['uri'],
				'reported?': ''
			}

			# Checks for a blank title and updates accordingly
			if all((playlist.title, not data['name'])):
				row['reported?'] += 'TITLE + '
				change_playlist_details(playlist.spotify_id,
					name=playlist.title
				)

			# Checks for a blank description and updates accordingly
			if all((playlist.description, not data['description'])):
				row['reported?'] += 'DESCRIPTION + '
				change_playlist_details(playlist.spotify_id,
					description=playlist.description
				)

			# Checks for a default cover image and updates accordingly
			if all((playlist.img_filename, data['images'][0]['height'])):
				row['reported?'] += 'COVER IMAGE + '
				add_custom_playlist_cover_image(playlist.spotify_id,
					img_filename=playlist.img_filename
				)

			if not row['reported?']:
				row['reported?'] = 'OK'
			else:
				row['reported?'] = row['reported?'][:-3]

			print('Writing data..')
			with open(data_file, 'a', newline='') as f:
				dictwriter = csv.DictWriter(f, fieldnames=column_names)
				dictwriter.writerow(row)

			print('[WRITING COMPLETE]')
			print('-' * 100)

		sleep(freq)

	except KeyboardInterrupt:
		sys.exit('[PROGRAM TERMINATED]')