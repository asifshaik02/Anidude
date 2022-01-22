import re
import markdown
import requests

class Anilist:
    def __init__(self):
        self.base_url = 'https://graphql.anilist.co'
        self.month = {
            1:'Jan',
            2:'Feb',
            3:'Mar',
            4:'Apr',
            5:'May',
            6:'Jun',
            7:'Jul',
            8:'Aug',
            9:'Sept',
            10:'Oct',
            11:'Nov',
            12:'Dec'
        }

    def get_content(self):
        query = '''
        {
            Page(page: 1, perPage: 8) {
                media(sort: TRENDING_DESC,type: ANIME) {
                    id
                    title {
                        english
                    }
                    description
                    bannerImage
                }
            }
        }
        '''
        r = requests.post(self.base_url, json={'query': query})
        res = []

        for row in r.json()['data']['Page']['media']:
            d = {}
            d['id'] = row['id']
            d['title'] = row["title"]['english']
            d['img'] = row['bannerImage']
            d['descrption'] = row['description']
            res.append(d)
        
        return res
    
    def get_top(self,_type,status=None):
        if status:
            query = '''
            query ($status: MediaStatus, $type: MediaType){
                Page(page: 1, perPage: 10) {
                    media(sort: POPULARITY_DESC, status: $status, type: $type) {
                    id
                    title {
                        english
                        romaji
                    }
                    coverImage {
                        large
                    }
                    startDate {
                        year
                        month
                    }
                    format
                    averageScore
                    }
                }
            }
            '''
            variables = {
                'status' : status,
                'type' : _type
            }
        else:
            query = '''
            query ($type: MediaType){
                Page(page: 1, perPage: 10) {
                    media(sort: POPULARITY_DESC,type: $type) {
                    id
                    title {
                        english
                    }
                    coverImage {
                        large
                    }
                    startDate {
                        year
                        month
                    }
                    format
                    averageScore
                    }
                }
            }
            '''
            variables = {
                'type' : _type
            }

        r = requests.post(self.base_url, json={'query': query, 'variables': variables}).json()
        res = []
        for row in r['data']['Page']['media']:
            d = {}
            d['id'] = row['id']

            if row['title']['english']:
                d['title'] = row['title']['english']
            else:
                d['title'] = row['title']['romaji']

            d['img'] = row['coverImage']['large']
            if row['startDate']['month'] and row['startDate']['year']:
                d['date'] = f"{self.month[row['startDate']['month']]} {row['startDate']['year']}"
            else:
                d['date'] = ''
            d['format'] = row['format']
            if status == 'RELEASING' or status == None:
                d['score'] = row['averageScore']
            res.append(d)
        return res

    def get_top_aring(self):
        return self.get_top('ANIME','RELEASING')
     
    def get_top_upcoming(self):
        return self.get_top('ANIME','NOT_YET_RELEASED')

    def get_top_anime(self):
        return self.get_top('ANIME')

    def get_top_manga(self):
        return self.get_top('MANGA')

    def get_details(self,_type,id):
        query = '''
        query($id:Int){
            Media(id:$id){
                title{
                    english
                    romaji
                }
                type
                coverImage{
                    large
                }
                genres
                description
                averageScore
                startDate{
                    day
                    month
                }
                episodes
                duration
                volumes
                chapters
                idMal
                id
                season
                seasonYear
                characters(page:1,perPage:6,sort:ROLE) {
                    nodes{
                        id
                        image {
                            medium
                        }
                        name {
                            first
                            middle
                            last
                        }
                    }
                }
            }
        }
        '''
        variables = {
            'id':id
        }
        r = requests.post(self.base_url, json={'query': query, 'variables': variables}).json()['data']['Media']

        res = {}
        if r['title']['english']:
            res['title'] = r['title']['english']
        else:
            res['title'] = r['title']['romaji']

        res['subTitle'] = r['title']['romaji']
        res['img'] = r['coverImage']['large']
        res['type'] = r['type']
        res['genres'] = ", ".join(map(str,r['genres']))
        res['description'] = r['description']
        res['score'] = f"{r['averageScore']}".replace('None','0')
        try:
            res['date'] = f"{r['startDate']['day']} {self.month[r['startDate']['month']]}"
        except:
            res['date'] = ''
        res['season'] = r['season']
        res['seasonYear'] = r['seasonYear']
        res['anilist'] = f'https://anilist.co/{_type}/{id}'.lower()
        res['mal'] = f'https://myanimelist.net/{_type}/{r["idMal"]}'.lower()
        res['char'] = []
        if _type == 'ANIME':
            res['epi'] = r['episodes']
            res['duration'] = r['duration']

        elif _type == 'MANGA':
            res['vol'] = r['volumes']
            res['chapter'] = r['chapters']
        
        for ch in r['characters']['nodes']:
            char = {}
            char['id'] = ch['id']
            char['name'] = f"{ch['name']['first']} {ch['name']['middle']} {ch['name']['last']}".replace('None',"")
            char['img'] = ch['image']['medium']
            res['char'].append(char)
        
        return res

    def get_anime_details(self,id):
        return self.get_details('ANIME',id)

    def get_manga_details(self,id):
        return self.get_details('MANGA',id)

    def get_char_details(self,id):
        query = '''
        query($id:Int){
            Character(id: $id) {
                name {
                    first
                    middle
                    last
                }
                image {
                    large
                }
                gender
                description
                media(sort:POPULARITY_DESC) {
                    edges {
                        node {
                            id
                            type
                            title {
                                romaji
                                english
                            }
                            coverImage {
                                large
                            }
                        }
                    }
                }
            }
        }
        '''
        variables = {
            'id':id
        }

        r = requests.post(self.base_url, json={'query': query, 'variables': variables}).json()['data']['Character']
        res = {}
        res['name'] = f"{r['name']['first']} {r['name']['middle']} {r['name']['last']}".replace('None',"")
        res['img'] = r['image']['large']
        res['gender'] = f"{r['gender']}".replace('None',' ')[0]
        res['description'] = markdown.markdown(re.sub('[~!].*[!~]','',r['description']), extensions=['md_in_html'])
        res['realtions'] = []

        for rel in r['media']['edges']:
            data = {}
            data['id'] = rel['node']['id']
            data['type'] = rel['node']['type']
            if rel['node']['title']['english']:
                data['title'] = rel['node']['title']['english']
            else:
                data['title'] = rel['node']['title']['romaji']
            data['img'] = rel['node']['coverImage']['large']
            res['realtions'].append(data)
        return res

    def search(self,q):
        query = '''
        query($q:String){
            Page{
                media(search:$q,sort:SEARCH_MATCH,isAdult:false){
                    id
                    title{
                        english
                        romaji
                    }
                    type
                    coverImage{
                        large
                    }
                }
                pageInfo{
                    total
                    lastPage
                    currentPage
                }
            }
        }
        '''
        variables = {
            'q':q
        }
        r = requests.post(self.base_url, json={'query': query, 'variables': variables}).json()['data']['Page']['media']

        res = []
        for media in r:
            d = {}
            d['id'] = media['id']

            if media['title']['english']:
                d['title'] = media['title']['english']
            else:
                d['title'] = media['title']['romaji']

            d['img'] = media['coverImage']['large']
            d['type'] = media['type'].lower()
            res.append(d)
        return res