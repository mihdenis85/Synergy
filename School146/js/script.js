"use strict";
window.onscroll = function() {
  let elem = document.getElementById("header");
  let data = elem.getBoundingClientRect();
  console.log(data.y, data.height);
  if (data.y + data.height < 0) {
  	let menu = document.getElementById("top_menu");
  	menu.style = "position: fixed;";
    let logo = document.getElementById("top_menu_logo");
    logo.style = "opacity: 1; transition: 0.5s;";
  }
  else {
  	let menu = document.getElementById("top_menu");
  	menu.style = "position: static";
    let logo = document.getElementById("top_menu_logo");
    logo.style = "opacity: 0; transition: 0.5s;";
  }
}