# AniDude
A website to browse your favorite Anime, Manga and its characters.Don't know what to watch? we got you covered, take a look at popular anime and manga, look what's trending, top aring anime shows.

# Run on your machine

## 1. Clone this repo:

    git clone https://github.com/asifshaik02/Anidude.git

    cd Anidude


## 2. configure Environment:

    virtualenv env

    For windows:  
    `\env\Scripts\activate.bat`

    For linux:
    `source env/bin/activate`

## 3. Installing requirements:

    pip install -r requirements.txt

## 4. Run on localhost:
    python3 app.py

# Anilist wrapper guide:

This wrapper class contains functions like:
1. [get_content()](#1)
2. [get_top_aring()](#2)
3. [get_top_upcoming()](#3)
4. [get_top_anime()](#4)
5. [get_top_manga()](#5)
6. [get_anime_details(id: int)](#6)
7. [get_manga_details(id: int)](#7)
8. [get_char_details(id: int)](#8)

### Examples

<div id="1"></div>

**get_content()**

    {
        descrption: "Gold Roger was known as the Pirate King, the strongest....
        img: "https://s4.anilist.co/file/anilistcdn/media/anime/banner/21-wf...
        title: "ONE PIECE"
    }
<div id="2"></div>

**get_top_aring()**

    {
        date: "Oct 1999"
        format: "TV"
        id: 21
        img: "https://s4.anilist.co/file/anilistcdn/media/anime/cover/mediu..."
        score: 86
        title: "ONE PIECE"
    }
<div id="3"></div>

**get_top_upcoming()**

    {
        date: "Jan 2022"
        format: "TV"
        id: 131681
        img: "https://s4.anilist.co/file/anilistcdn/media/anime/cover/mediu..."
        title: "Attack on Titan Final Season Part 2"
    }
<div id="4"></div>

**get_top_anime()**

    {
        date: "Apr 2013"
        format: "TV"
        id: 16498
        img: "https://s4.anilist.co/file/anilistcdn/media/anime/cover/mediu..."
        score: 85
        title: "Attack on Titan"
    }
<div id="5"></div>

**get_top_manga()**

    {
        date: "Sept 2009"
        format: "MANGA"
        id: 53390
        img: "https://s4.anilist.co/file/anilistcdn/media/manga/cover/mediu..."
        score: 86
        title: "Attack on Titan"
    }
<div id="6"></div>

**get_anime_details(id: int)**

    {
        anilist: "https://anilist.co/anime/16498"
        char: [
            {
                id: 46494
                img: "https://s4.anilist.co/file/anilistcdn/character/medi.."
                name: "Armin  Arlert"
            }
            .
            .
        ]
        date: "7 Apr"
        description: "Several hundred years ago, humans were nearly extermin...
        duration: 24
        epi: 25
        genres: (4) ['Action', 'Drama', 'Fantasy', 'Mystery']
        img: "https://s4.anilist.co/file/anilistcdn/media/anime/cover/mediu..."
        mal: "https://myanimelist.net/anime/16498"
        score: 85
        season: "SPRING"
        seasonYear: 2013
        subTitle: "Shingeki no Kyojin"
        title: "Attack on Titan"
    }
<div id="7"></div>

**get_manga_details(id: int)**

    {
        anilist: "https://anilist.co/manga/53390"
        chapter: 141
        char:[
            {
                id: 40881
                img: "https://s4.anilist.co/file/anilistcdn/character/med..."
                name: "Mikasa  Ackerman"
            }
            .
            .
        ]
        date: "9 Sept"
        description: "In this post-apocalyptic sci-fi story, humanity has be...
        genres: (4) ['Action', 'Drama', 'Fantasy', 'Mystery']
        img: "https://s4.anilist.co/file/anilistcdn/media/manga/cover/medi...
        mal: "https://myanimelist.net/manga/53390"
        score: 86
        season: ""
        seasonYear: ""
        subTitle: "Shingeki no Kyojin"
        title: "Attack on Titan"
        vol: 34
    }

<div id="8"></div>

**get_char_details(id: int)**

    {
        gender: "F"
        img: "https://s4.anilist.co/file/anilistcdn/character/large/b40..."
        name: "Mikasa  Ackerman"
        descrption: "<p><strong>Height:</strong> 170 cm (5'7\")\n<strong>Posi..
        realtions:[
            {
                id: 16498
                img: "https://s4.anilist.co/file/anilistcdn/media/anime/cov..."
                title: "Attack on Titan"
            }
            .
            .
        ]
    }