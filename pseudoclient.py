import urllib 
import urllib2
import time
import thread
def postit(no,interval):
	for j in range(40):
		post_data = urllib.urlencode({'id': str(no), 'num':50.0-0.1*j})
		req = urllib2.Request(path,post_data)
		response = urllib2.urlopen(req)
		print response.read()
path = "http://192.168.1.150:8080/attend"
for i in range(100000,100040):
	thread.start_new_thread(postit,(i,1))
		
