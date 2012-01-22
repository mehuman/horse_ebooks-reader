import twitter
import subprocess
import time
api = twitter.Api()

statuses = api.GetUserTimeline('horse_ebooks')
for s in statuses:
	subprocess.call(['/usr/bin/say','A horse ebooks tweet'])
	time.sleep(1)
	subprocess.call(['/usr/bin/say',s.text])
	time.sleep(2)
