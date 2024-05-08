function changeColor() {
  the_heading = document.getElementById("hello");
  the_heading.style.color = "red";
  console.log("I just changed the color to: " + the_heading.style.color)  
}

function changeSize() {
  the_heading = document.getElementById("hello");
  the_heading.style.fontSize = "x-large";
  console.log("I just change the shadowing to: " + the_heading.style["text-shadow"])
}

function changeShadow() {
  the_heading = document.getElementById("hello");
  the_heading.style["text-shadow"] = "3px 2px gray";
  console.log("I just change the shadowing to: " + the_heading.style["text-shadow"])
}
