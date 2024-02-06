from os import environ
from dotenv import load_dotenv
import pprint
# -------------------------------------------------------------------------------------------------

load_dotenv()

# Settings for pprint PrettyPrinter
custom_printer = pprint.PrettyPrinter(
	depth=None,
	indent=1,
	width=100,
	sort_dicts=False,
	compact=False
)

class Playlist:
	def __init__(self, spotify_id, title=None, description=None, img_filename=None):
		self.spotify_id = spotify_id
		self.title = title
		self.description = description
		self.img_filename = img_filename

# EDIT ACCORDINGLY --------------------------------------------------------------------------------
CLIENT_ID = environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = environ.get('SPOTIFY_CLIENT_SECRET')
redirect_uri = "http://localhost:8080/callback"

# Input a string for each parameter you wish to update, else input None
playlist1 = Playlist(spotify_id=None,
	title=None,
	description=None,
	img_filename=None
)

playlist2 = Playlist(spotify_id=None,
	title=None,
	description=None,
	img_filename=None
)

playlist3 = Playlist(spotify_id=None,
	title=None,
	description=None,
	img_filename=None
)

# Example
example = Playlist(spotify_id='22characters-long-here',
	title='My Amazing Playlist Title - But keeps disappearing!',
	description=None,
	img_filename="sexy-monkey.jpg"
)

# Input all playlists you wish to monitor and update accordingly
playlists_for_automation = [playlist1, playlist2, playlist3]

# How often to check in minutes
frequency = 2
