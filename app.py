from flask import Flask, render_template, redirect, request
import os
import psycopg2
from psycopg2 import pool


app = Flask(__name__)
db = psycopg2.pool.SimpleConnectionPool(1, 20, os.environ.get('DATABASE_URL'))
conn = db.getconn()

@app.route('/')
def hello():
    cursor = conn.cursor()
    cursor.execute("select * from todo order by name asc;")
    result = cursor.fetchall()
    cursor.close()
    return render_template('todo-list.html', todos=result)

@app.route('/todo/create')
def create():
    cursor = conn.cursor()
    if "todo_name" in request.args:
        todo_name = request.args.get('todo_name')
        if todo_name:
            cursor.execute("insert into todo (name,completed) values (%s, %s)", (todo_name, False))
            conn.commit()

    cursor.close()
    return redirect('/')

@app.route('/todo/delete/<int:id>')
def delete(id):
    cursor = conn.cursor()
    
    if id:
        sql = "delete from todo where id={}".format(id)
        cursor.execute(sql)
        conn.commit()

    cursor.close()
    return redirect('/')


@app.route('/todo/complete/<int:id>')
def complete(id):
    cursor = conn.cursor()

    if id:
        sql = "update todo set completed={} where id={}".format(True, id)
        cursor.execute(sql)
        conn.commit()

    cursor.close()
    return redirect('/')

if __name__ == '__main__':
    app.run()