# routes.py

import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

from flask import Response, render_template

from . import app
from .forms import SmuleForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SmuleForm()
    if form.validate_on_submit():
        song_url = form.url.data

        http_resp = requests.get(
            song_url, headers={'User-Agent': UserAgent().random})

        if not http_resp.ok:
            form.url.errors.append('Link invalid or does not exist')
            return render_template('index.html', form=form)

        soup = BeautifulSoup(http_resp.text, 'html.parser')

        media_url = soup.find(
            attrs={'name': 'twitter:player:stream'})['content']
        media_title = soup.find(
            attrs={'name': 'twitter:description'})['content']

        file_name = media_title[:media_title.index(
            "on Smule.")].strip().replace("/", " - ") + '.mp4'

        media_stream = requests.get(media_url, stream=True)

        response = Response(
            media_stream, content_type=media_stream.headers['Content-Type'])
        response.headers['Content-Disposition'] = f'attachment; filename={file_name}'

        return response

    return render_template('index.html', form=form)
