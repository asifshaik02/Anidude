from flask import Flask
from flask import render_template
from Anilist import Anilist

app = Flask(__name__)
obj = Anilist()

@app.route("/")
def index():
    c = obj.get_content()
    ta = obj.get_top_aring()
    tu = obj.get_top_upcoming()
    tan = obj.get_top_anime()
    tm = obj.get_top_manga()

    return render_template('index.html',c=c,ta=ta,tu=tu,tan=tan,tm=tm)

@app.route("/anime/<id>")
def anime(id):
    ani = obj.get_anime_details(id)

    return render_template('anime.html',ani=ani)

@app.route("/manga/<id>")
def manga(id):
    man = obj.get_manga_details(id)
    
    return render_template('anime.html',ani=man)

@app.route("/character/<id>")
def character(id):
    chr = obj.get_char_details(id)
    return render_template('character.html',chr=chr)

if __name__ == '__main__':
   app.run(debug=True)