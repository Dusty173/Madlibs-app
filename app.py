from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secret'

# debug = DebugToolbarExtension(app)


@app.route('/')
def ask_user():
    """Generate/display form to ask for words"""
    prompts = story.prompts

    return render_template("qform.html", prompts=prompts)

@app.route('/story')
def display_story():
    """Show the result of the madlib story"""
    text = story.generate(request.args)

    return render_template('story.html', text=text)