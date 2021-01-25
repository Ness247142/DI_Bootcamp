

// Exercise 2

//Create a list of all bold items 
let bold_items = document.getElementsByTagName("strong"); 

// Call the function highlight() onMouseOver and the function return_normal() onMouseOut
newEvent.addEventListener("mouseover", highlight)
newEvent.addEventListener("mouseout", return_normal)
 
// Create a function called : getBold_items() that takes no parameter. This function has to collect all the bold items inside the paragraph.
function getBold_items() 
{
  bold_items = document.querySelectorAll("strong");
  return bold_items;
}

// Create a function called : highlight() that changes the color of each bold item to blue.
function highlight(event) {         
    console.log("event : ", event.target)

   for (let i = 0; i < bold_items.length; i++)
   {                                                    
    bold_items[i].style.color = "blue";
    }
}

// Create a function called : return_normal() that changes the color of each bold item to black.
function return_normal(event){ 
    console.log("event : ", event.target)
    for (let i = 0; i < bold_items.length; i++) 
  {
       bold_items[i].style.color = "black";
  }
}

