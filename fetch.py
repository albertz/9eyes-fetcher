#!/usr/bin/python -u

import better_exchook
better_exchook.install()

# NOTE: I had to make a few fixes on mechanize and I also added images support.
# So, in case this isn't upstream yet, you have to get mechanize from here:
#   https://github.com/albertz/mechanize
import mechanize

br = mechanize.Browser()

baseurl = "http://9-eyes.com/"

def filename_for_url(url):
	fn = url.replace(baseurl, "")
	fn = fn.replace("/", "_")
	if not fn.endswith(".jpg"): fn += ".jpg"
	return fn

def fetch(url):
	fn = filename_for_url(url)
	print fn, "...",
	import urllib2
	open(fn, "w").write( urllib2.urlopen(url).read() )
	print "fetched"
	
i = 1
while True:
	br.open(baseurl + "page/" + str(i))

	c = 0
	for img in br.images():
		url = img.url
		if baseurl not in url: continue
		fetch(url)		
		c += 1
		
	print "page", i, ", pictures:", c
	if c == 0: break
	
	i += 1
