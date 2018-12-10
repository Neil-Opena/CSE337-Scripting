from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import TextForm
from app.operations import *
from flask_login import login_user, logout_user, current_user, login_required


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = TextForm()
    if form.validate_on_submit():
        print(form.text.data)
        print(form.operations.data)
        print(form.delimiters.data)
        return render_template('404.html')
    return render_template('index.html', title='Home', form=form)

@app.route('/result/<operationname>')
def showresult(operationname):
    return render_template('500.html')

# @app.route('/posts/<postid>')
# def showpost(postid):
    # if current_user.is_authenticated:
        # current_post = Post.query.filter_by(id=postid)[0]
        # author = current_post.author #User.query.filter_by(id=current_post.user_id).first_or_404()
        # return render_template('showpost.html', title='Show Post', post=current_post, author=author)
    # return render_template('notloggedin.html')

# @app.route('/submit', methods=['GET', 'POST'])
# def submitpage():
#     if current_user.is_authenticated:
#         #print(current_user)
#         form = SubmissionForm()
#         if form.validate_on_submit():
#             flash('Topic {} has been submitted.'.format(
#                 form.title.data))
#             new_title = form.title.data
#             new_text = form.text.data
#             user_id = current_user.id
#             p = Post(title=new_title,body=new_text,user_id=user_id)
#             #print(p.user_id)
#             db.session.add(p)
#             db.session.commit()
#             return redirect(url_for('index'))
#         return render_template('submit.html',  title='Submit New Entry', form=form)
#     return render_template('notloggedin.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
