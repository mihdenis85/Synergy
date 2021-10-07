"use strict";

function str(n) {
  return n.toString();
}

window.onscroll = function() {
  let elem = document.getElementById("slider");
  let data = elem.getBoundingClientRect();
  if (data.y + data.height >= 0) {
    let logo = document.getElementById("top_menu_logo");
    logo.style = "transform: rotate(-360deg); transition: 0.5s; width: 0%;";
    let menu = document.getElementById("top_menu");
    menu.style = "width: 100%; transition: 0.5s";
  }
  else {
    let logo = document.getElementById("top_menu_logo");
    logo.style = "transform: rotate(360deg); transition: 0.5s; width: 3%;";
    let menu = document.getElementById("top_menu");
    menu.style = "width: 90%; transition: 0.5s";
  }
}

var images = ["slider_image_0.png", "slider_image_1.png", "slider_image_2.png"];
var now = 2;
var header = ["Lorem", "Ipsum", "Dolor"];
var text = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit", "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua", "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat"];
var article_img = ["article_img_0.png", "article_img_1.png", "article_img_2.png", "article_img_3.png"]

function main() {
  let slide = document.getElementById("slider");
  slide.style = "background: url(../static/img/" + images[now] + ") no-repeat center; transition: 0.5s; background-size: 50% auto;";
  setTimeout(() => {
     slide.style = "background: url(../static/img/" + images[now] + ") no-repeat center; transition: 0.5s; background-size: 100% auto;";
  }, 500)
  let slider_h = document.getElementById("slider_h");
  slider_h.style = "opacity: 0;";
  setTimeout(() => {
      slider_h.innerHTML = header[now];
      slider_h.style = "transition: 0.5s; opacity: 1;";
    }, 500);
  let slider_text = document.getElementById("slider_text");
  slider_text.style = "opacity: 0;";
  setTimeout(() => {
      slider_text.innerHTML = text[now];
      slider_text.style = "transition: 0.5s; opacity: 1;";
    }, 500);
  for (let i = 0; i < 4; i++) {
    let img = document.getElementById("article_img_" + str(i));
    img.style = "background: url(../static/img/" + article_img[i] + ") no-repeat;";
  }
}
function setup() {
  let slide = document.getElementById("slider");
  slide.style = "background: url(../static/img/" + images[now] + ") no-repeat center; transition: 0.5s; background-size: 50% auto;";
  setTimeout(() => {
     slide.style = "background: url(../static/img/" + images[now] + ") no-repeat center; transition: 0.5s; background-size: 100% auto;";
  }, 500)
  let slider_h = document.getElementById("slider_h");
  slider_h.style = "transition: 0.5s; opacity: 0; transform: translateY(40vh);";
  setTimeout(() => {
      slider_h.innerHTML = header[now];
      slider_h.style = "transition: 0.5s; opacity: 1;";
    }, 500);
  let slider_text = document.getElementById("slider_text");
  slider_text.style = "transition: 0.5s; opacity: 0; transform: translateY(40vh);";
  setTimeout(() => {
      slider_text.innerHTML = text[now];
      slider_text.style = "transition: 0.5s; opacity: 1;";
    }, 500);
}

function next_slide() {
  now -= 1;
  if (now < 0) {
    now += 3;
  }
  setup(now);
}

function prev_slide() {
  now += 1;
  if (now >= 3) {
    now -= 3;
  }
  setup(now);
}