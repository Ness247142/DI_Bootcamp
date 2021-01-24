

// Create an array of planets of the solar system
// For each planet, in the array, create a div using createElement. This div should have a class named ‘planet’.
// Each planet should have a different background color. (Hint: add a new class to each planet)
// Finally append each div to the body.
// Bonus Do the same process for moons. Be careful, each planet has a certain amount of moons; How should you display them ?

let planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];

let colors = ["green", "white", "blue", "red", "yellow", "brown", "turquoise", "darkblue"]

for (let i = 0; i <= 7; i++) {
    let newDiv = document.createElement("div");
    let newClass = document.createTextNode(planets[i]);
    console.log(newDiv.appendChild(newClass));
    console.log(document.body.appendChild(newDiv));
    let SolarSystemclass = document.getElementsByTagName("div")[i].setAttribute("class", `planet planets${i}`);
    let planetBackgroundColor = document.getElementsByClassName("planet")[i].style.backgroundColor = colors[i];
    console.log(SolarSystemclass);
    console.log(planetBackgroundColor);
}
}


