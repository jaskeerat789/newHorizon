import os
import EmotiRecog  
from flask import Flask,jsonify,request
import time
from threading import Thread
import json
obj1=EmotiRecog.Emotion()
import test
lis=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','T','U','V','W','X','Y','Z']

#from werkzeug import secure_filename
#os.system("./ngrok http 5000")
class Function:
	def __init__(self):
		self.stop=False
		self.stop1=False
		self.stop2=False
		self.stop3=False
		self.stop4=False
		self.stop5=False
		self.time=0
		self.rurl=None
	def Work(self):
		i=1
		while(i):
			if(self.stop):
				break
			obj1.capture()
			obj1.send()
			i+=1
		return
	def Loging(self,session,Time,hr,attention=None,Type=None,):
		with open("data.json") as json_file:
			data=json.load(json_file)
			l=len(data['today'])
			print(l)
			data['today'].append({})
			print(len(data['today']))
			data['today'][l]["session"] = session
			data['today'][l]["time"] = Time
			data['today'][l]["heartrate"] = hr
			if(attention):
				data['today'][l+1]["attention"] =attention
			if(Type):
				data['today'][l+1]["type"] = Type
			json_file.seek(0)
			json.dump(data, json_file, indent=4)
			json_file.truncate()
		pass
	def TraingAbc(self):
		before=time.time()
		for i in lis:
			if (not self.stop5):
				test.ABC(i)
			else:
				return
		return

	def TrainigStencile(self):
		before=time.time()
		while(not self.stop1):
			print("Stencile")
		after=time.time()
		self.time=before-after
		#self.Loging("writing",obj.time,[])
		return
		# obj.capture()
		# res=obj.send()
	def Rhymes(self):
		before=time.time()
		while(not self.stop2):
			print(self.rurl)
		after=time.time()
		self.time=before-after
		#self.Loging("writing",obj.time,[])
		return
	def Beats(self):
		before=time.time()
		while(not self.stop3):
			print("Beates")
		after=time.time()
		self.time=before-after
		#self.Loging("writing",obj.time,[])
		return
	def Play(self):
		before=time.time()
		while(not self.stop4):
			print("play")
		after=time.time()
		self.time=before-after
		#self.Loging("writing",obj.time,[])
		return
obj=Function()

app=Flask(__name__)

@app.route("/trainig/Abc/start")
def hello():
	thread=Thread(target=obj.TraingAbc)
	if(obj.stop5):
		obj.stop5=False
	thread.start()
	print("started")
	return "started"
@app.route("/training/Abc/stop")
def stopAbc():
	obj.stop5=True
	return 'ended'

@app.route("/emotirecog/start")
def rec():
	thread=Thread(target=obj.Work)
	if(obj.stop):
		obj.stop=False
	thread.start()
	print("started")
	return "started"

@app.route("/emotirecog/stop")
def stop():
	obj.stop=True
	return 'ended'

@app.route("/training/stensile/start")
def trainigStencileStart():
	thread=Thread(target=obj.TrainigStencile)
	if(obj.stop1):
		obj.stop1=False
	thread.start()
	value=None
	Type=request.args.get('name')
	if(Type=='English'):
		value="started english"
	elif Type=='Hindi':
		value="started Hindi"
	elif Type=='Maths':
		value="started Maths"
	
	return(value)
@app.route("/training/stensile/stop")
def trainigStencileStop():
	obj.stop1=True
	return("stopped")

@app.route("/training/Rhymes/start")
def StartRhymes():
	obj.rurl=request.args.get("url")
	thread=Thread(target=obj.Rhymes)
	if(obj.stop2):
		obj.stop2=False
	thread.start()
	#send the hit the url to play video
	return("rhyme started")
@app.route("/training/Rhymes/stop")
def StopRhymes():
	obj.stop2=True
	return("stopped")

@app.route('/beats/start')
def StartBeats():
	thread=Thread(target=obj.Beats)
	if(obj.stop3):
		obj.stop3=False
	thread.start()
	#send the hit the url to play video
	return("beat started")

@app.route('/beats/stop')
def StopBeats():
	obj.stop3=True
	return("stopped")

@app.route('/play/start')
def StartPlay():
	thread=Thread(target=obj.Play)
	if(obj.stop4):
		obj.stop4=False
	thread.start()
	#send the hit the url to play video
	return("video started")

@app.route('/play/stop')
def StopPlay():
	obj.stop4=True
	return("stopped")
	#stop video
	pass


