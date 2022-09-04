#импортируем все необходимое
from flask import Flask, jsonify
from functions import get_posts_all, get_post_by_pk
from main.views import main_blueprint
from post.views import post_blueprint
import logging

#регистрируем блюпринты
app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)

#добавляем api
@app.route("/api/post")
def get_all_post():
    posts = get_posts_all()
    FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
    logging.basicConfig(filename="api.log", level=logging.INFO, format=FORMAT)
    return jsonify(posts)


@app.route("/api/post/<int:post_id>")
def get_post(post_id):
    post = get_post_by_pk(post_id)
    FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
    logging.basicConfig(filename="api.log",level=logging.INFO, format=FORMAT)
    return jsonify(post)

#добавляем обработчики ошибок
@app.errorhandler(404)
def not_found(e):
    return "Not found", 404

@app.errorhandler(500)
def not_found(e):
    return "Internal Server Error", 500

#запускаем
if __name__ == '__main__':
    app.run()

