let post = document.getElementsByClassName("project-post");
let scroll = window.scrollY;


function slideIn(arr) {
    for (let p of arr) {
        let rect = p.getBoundingClientRect();
        if ((window.innerHeight / 2) > rect.top) {
            p.classList.add("slideIn");
        }
    }
}

window.addEventListener('scroll', ()=>{
    slideIn(post)
});


