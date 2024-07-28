from flask import Flask, redirect, render_template, request, url_for, flash
import sqlite3 as sql

app=Flask(__name__)
app.secret_key='star/cloud@821'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        if request.form['username'] !='thariq' or request.form['password'] != 'thariq08':
            error='Invalid username or password. Please try again!'
        else:
            message='You were successfully logged in \t' +  request.form['username'] 
            return render_template('index.html',message=message)
    return render_template('home.html',error=error)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/enter_expense')
def new_stud():
    return render_template('add_expense.html')

@app.route('/add_expense',methods=['POST','GET'])
def add_expense():
    try:
        date=request.form['date']
        category=request.form['category']
        description=request.form['description']
        amount=request.form['amount']
        with sql.connect("expense_data.db") as con:
            cur = con.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS expense_tracker (date DATE,category TEXT, description TEXT, amount INTEGER )''')
            cur.execute("insert into expense_tracker (date, category, description, amount) values (?,?,?,?)",(date, category,description,amount))
            con.commit()
            msg="Record successfully addded"
    except:
        con.rollback()
        msg="Error in insert operation"
    finally:
        return render_template('index.html',msg=msg)
        
@app.route('/listall',methods=['POST','GET'])
def list():
    total_amount = 0
    con=sql.connect("expense_data.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from expense_tracker")
    rows=cur.fetchall()
    for row in rows:
        total_amount += row['amount']
    return render_template("list_all.html",rows=rows,total_amount=total_amount)

if __name__=='__main__':
    app.run(debug=True,port=5005)

