import web
import thread
import time
import data
import string
from web import form

render=web.template.render('templates/')
urls=(
	'/','index',
	'/attend','attend',
	'/register','register'
	)

registerform=form.Form(
	form.Textbox("id",form.notnull)
	)

attendform=form.Form(
	form.Textbox("id",form.notnull),
	form.Textbox("num",form.notnull)
	)


def index_page():
	for i in list(data.db.select('users')):
		print i['id']
	time.sleep(10)
	for i in list(data.db.select('users')):
		data.users[i['id']]=0.0
	while True:
		start=time.time()
		data.thisturn={}
		data.num=0
		data.total=0
		time.sleep(0.9)
		if data.num!=0:
			average=data.total/data.num*0.618
			print average
			data.thisturn['winner']=score(data.thisturn,data.users,average)
			data.winner=data.thisturn['winner']
			data.winnernumber=data.thisturn[data.winner]
			data.thisturn['result']=average
			data.goldpoint.append(average)
		t=1-(time.time()-start)
		time.sleep(t)
		print data.num
		data.turn+=1

def score(thisturn,users,average):
	value_max=0
	value_min=100
	for i in thisturn:
		a=abs(thisturn[i]-average)
		if a>value_max:
			value_max=a
			max_num=i
		if a<value_min:
			value_min=a
			winner=i
	for i in list(data.db.select('users')):
		if i['id'] not in thisturn and i['id']!=winner:
			users[i['id']]-=5
		elif i['id']==winner:
			users[i['id']]+=10
		elif i['id']==max_num:
			users[i['id']]-=1
	return winner

class index:
	def GET(self):
		return render.index(data.turn,data.winnernumber,data.users,data.goldpoint)

class attend:
	def GET(self):
		form=attendform()
		return render.attend(form)
	def POST(self):
		form=attendform()
		if not form.validates():
			return render.attend(form)
		else:
			i=web.input()
			i.num=string.atof(i.num)
			data.num+=1
			data.total+=i.num
			data.thisturn[i.id]=i.num
			return 0

class register:
	def GET(self):
		form=registerform()
		return render.register(form)
	def POST(self):
		form=registerform()
		if not form.validates():
			return render.register(form)
		else:
			i=web.input()
			data.db.insert('users',id=i.id,pd=0)
			data.users[i.id]=0.0
			return 0

if __name__=="__main__":
	thread.start_new_thread(index_page,())
	app=web.application(urls,globals())
	app.run()