from flask import Blueprint
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from config import db
from models.Post import Post

posts = Blueprint('posts',__name__)

@posts.route('/new', methods=['GET'])
def new():
    return render_template('posts/new.html')

@posts.route('/', methods=['POST'])
def create():
    post = Post(request.form['title'], request.form['conteudo'])

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('posts.new'))




