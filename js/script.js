"use strict"
/* let message; // let, const, var
message = "Hello";
console.log(message);

let a = 10;
a = 3.5;

let b, c;
let d = 6, e = 2;

let firstName = "Irina";
console.log(firstName);
 */

// const week = 7;

// let str1 = "Двойные кавычки"
// let str2 = 'Одинарные кавычки'
// let str3 = `Обратные ${5 + 9}
// кав     ыч      ки`
// console.log(str1);
// console.log(str2);
// console.log(str3);

// let first_name = "Ivan";
// alert(`Hello, ${first_name}`);

// let day = 365;
// let planet = "Земля";
// let people = "7млрд.";
// let sun = 'Солнца'
// alert(`Мы живем на планете ${planet}, она делает один оборот вокруг ${sun} за ${day} дней. Население нащей планеты составляет примерно ${people} человек`)

// let res = confirm("Знаете ли вы HTML?");
// console.log(res);
// if(res){
//     alert("Пора учить JavaScript")
// }
// else {
//     alert("Нужно выучить")
// }

/* let number = 13;
console.log(number, typeof number);

let a = 23.56;
console.log(a, typeof(a));

let b = "Hello";
console.log(b, typeof(b));

let c = true;
console.log(c, typeof(c));

let d = null;
console.log(d, typeof(d));

let e = undefined;
console.log(e, typeof(e)); */

// let res = prompt("Ваше имя:", "Значение по умолчанию");
// console.log(res)

/* let a = 12;
let b = 8;
console.log('+:', a + b);
console.log('-:', a - b);
console.log('*:', a * b);
console.log('/:', a / b);
console.log('%:', a % b);
console.log('**:', a ** b); */

/* let a = 23;
let b = "6";
console.log(a + b); */

/* let a = +prompt("Введите первое число:", 5);
let b = +prompt("Введите второе число:", 3);
/* a = parseInt(a)
b = parseInt(b) */
// alert("Результат: " + (a + b)); 


/* console.log(parseInt("21.84")); // 21
console.log(parseFloat("21.84")); // 21.84
console.log(parseFloat("21.84123").toFixed(2)); 
console.log(+"21.84"); 
console.log(-"21.84"); 
console.log(+true); 
console.log(+false);  */

/* let a = 0 , b = 0;
a++;
b--;
console.log(a)
console.log(b) */

/* let a = 0 , b = 0;
a++;
++b;
console.log(a)
console.log(b) */

/* let a = 0 , b = 0;
let c = a++ + 2;
let d = ++b + 2;
console.log(a) // 1
console.log(b) // 1
console.log(c) // 2
console.log(d) // 3 */

/* let a = 1;
let b = a++; // b = 1, a = 2
let c = b + 5 + a; // c = 
console.log(c); // 8 */

/* let a = 1;
let b = ++a; // b = 2, a = 2
let c = b + 5 + a; // c = 2 + 5 + 2
console.log(c); // 9
 */

/* let num = 10;

num += 5;
console.log(num); // 15

num -= 7;
console.log(num); // 8

console.log(5 > 3);
console.log(5 < 3);
console.log(5 <= 5);
console.log(5 >= 5);
console.log(5 == "5");
console.log(5 === "5");
console.log(5 != "5");
console.log(5 !== "5"); */

// 7 > 3 ? alert("7") : alert("3");

/* let ch = prompt("Угадайте число от 1 до 10");
let num = 7;
// (ch == num) ? alert("Угадали") : alert("Не угадали");
(ch == num) ? alert("Угадали") : (ch < num) ? alert("Загаданное число больше") : alert("Загаданное число меньше"); */

/* if (условие){
    блок истина
} else {блок ложь} */

/* a = 0;
if (a){
    console.log("TRUE");
    
} else{
    console.log("FALSE");
    
} */

/* let a = +prompt("Введите первое число:", 5)
let b = +prompt("Введите второе число:", 0)

if (b != 0)
    alert(a/b);
else
    alert("На ноль делить нельзя") */

/* let a = 12;
let b = 6;

if (a > b){
    alert(a + " > " + b);
}if(a < b){
    alert(a + " < " + b)
}
if(a == b){
    alert(a + "==" + b)
} */

/* if (a > b){
    alert(a + " > " + b);
}else if(a < b){
    alert(a + " < " + b)
}
else{
    alert(a + "==" + b)
} */
/* if (a > b){
    alert(a + " > " + b);
}else{
    alert(a + " < " + b)
} */

/* let login = prompt("Введите логин: ")
if (login){
    if (login == 'admin'){
        let psw = prompt("Введите пароль: ");
        if (psw){
            if (psw == 'password'){
                alert("Добро пожаловать!")
            } else{
                alert("Пароль не верен")
            }
        } else{
            alert("Вход отменен")
        }
    } else{
        alert("Я вас не знаю")
    }

} else{
    alert("Вход отменен");
} */
/* let a = 1;
if (a){
    let b = 5;
}
    console.log(b); */
    
// let a = 5;
// console.log(a);

/* if (5 == 5 || 5 > 7){
    console.log("TRUE");
    
} else{
    console.log("FALSE");
    
} */
// console.log(!9);

/* let age = prompt("Введите возраст: ");
if(age > 17 && age < 70){
    alert("Вы можете получать права");
} else{
    alert("Права не давать")
} */

/*     let age = prompt("Введите возраст: ");
if(  18 > age || age > 69){
    alert("Права не давать");
} else{
    alert("Вы можете получать права")
} */

/* switch(условие){
    case значение_1:
        блок кода;
        break;
    case значение_2:
        блок кода;
        break;
        default:
            блок кода;
} */

/* let a = +prompt("Введите число: ");
switch(a){
    case 1:
        alert("Код 1");
        break;
    case 2:
        alert("Код 2");
        break;
    case 3:
        alert("Код 3");
        break;
    default:
        alert("Я таких значений не знаю")
} */

/*         let a = +prompt("Введите результат '2 + 2': ");
switch(a){
    
    case 4:
        alert("Верно");
         break;
    case 3:   
    case 5:
        alert("Не верно");
        break;
        
    default:
        alert("Я таких значений не знаю")
} */

let m = +prompt("Введите номер месяца");
let n;
switch(m){
    case 1: n = "Январь"; break;
    case 2: n = "Февраль"; break;
    case 3: n = "Март"; break;
    case 4: n = "Апрель"; break;
    case 5: n = "Май"; break;
    case 6: n = "Июнь"; break;
    case 7: n = "Юиль"; break;
    case 8: n = "Август"; break;
    case 9: n = "Сентябрь"; break;
    case 10: n = "Октябрь"; break;
    case 11: n = "Ноябрь"; break;
    case 12: n = "Декабрь"; break;
    default: n="Неправильный номер месяца";
}
alert("Вы ввели: " + n);