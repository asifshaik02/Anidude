function slide(dir,index) {
    if (dir == 'left') {
        document.getElementById(index).scrollBy({left:-184,behavior:'smooth'})
    }
    else{
        document.getElementById(index).scrollBy({left:+184,behavior:'smooth'})
    }
}