#импортируем все необходимое
from flask import Flask, Blueprint, request, render_template
from functions import get_comments_by_post_id, get_post_by_pk
post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')

#создаем вьюшку
@post_blueprint.route('/posts/<int:postid>')
def main_page(postid):
    post = get_post_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    comments_number = len(comments)
    return render_template("post.html", post=post, comments=comments, comments_number=comments_number)