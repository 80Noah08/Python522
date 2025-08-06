document.querySelector(".btn").onclick = function(){
    document.querySelector('img').hidden = !document.querySelector('img').hidden
}

function on(){
    const img = document.getElementById('img');
    img.hidden = false;
}
function off(){
    const img = document.getElementById('img');
    img.hidden = true;
}