from flask import Flask,render_template,request
from flask_caching import Cache
from Anilist import Anilist

app = Flask(__name__)
cache = Cache(app,config={'CACHE_TYPE': 'SimpleCache'})
obj = Anilist()

@app.route("/")
@cache.cached(timeout=200)
def index():
    c = obj.get_content()
    ta = obj.get_top_aring()
    tu = obj.get_top_upcoming()
    tan = obj.get_top_anime()
    tm = obj.get_top_manga()

    return render_template('index.html',c=c,ta=ta,tu=tu,tan=tan,tm=tm)

res = []
query = ''

@app.route("/search/<int:page>",methods=["POST", "GET"])
def search(page):
    global res,query
    
    if request.method == "POST":
        query = request.form['q']
        media = obj.search(query)
        res = [media[i:i+15] for i in range(0,len(media),15)]

    pageInfo = {
        'total':len(res),
        'page':page
    }
    return render_template('search.html',media=res[page-1],q=query,pi=pageInfo)

@app.route("/anime/<id>")
@cache.cached(timeout=200)
def anime(id):
    ani = obj.get_anime_details(id)

    return render_template('anime.html',ani=ani)

@app.route("/manga/<id>")
@cache.cached(timeout=200)
def manga(id):
    man = obj.get_manga_details(id)
    
    return render_template('anime.html',ani=man)

@app.route("/character/<id>")
@cache.cached(timeout=200)
def character(id):
    chr = obj.get_char_details(id)
    return render_template('character.html',chr=chr)

if __name__ == '__main__':
   app.run(debug=True)