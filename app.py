from flask import Flask,render_template,request
import datetime
from pymongo import MongoClient



def create_app():
    app = Flask(__name__)

    client = MongoClient("mongodb+srv://ARYAN23:aryan@microblog.pnklz.mongodb.net/test")
    app.db = client.microblog

    entries =[]
        
    @app.route("/",methods=["POST","GET"])
    def home():
        if request.method == "POST":
            entry_content = request.form.get("content")
            date = datetime.datetime.today().strftime("%d/%m/%y")
            entries.append((entry_content,date))
            app.db.entries.insert({"content":entry_content,"date":date})


        entries_formated = [
            (entry["content"],
            entry["date"],
            datetime.datetime.strptime(entry["date"],"%d/%m/%y").strftime("%b %d"))
            for entry in app.db.entries.find({})
        ]
        

        return render_template('home.html',entries=entries_formated)

    return app



