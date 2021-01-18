
let str = "This movie is not bad";
let not = /not/i;
let findnot = str.match(not);
let bad = /bad/i;
let findbad = str.match(bad);
console.log(findnot);
console.log(findbad);

let result = str.replace("not bad", "good");
console.log(result);