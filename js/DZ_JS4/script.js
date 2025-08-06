let months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"];

function divClr(){
    let r = Math.floor(Math.random() * 256);
    let g = Math.floor(Math.random() * 256);
    let b = Math.floor(Math.random() * 256);
    let styleClr = `rgb(${r},${g},${b})`
    return styleClr  
}

for(let i = 0; i < months.length; i++){
    document.writeln("<div id='"+ i +"'></div>");
    let id = document.querySelectorAll("div")[i];
    id.style.textAlign = "center";
    id.style.height = "75px";
    id.style.fontWeight = "bold";
    id.style.fontSize = "30px";
    id.style.background = divClr();
    id.innerHTML = months[i];

}