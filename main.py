from flask import Flask
from flask import request
from flask import jsonify
import hashlib 
import sqlite3

app = Flask(__name__)


@app.route("/add")
def hello():
    x = int(request.args.get("x"))
    y = int(request.args.get("y"))
    
    return jsonify({"result":str(x+y)})

@app.route("/reverse")
def reverse():
    x = request.args.get("name")
    
    return jsonify({"result":x[::-1]})

@app.route("/creatDB")
def creatsdb():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE User (id INT,Email TEXT, Key TEXT)')
    return "Table created successfully"
    conn.close()

@app.route("/addrec")
def addrec():
    msg="x"
    print("Hello") 
#    ide = request.args.get('id')
    email = request.args.get('email')
#    key = request.args.get('key') 
    con = sqlite3.connect("database.db")
    result = hashlib.md5(email.encode())
    cur = con.cursor()
    cur.execute("INSERT INTO User (Email,Key) VALUES (?,?)",(email,result.hexdigest() ) )
    con.commit()
    return "Record successfully"