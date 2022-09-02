from flask import Flask, Blueprint, request, render_template
from functions import get_posts_by_user
user_blueprint = Blueprint('user_blueprint', __name__, template_folder='templates')

@user_blueprint.route("/users/<username>")
def user_posts(username):
    user_posts = get_posts_by_user(username)

