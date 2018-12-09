from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import SubmissionForm
from app.models import Post
from app import db


@app.route('/')
@app.route('/index')
def index():
    current_posts = Post.query.all()
    return render_template('index.html', title='Home', posts=current_posts)

@app.route('/posts/<postid>')
def showpost(postid):
    current_posts = Post.query.filter_by(id=postid)
    return render_template('showpost.html', title='Show Post', post=current_posts[0])

@app.route('/submit', methods=['GET', 'POST'])
def submitpage():
    form = SubmissionForm()
    if form.validate_on_submit():
        flash('Topic {} has been submitted.'.format(
            form.title.data))
        new_title = form.title.data
        new_text = form.text.data
        p = Post(title=new_title,body=new_text)
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('submit.html',  title='Submit New Entry', form=form)
