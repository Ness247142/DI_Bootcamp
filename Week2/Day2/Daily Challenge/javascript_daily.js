
let string1 = "not";
let string2 = "bad";
let testA = "This movie is not so bad";
let testB = testA.indexOf("not");
let testC = testA.indexOf("bad");
console.log(testB);
console.log(testC);


if((testA.includes("not")) && (testA.includes("bad")) && (testA.indexOf("not"))<testA.indexOf("bad")){
console.log(testA.slice(0, testA.indexOf("not")) + "good");
}

else {
console.log(testA);
}
