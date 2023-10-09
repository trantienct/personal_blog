from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key='abcda1234'
@app.route('/home')
def main():
    page_title = "Home | Personal Blog"
    name = "Than Duc Kien"
    return render_template('index.html', page_title=page_title)
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/')
def login():
    return render_template('login.html')
@app.route('/log_out')
def logout():
    session.pop('username')
    session.pop('status')
    return redirect(url_for('login'))
@app.route('/dashboard')
def dashboard():
    if session.get('status') is None:
        return redirect(url_for('login'))
    else:
        if session.get('status') ==1:
            conn = sqlite3.connect('PostDB.db')
            cur = conn.execute('SELECT fullname FROM users WHERE username = ? ', ("admin",))
            row = cur.fetchone()
            session['username'] = row[0]
            return render_template('dashboard.html')

@app.route('/dashboard/new-category')
def new_category():
    return render_template('new-category.html')
@app.route('/dashboard/category', methods=['GET'])
def edit_category():
    category_id = request.args.get('id')
    conn = sqlite3.connect('PostDB.db')
    cur = conn.execute('SELECT * FROM category WHERE category_id =?',(category_id))
    row = cur.fetchone()
    return render_template('edit-category.html', id = row[0], category_name = row[1])
    #BTVN: Trong form edit-category sửa text Name thành name của category mà ta bấm vào lấy từ id, Khi bấm save thì sẽ thực hiện update category này (update name)



@app.route('/dashboard/save_category', methods=('GET', 'POST'))
def save_category():
    category_name = request.form['category_name']
    session['category_title'] = request.form['category_name']
    conn = sqlite3.connect('PostDB.db')
    select_query = '''
        SELECT * FROM category WHERE category_name = ?
    '''
    cur = conn.execute(select_query, (category_name, ))
    rows = cur.fetchall()
    if len(rows) > 0:
        session['msg'] = 'Category ' + category_name + ' is existed'
        return redirect(url_for('new_category'))
    else:
        insert_query = 'INSERT INTO category (category_name) VALUES (?) '
        cur2 = conn.execute(insert_query, (category_name,))
        conn.commit()
        category_lists = conn.execute('SELECT * FROM category')
        results = category_lists.fetchall()
        conn.close()
        msg = 'Insert ' + category_name + ' successfully'
        session.pop('category_title')
    return render_template('all-category.html', msg=msg, category_data = results)
@app.route('/save_contact', methods=('POST','GET'))
def save_contact():
    conn = sqlite3.connect('PostDB.db')
    name = request.form['name']
    email = request.form['email']
    sub = request.form.getlist('subject')
    subject = ''
    type1 = request.form['type']
    if len(sub) >0:
        for i in range(0, len(sub)):
            if i < (len(sub) - 1):
                subject = subject + sub[i] + ', '
            else:
                subject = subject + sub[i]
    if name or email =='':
        session['msg1'] = 'Your name or your email is null'
        session['name'] = name
        session['email'] = email
        return redirect(url_for('contact_form'))

        if email.count('@') == 0:
            session['msg1'] ='Your email must have charater:@'
            session['name']=name
            session['email'] = email
            return redirect(url_for('contact_form'))

        else:
            print(type1)
            message = request.form['message']
            conn.execute('INSERT INTO contact (username,email,subject,gender,message) VALUES(?,?,?,?,?)',(name, email, subject, type1, message))
            session.pop('msg1')
            conn.commit()
            conn.close()
            return render_template('contact_form.html')






    # return redirect(url_for('about')) # gọi ra route có function about
    # return redirect('/about') # gọi ra route có đường dẫn là /about

     #BTVN(2/10)
    # check contact form tương tự như check new category
    # name, message not null
    # email have @
    # phone number: must be a number
    # check input of contact form, return and show error if validation failed
    # If OK save to DB

@app.route('/check_login', methods=('GET', 'POST'))
def check_login():
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect('PostDB.db')
    select_user = 'SELECT * FROM users WHERE username=? AND password=?'
    cur = conn.execute(select_user, (username, password, ))
    row = cur.fetchall()
    count = len(row)
    # 1 record
    # 0 record: failed
    if count >0:
        session['username'] = username
        session['status'] = 1
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login'))
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
@app.route('/create_comment', methods=('POST', 'GET'))
def create_comment():
    # session['username'] = 'Nguyen Van A'
    # session.pop('username') # xóa session
    return render_template('create_comment.html')


@app.route('/save_comment', methods=('GET','POST'))
def save_comment():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    gender = request.form['gender']
    country = request.form['country']
    message = request.form['message']
    return render_template('save_comment.html')
@app.route('/contact_form', methods=('POST', 'GET'))
def contact_form():
    return render_template('contact_form.html')






if __name__ == '__main__':
    app.run()
