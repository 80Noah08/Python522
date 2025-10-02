function Person(name, age, job) {
    this.name = name;
    this.age = age;
    this.job = job;
    this.who = function () {
        document.writeln(`<p>Я <b>${this.name}</b> мне <b>${this.age}</b> лет. Я работаю <b>${this.job}ом</b>.</p>`)
    };

};

let pers1 = new Person("Дмитрий", 26, "Дизайнер");
let pers2 = new Person("Станислав", 29, "Программист");
let pers3 = new Person("Сергей", 35, "Менеджер");

let arr = [pers1, pers2, pers3];
for (let i = 0; i < arr.length; i++) {
    arr[i].who();

}