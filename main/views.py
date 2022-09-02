from flask import Flask, Blueprint, request, render_template
from functions import get_posts_all, search_for_posts
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

@main_blueprint.route('/')
def main_page():
    posts = get_posts_all()
    return render_template("index.html", posts=posts)

@main_blueprint.route('/search')
def search_page():
    s = request.args.get('s')
    posts = search_for_posts(s)
    return render_template("search.html", posts=posts, posts_number=len(posts), word=s)

