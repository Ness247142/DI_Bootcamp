// Create a variable which value is the concatenation of the two strings (separated by a space) slicing out and swapping the first 2 characters of each.

let string1 = "Boy";
let string2 ="Girl";
let string3 = string1.replace("h", "w") + string2.replace("w", "h");
let string4 = string1.substring(0,string1.length-1) + string2.substring(string2.length-1);
console.log(string4)

let string5 = string2.substring(0,string2.length-1) + string1.substring(string1.length-1);
console.log(string5)

function mixUp(mix, pod) {
    return pod.slice(0, 2) + mix.slice(2) + " " + mix.slice(0, 2) + pod.slice(2);
  }
  
console.log(mixUp('mix', 'pod'));
