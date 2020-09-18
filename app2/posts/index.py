from flask import Blueprint

posts = Blueprint('posts',__name__)

@posts.route('/', methods=['GET','POST'])
def main():
    return 'Posts routes'
