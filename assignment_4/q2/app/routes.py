from flask import render_template, flash, redirect, url_for, request
from app import app
from app.operations import *
from app.forms import TextForm

# instead of using a data base, global variables were used since only one instance is needed
text = None
delimiter = ''

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    global text, delimiter
    form = TextForm()
    if form.validate_on_submit():
        text = form.text.data
        delimiter = form.delimiters.data
        operation = form.operations.data
        operation_name = None
        if(operation == 'a'):
            operation_name = 'wordcount'
        elif(operation == 'b'):
            operation_name = 'charactercount'
        elif(operation == 'c'):
            operation_name = 'mostfrequent5words'

        return redirect(url_for('showresult', operationname=operation_name))
    return render_template('index.html', title='Home', form=form)

@app.route('/result/<operationname>')
def showresult(operationname):
    global text, delimiter

    if(operationname == None):
        return render_template('404.html'), 404
    if(text == None):
        return render_template('500.html'), 500

    if(operationname == 'wordcount'):
        operation_text = 'Word Count'
        result = word_count(text, delimiter)
    elif(operationname == 'charactercount'):
        operation_text = 'Character Count'
        result = character_count(text)
    else:
        operation_text = 'Most Frequent 5 Words'
        result = frequent_five_words(text, delimiter)

    return render_template('result.html', title='Result', operation=operation_text, input=text, result=result)

app.errorhandler(403)
def forbidden_error(error):
    return render_template('403.html'), 403

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
