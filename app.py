from flask import Flask, jsonify

from functions import get_posts_all, get_post_by_pk
from main.views import main_blueprint
from post.views import post_blueprint

app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)



@app.route("/api/post")
def get_all_post():
    posts = get_posts_all()
    return jsonify(posts)


@app.route("/api/post/<int:pk>")
def get_post(pk):
    post = get_post_by_pk(pk)
    return jsonify(post)


@app.errorhandler(404)
def not_found(e):
    return "Not found" , 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7000)

