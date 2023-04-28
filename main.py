from flask import Flask, render_template, abort, request, redirect, url_for,jsonify
from model import db, save

# Create Flask Application
app = Flask(__name__)

# home page view function / show all questions without answers


@app.route('/')
def home_page():
    return render_template('index.html', questions=db)


# show each question indivisually by its answer
@app.route('/questions/<int:index>')
def question_pages(index):
    try:
        return render_template('show_questions.html', question=db[index],
                               index=index,
                               max_index=len(db)-1)
    except IndexError:
        abort(404)


# Add new Question at the end of data
@app.route('/add_question', methods=['Get', 'POST'])
def add_new_question():
    if request.method == 'POST':
        new = {'question': request.form['question'],
               'answer': request.form['answer']}
        db.append(new)
        save(db)
        return redirect(url_for('home_page'))
    else:
        return render_template('create_new.html')


# remove question
@app.route('/remove_question/<int:index>', methods=['GET', 'POST'])
def remove_a_question(index):
    print(db[index])
    if request.method == 'POST':
        print('ooooooooooooooooooooooooo')
        del db[index]

        save(db)
        return redirect(url_for('home_page'))
    else:
        return render_template('remove_question.html', index=index)
    

#  API
@app.route('/api/questions')
def api_questions_list():
    return jsonify(db)


@app.route('/api/questions/<int:index>')
def api_question(index):
    try:
        return jsonify(db[index])
    except IndexError:
        abort(404)


# Run Application if module name is main
if __name__ == '__main__':
    app.run()
