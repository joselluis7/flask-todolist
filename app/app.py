# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, request, redirect, flash

from app.extensions import database
from app.extensions.database import db
from app.extensions import appearance
from app.models.tables import Todo

app = Flask(__name__)
app.config.from_object('settings')
database.init_app(app)
appearance.init_app(app)

@app.route('/', methods=['GET','POST'])
def index(): 
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)
        if new_task:
            db.session.add(new_task)
            db.session.commit()
            flash('Added task named as {}.'.format(new_task.content))
            return redirect('/')
        return "There was an issue adding a task"
    tasks = Todo.query.order_by(Todo.data_created).all()
    return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task = Todo.query.get_or_404(id)
    try:
        db.session.delete(task)
        db.session.commit()
        return redirect('/')
    except:
        return "Something went wrong while deleting"


@app.route('/update/<int:id>', methods=['POST','GET'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue during the update"
    else:
        return render_template('update.html', task=task)


def create_app():
    return app