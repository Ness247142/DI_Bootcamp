
// function clickParagraph() {
//     console.log("hello")
//     document.getElementById("p").style.backgroundColor = "yellow"
//     document.getElementById("p").classList.toggle("welcomeUsers")
// }

// document.getElementById("p").onclick = function(){
//     console.log("hello");
//     document.getElementById("p").classList.toggle("welcomeUsers")
// }


// Exercise 1
// Write a JavaScript function to add rows to a table. Use the code below as a base
function insert_Row() { // Function for inserting a new row each time the button is clicked on
    let a = document.getElementById("sampleTable").insertRow(2); //New variable for a new row.
    
    let b = a.insertCell(0); // New variable for the first cell
    let c = a.insertCell(1); // New variable for the second cell
    
    b.innerHTML= "New Cell1"; // Insert text in the first cell
    c.innerHTML= "New Cell2"; // Insert text in the second cell
    }

    // Solution of Lize
    // function insert_Row() {
    //     // access the table
    //     let tableHtml = document.getElementById("sampleTable")
    //     //create a row
    //     let rowHtml = document.createElement("tr")
    //     //create 2 cells (or columns)
    //     for (let i = 0; i<2; i++){
    //         //create a column
    //         let columnHtml = document.createElement("td")
    //         //add text content to the column
    //         let contentCell = document.createTextNode(`Row New cell${i+1}`)
    //         //add the text node to the column
    //         columnHtml.appendChild(contentCell)
    //         //add the column to the row
    //         rowHtml.appendChild(columnHtml)
    //     }
    //   add row to the table
    //     tableHtml.appendChild(rowHtml)
    // }


    let paragraph = document.getElementById("p")
    paragraph.addEventListener("click", clickParagraph)

    let listShopping = document.getElementById("list")
    listShopping.addEventListener("click", clickParagraph)

    function clickParagraph(event) {
        console.log("event : ", event.target)
        //the paragraph
        event.target.style.backgroundColor = "yellow"
    }

    // Exercise 2
    // Add a few event listener to the button. The event listeners should change the style of the button

    let newEvent = document.getElementById("jsstyle")
    newEvent.addEventListener("click", newButton)
    newEvent.addEventListener("mouseover", newButton)
    newEvent.addEventListener("mouseout", newButton)

    function newButton(event) {
        console.log("event : ", event.target)
        event.target.style.backgroundColor = "blue"
        event.target.innerHTML = "Hello World"
        event.target.style.color = "white"
    }

    let form = document.forms[0]
    let buttonHTML = formHTML.elements[1]
    buttonHTML.addEventListener("click", retrieveInput)

    function retrieveInput(event) {
        //prevent the button to refresh my page
        event.preventDefault()
        let inputHTML = event.target.previousElementSibling

        let divHTML = document.getElementById("container")
        //create a paragraph
        let p = document.createElement("p")
        // create a text node
        let content = document.createTextNode(inputHTML.value)
        // append the text node to the paragraph
        p.appendChild(content)
        // append the div to the div
        divHTML.appendChild(p);
    }
