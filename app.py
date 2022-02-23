from gtts import gTTS
from playsound import playsound
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def FUN_root():
    return render_template("index.html")


 
@app.route("/tsact",methods = ['GET','POST'])
def owner_logact():
   if request.method == 'POST':
       text = request.form['text']
       language = 'en'
       myobj = gTTS(text=text, lang=language, slow=True)
       print(myobj)
       myobj.save("welcome.mp3")
       playsound("welcome.mp3")
       os.remove('welcome.mp3')
       return render_template('index.html')
   

if __name__ == "__main__":
   app.run(debug=True,host='127.0.0.1', port=5000)