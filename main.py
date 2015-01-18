#!/usr/bin/python

import praw
import tyo
from time import sleep
from random import randint

r = praw.Reddit(user_agent='12 y/o translator bot by /u/hassanchug.', cache_timeout=5)
r.login('tyo-translate', '')

while True:
	try:
		for msg in r.get_unread():
			if msg.body.lower().find('/u/tyo-translate') != -1:
				txt = ' '.join(msg.body.lower().split())
				if txt == '/u/tyo-translate':
					txt = r.get_info(thing_id=msg.parent_id).body
					
				
				if txt.split()[1].find('asl') == 0 or txt.split()[1].find('a/s/l') == 0:
					m = ''
					act = 'cyber'
					if randint(0, 1) == 0:
						act = 'cam'
						m += str(randint(18, 20)) + "/f/ca\n\nlet's " + act +  "  ;)"
						msg.reply(m)
				else:
					msg.reply(tyo.translate(txt.replace('/u/tyo-translate', ''))[:10000])
				sleep(5)
			msg.mark_as_read()
	except:
		continue
