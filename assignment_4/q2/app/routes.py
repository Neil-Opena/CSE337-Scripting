from flask import render_template, flash, redirect, url_for, request
from app import app
from app.operations import *
from app.forms import TextForm
from app.models import Post
from app import db

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = TextForm()
    if form.validate_on_submit():
        # get db data and edit it
        return redirect(url_for('showresult', operationname='wordcount'))
    return render_template('index.html', title='Home', form=form)

@app.route('/result/<operationname>')
def showresult(operationname):
    result = 'yeet'
    operation = 'Word Count'
    return render_template('result.html', title='Result', operation=operation, input='text', result=result)

app.errorhandler(403)
def forbidden_error(error):
    return render_template('403.html'), 403

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
