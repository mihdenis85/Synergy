"use strict";
window.onscroll = function() {
  let elem = document.getElementById("top_menu");
  let data = elem.getBoundingClientRect();
  if (data.y <= 0) {
  	let menu = document.getElementById("usual_menu");
  	menu.style = "opacity: 1; transition: 0.5s;"
  }
  else {
  	let menu = document.getElementById("usual_menu");
  	menu.style = "opacity: 0; transition: 0.5s;"
  }
}