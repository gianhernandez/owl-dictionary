from flask import Flask, render_template, redirect, url_for, flash
import requests
from flask_bootstrap import Bootstrap
from forms import FindWord
import os
from dotenv import load_dotenv


app = Flask(__name__)
Bootstrap(app)


load_dotenv('.env')
app.config['SECRET_KEY'] = os.getenv('OWL_SECRET_KEY')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = FindWord()

    if form.validate_on_submit():

        word = form.title.data
        params = {
            'Authorization': 'Token e1f563785854f465a1769b928a79ee436c81382d',
            'word': word
        }

        try:
            site = requests.get(f'https://owlbot.info/api/v4/dictionary/{word}', headers=params).json()
            word_searched = site['word'].capitalize()
            emoji = site['definitions'][0]['emoji']
            definition = site['definitions'][0]['definition']
            img = site['definitions'][0]['image_url']
            example = site['definitions'][0]['example']
            form.title.data = ''

        except ValueError:
            flash('The word you searched do not exist in this dictionary.')
            return redirect(url_for('home'))
        except TypeError:
            flash('The word you searched do not exist in this dictionary.')
            return redirect(url_for('home'))

        return render_template('index.html', word=word, site=site, form=form, definition=definition, img=img,
                               word_searched=word_searched, emoji=emoji, example=example)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()
