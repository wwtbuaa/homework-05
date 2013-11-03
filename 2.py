import web
import thread
import string
import time

answersum=0
turn=0
start=0
number=0
db=web.database(dbn='sqlite',db='./web.db')
render=web.template.render('templates/')
usrers={}
now={}
thisturn={}
allturn={}
urls=(
	'/register','register',
	'/attend','attend'
	'/','index'
)
app=web.application(urls,globals())

class index:
	def GET(self):
		return render.index(turn)

def index_page():
	for i in list(db.select('users')):
		users[i['id']]=0.0
	while True:
		thisturn={}
		number=0
		answersum=0
		start=time.time()
		t=10-(time.time()-start)
		time.sleep(t)
	thread.exit_thread()

if __name__=="__main__":
	thread.start_new_thread(index_page,())
	app.run()