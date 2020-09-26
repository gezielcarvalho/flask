from flask import Blueprint
from models.Post import Post

posts = Blueprint('posts',__name__)

@posts.route('/', methods=['GET','POST'])
def main():
    return 'Posts routes'
