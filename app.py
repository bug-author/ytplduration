from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import datetime
import ytpl
from forms import Link

app = Flask(__name__)
app.config['SECRET_KEY'] = '9021cbfa'


@app.route('/', methods=['GET', 'POST'])
def search():
    form = Link()
    invalid = {'msg': ''}
    if form.validate_on_submit():
        try:
            time = ytpl.playlist_duration_finder(form.link.data)
            no_of_videos = ytpl.total_videos()
            flash(no_of_videos)
            flash(time)
            ytpl.reset_video_length()
        except:
            invalid['msg']='Sorry you entered an invalid link, try again!'
    return render_template('index.html', form=form, invalid=invalid)


if __name__ == '__main__':
    app.run()
