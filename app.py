from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def main():
    page_title = "Home | Personal Blog"
    name = "Than Duc Kien"
    return render_template('index.html', page_title=page_title)
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/dashboard')
def dashboard():
    conn = sqlite3.connect('PostDB.db')
    cur = conn.execute('SELECT fullname FROM users WHERE username = ? ', ("admin", ))
    row = cur.fetchone()
    fullname = row[0]
    return render_template('dashboard.html', user=fullname)
@app.route('/check_login', methods=('GET', 'POST'))
def check_login():
    pass
    # username = request.form['username']
    # password = request.form['password']
    # conn = sqlite3.connect('PostDB.db')
    # select_user = 'SELECT * FROM users WHERE username=? AND password=?'
    # cur = conn.execute(select_user, (username, password, ))
    # row = cur.fetchall()
    # count = len(row)
    # # 1 record
    # # 0 record: failed
    # db_username = row[0]
    # db_password = row[1]
    #
    # msg = ''
    # # if username != db_username or password != db_password:
    #     msg = 'Your credential is incorrect'
    # else:
    #     msg = 'Login successfully'
    # return render_template('dashboard.html', username=username, message=msg)
@app.route('/save_post')
def save():
    return render_template('contact.html')
@app.route('/post/<post_id>')
def post(post_id):
    if post_id == 10:
        post_title = "Post 10"
    else:
        post_title = "Something"
    return render_template('post.html', post_title=post_title, post_id=post_id)
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/form')
def form():
    return render_template('form.html')
@app.route('/create_post')
def create_new_post():
    post_tile = "Cách Trung Quốc chiếm ngôi vương xuất khẩu ôtô"
    page_title = "Create New Post | Personal Blog"
    return render_template('create_post.html', page_title=page_title)
# @app.route('/about/<user>')
# def get_about(user):
#     return render_template('about.html', name=user)

if __name__ == '__main__':
    app.run()
