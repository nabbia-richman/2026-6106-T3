from flask import Flask, render_template, request
import sqlite3
import datetime


app = Flask(__name__)

# 初始化数据库
def init_db():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS user (
            name TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()


@app.route("/",methods=["GET","POST"])
def index():
   return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
   return(render_template("main.html"))

@app.route("/transferMoney",methods=["GET","POST"])
def transferMoney():
   return(render_template("transferMoney.html"))

@app.route("/depositMoney",methods=["GET","POST"])
def depositMoney():
   return(render_template("depositMoney.html"))

@app.route("/message", methods=["GET","POST"])
def message():
    return render_template("message.html")


if __name__ == "__main__":
    app.run()