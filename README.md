Spotify Playlist Updater
========================
A script that checks if your playlists have been falsely reported and reupdates its details accordingly.

The Problem
-----------
As of now, **anyone can get a Spotify playlist's title, description or thumbnail cover removed in _seconds_.** You can't do this on some of Spotify's own playlists for obvious reasons, but it still works on most playlists, especially if it isn't owned by a label or distributor.

The process for such abusive/false reporting of Spotify playlists would look something like this:

1. Create an email account. (no Spotify account is needed)
2. Find the report button on the playlist you want to sabotage and click it.
3. Choose "Deceptive content" as the given reason for the report.
4. Copy and paste the given verification code sent to your email.
5. Under "What are you reporting?", you can choose either the image, title, or description. Most malicious actors would choose the title because that is what does max damage.

![what-are-you-reporting](https://github.com/jeremyngcode/Spotify-Playlist-Updater/assets/156220343/eec091df-6133-42ac-8147-d0933385b6dc)

And that's it.

Watch as the image/title/description (whichever you chose) disappears in seconds. In case it wasn't already obvious, a missing playlist title essentially removes the playlist from search results, wiping off its search traffic in an instant.

**This translates to overnight income loss.**

The Evolving Situation
----------------------
To my knowledge, this has been an ongoing issue for at least 4+ years, and has even been covered on [TechCrunch](https://techcrunch.com/2021/09/08/spotify-playlist-curators-complain-about-ongoing-abuse-that-favors-bad-actors-over-innocent-parties/) and [Digital Music News](https://www.digitalmusicnews.com/2021/09/09/spotify-playlist-curators-copyright-abuse/). Searching ["spotify playlist false report"](https://www.google.com/search?q=spotify+playlist+false+report) on Google will yield loads of info on this, and [a thread](https://community.spotify.com/t5/Live-Ideas/Playlists-Solution-to-false-abusive-reporting/idi-p/4928676/page/76) on the Spotify forum that was started in 2020 has accumulated over 70 pages worth of posts with [numerous complaints](https://community.spotify.com/t5/Live-Ideas/Playlists-Solution-to-false-abusive-reporting/idc-p/5587940/highlight/true#M262494) on how playlists are being attacked multiple times by all kinds of [bots](https://community.spotify.com/t5/Live-Ideas/Playlists-Solution-to-false-abusive-reporting/idc-p/5596545/highlight/true#M263121) and [humans](https://community.spotify.com/t5/Live-Ideas/Playlists-Solution-to-false-abusive-reporting/idc-p/5603859/highlight/true#M263830). That thread is no longer open to new replies, but [this one](https://community.spotify.com/t5/Accounts/Playlists-Being-Falsely-Reported/td-p/4782639/page/7) still is (for now). Currently, there is even a [service](https://www.claimguard.cc/) capitalizing on this problem that Spotify refuses to fix. Could it be they themselves doing the false reporting? You decide.

**Over the past few years since I first discovered this problem, Spotify has done close to nothing.**

### Let's take a closer look..
- It used to be that when you report a playlist, let's say the title, then all title, description, and thumbnail cover gets removed together. They have since "improved" in that now if you report the title, then that is all that's being removed.
- I think there used to be no captcha, but now there is, so maybe this helps with bots somewhat.
- More recently, they have included a checkbox where you'd have to acknowledge that you could get your account suspended for false reporting. This one is funny because **you don't need a Spotify account to report any playlist.**
- Choosing the "I just don't like it" option as a reason for reporting no longer works, whereas any reason you selected used to work.

That's pretty much it, or at least from what I'm aware of. Nowhere near solving the problem.

As of now, you can make somewhere between 5-10 consecutive reports before Spotify prevents you from further doing so for a certain timeframe. But anyone can create a new email account on the spot, so this mitigation is almost as good as useless.

### Reviewing Process
**There is no reviewing process.**

When the report is made, Spotify states, "We'll review your report as soon as we can."

![review-report](https://github.com/jeremyngcode/Spotify-Playlist-Updater/assets/156220343/bb971bf6-b43f-4ba8-852c-4b561e2275aa)

**This is 100% a bullshit lie.** Not only do they not review it "as soon as we can", they do not review it *at all.* The playlist title gets removed in seconds.

So I call bullshit.

Also, one would think that they would at least review reports made on "higher stakes" playlists, but I know of at least a few playlists with >50k followers being taken down in an instant, one of which had almost 100k followers.

### Whitelisting
If you try hard enough with Spotify support, you may get a chance to get your playlist [whitelisted](https://community.spotify.com/t5/Live-Ideas/Playlists-Solution-to-false-abusive-reporting/idc-p/5629154/highlight/true#M267588), or "immune" from these false reports.

![playlist-whitelist](https://github.com/jeremyngcode/Spotify-Playlist-Updater/assets/156220343/7db13446-f85a-4aea-a8aa-59378bb4a2a7)

I have just tried reporting my own playlist as I'm typing this, and I can confirm that this works at least. I also tested if the "immunity" remains if you add new tracks, and it does remain.

As a playlist curator, this is probably the best help you can get from Spotify.

### Current Solution (*Somewhat*)
It's hardly surprising to know that automation scripts have since been written to combat this problem. If you didn't manage to persuade Spotify to whitelist your playlist or if you need to change your playlist title / image cover frequently for whatever reason, then scripts can help to reupdate the playlists with the relevant meta info.

However, while this does give a fighting chance for playlist curators, **artists are still being left behind.**

If you're an artist and you have your tracks being added organically to playlists owned by anyone other than yourself, you cannot request for Spotify to whitelist that playlist that's blowing up. If it's not yours, you have zero control, period.

This means that if you see a certain playlist in your Spotify for Artists app gaining traction, you'd have to:
1. Brace yourself because that playlist may be a target soon.
2. When it finally gets reported, pray and hope the curator is alive to reupdate it / fight back / demand for whitelist.

If it's a casual curator who isn't trying to monetize their playlist, then chances are the playlist will not be reupdated, or the curator will simply succumb to the persistent reporting from bots. On the other hand, there is more at stake for a "serious" curator who is making money off their playlist (if they have their own tracks in it for example), so it is likely they will fight back. As an artist, you hope it's the latter.

And that's the solution for artists - *Pray and hope.*

### Bullying An Artist
Apart from rising playlists being a target, indie artists themselves are also at risk of being bullied.

It's simple. There is a "Discovered on" section in every artist page on Spotify. The playlists displayed there are listed in descending order of listeners it generates for the artist. Listeners translate to streams, streams translate to income.

Need I say more?

---

For playlist curators looking to use this tool.. let's dive in.

The Automator
-------------
What this tool essentially does is that it checks at regular intervals if a playlist you own has been reported, and then reupdates the meta info accordingly. I believe this is similar to what most other scripts currently do.

In addition, there are two more features my script does:
1. Able to monitor as many playlists as you like
2. Writes the result of every check into a CSV file (time, which playlist, what got reported) <br>
   Example:
   ```
   date,time,spotify uri,reported?
   2023-11-20,04:10:05,spotify:playlist:123456789abcdefghijklm,OK
   2023-11-20,04:11:05,spotify:playlist:123456789abcdefghijklm,TITLE
   2023-11-20,04:12:05,spotify:playlist:123456789abcdefghijklm,COVER IMAGE
   ```
   This is so you can document and see for yourself how often your playlists are being reported. Also, and I'm not sure if this makes sense, but perhaps the community could then come together to publish the results into one database, so that everyone will know what kind of damage Spotify is refusing to fix.

Getting Started
---------------
Make sure to first have Python installed on your machine, along with the relevant libraries in [requirements.txt](requirements.txt).

### 1. Create App
- Login to [Spotify for Developers](https://developer.spotify.com) and click on 'Create app' in your dashboard.
- Fill in required fields:
  1. App name (can be anything)
  2. App description (can be anything)
  3. Redirect URI: http://localhost:8080/callback
- Go to your newly created app settings and note the following:
  1. Client ID
  2. Client Secret

### 2. Configure [settings.py](settings.py)
- Fill in your `CLIENT_ID` and `CLIENT_SECRET`:
  ```py
  # Example
  CLIENT_ID = 'abc-my-client-id-123'
  CLIENT_SECRET = 'abc-my-client-secret-123'
  ```
  I have also provided a .env template file to use with `load_dotenv()`.
- Make sure `redirect_uri` is the same as the one you entered in your app.
- Fill in your playlist details:
  ```py
  # Example
  playlist1 = Playlist(spotify_id='22characters-long-here',
	title='My Amazing Playlist Title - But keeps disappearing!',
	description='My favourite sleepy music',
	img_filename="sexy-penguin.jpg"
  )
  ```
  The script will update your playlist based on the info you've provided here. You can monitor multiple playlists, just repeat the above code and make sure to include all of them in the `playlists_for_automation` list.
- Fill in `frequency` in minutes. The value here is the time interval between each check. I suggest at least 1 min because even though the frontend will get updated almost instantly, the API takes about that long to update. Not that this is a big issue, but it could skew the data being written in the CSV file.

### 3. Provide cover images
Drop all the relevant image files in the "playlist_cover_images" directory. Make sure the size of each image file is not more than 180kb or you might get a 413 error.

### 4. Authorize App
- Run [oauth.py](oauth.py) in your terminal / cmd.
- In the opened web browser, login to your Spotify account if you haven't already.
- Click 'Agree' to grant the relevant access permissions to your app. 
- In the address bar, copy everything after `code=` and paste it in the terminal.
- Hit enter. If all went well, you should see your token details printed.

The access token expires in 60 mins, but you will not have to worry about this as I have coded it in such a way that it will refresh whenever required.

### 5. Begin Automation
When you're ready, run the [Automator.py](Automator.py) script. You should notice a new output file "data.csv" in the working directory. If you're running this from cmd, press `CTRL+C` to exit the process.

I suggest testing the script with a dummy playlist first to ensure everything is working correctly. Try reporting your own playlists as well.

Dev Notes
---------
Here's how the script determines when a playlist has been reported.

For the title and description, it's pretty straightforward - Empty value = reported. Unless of course the playlist owner intended for the description to be empty (not possible with title), in which case the script will not check it.

It's a little different for the cover image because a default image is still displayed in the absence of a custom provided one. What I've found is that the value for `['images'][0]['height']` in the [API response](https://developer.spotify.com/documentation/web-api/reference/get-playlist) is actually `None` if a custom cover image is provided, and a number if it's a default one. So I just check for truthiness. The exception to this is that if the playlist doesn't consist of tracks from at least 4 different albums (to create the 4 squares in the default cover), then this value will always be `None`, even without a custom cover image. So this litmus test isn't guaranteed to work for all cases as of now. But good thing the playlist image cover is probably the least important.

Help / Contact
--------------
If you need help getting things set up or find any bugs, do create an issue or reach out to me directly at my Twitter or Discord, both of which you can find [here](https://github.com/jeremyngcode/jeremyngcode).

Extras
------
If you're an artist on Spotify, you might also be interested in checking out a [dashboard](https://github.com/jeremyngcode/Spotify-Graphs-Dashboard) I built for visualizing your streams.
