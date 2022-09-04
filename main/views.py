#импортируем все необходимое
from flask import Blueprint, request, render_template
from functions import get_posts_all, search_for_posts, load_bookmarks, get_posts_by_user
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

#создаем вьюшки
@main_blueprint.route('/')
def main_page():
    posts = get_posts_all()
    bookmarks = load_bookmarks()
    return render_template("index.html", posts=posts, bookmarks_number=len(bookmarks))

@main_blueprint.route('/search')
def search_page():
    s = request.args.get('s')
    posts = search_for_posts(s)
    return render_template("search.html", posts=posts[1:11], posts_number=len(posts), word=s)

@main_blueprint.route('/users/<user_name>')
def user_page(user_name):
    user_posts = get_posts_by_user(user_name)
    return render_template("user-feed.html", posts=user_posts)


