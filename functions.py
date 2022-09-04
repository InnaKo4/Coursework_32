import json

def load_posts():
    """Загружает данные из файла JSON"""
    with open('data/posts.json', "r") as file:
        raw_json = file.read()
        json_file = json.loads(raw_json)
        return json_file

def get_posts_all():
    """Возвращает данные из JSON"""
    posts = load_posts()
    return posts

def get_posts_by_user(user_name):
    """Получает список постов по имени пользователя"""
    posts = load_posts()
    all_user_posts = []
    for post in posts:
        if user_name == post['poster_name']:
            try:
                all_user_posts.append(post)
            except ValueError:
                return "Пользователь не найден"
    return all_user_posts

def get_comments_by_post_id(post_id):
    """Получает комментарии по id"""
    with open("data/comments.json", 'r') as f:
        raw_json = f.read()
        comments = json.loads(raw_json)
        post_comments = []
        for comment in comments:
            if post_id == comment['post_id']:
                try:
                    post_comments.append(comment)
                except ValueError:
                    "Пост не найден"
        return post_comments

def search_for_posts(word):
    """Получает список постов по слову"""
    posts = load_posts()
    posts_by_word = []
    for post in posts:
        if word.lower() in post['content'].lower():
            posts_by_word.append(post)
    return posts_by_word


def get_post_by_pk(pk):
    """Получает пост по его pk"""
    posts = load_posts()
    for post in posts:
        if pk == post['pk']:
            return post

def load_bookmarks():
    """Получает список закладок"""
    with open('data/bookmarks.json', "r") as file:
        raw_json = file.read()
        bookmarks = json.loads(raw_json)
        all_bookmarks = []
        for bookmark in bookmarks:
            all_bookmarks.append(bookmark)
        return all_bookmarks

