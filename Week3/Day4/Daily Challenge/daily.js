

function pyramid() {
    let n = 4;
    let output = " ";
    for (let i = 0; i <= n; i++) {
        let star = " ";
        for (let j = 0; j < (n - i); j++)
            star += " ";
        for (let k = 0; k <= 2 * i; k++)
            output += "* ";
        console.log(star + output);
        output = " ";
    }
}

pyramid(4);
