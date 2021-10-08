"use strict";

function str(n) {
  return n.toString();
}

var content_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Morbi tempus iaculis urna id volutpat lacus laoreet. Gravida rutrum quisque non tellus orci ac auctor augue. Elementum integer enim neque volutpat ac. Amet venenatis urna cursus eget nunc scelerisque. Duis tristique sollicitudin nibh sit amet commodo nulla facilisi nullam. Egestas sed sed risus pretium quam. Urna id volutpat lacus laoreet non curabitur gravida. Pellentesque adipiscing commodo elit at. Fringilla est ullamcorper eget nulla facilisi etiam dignissim. Diam quam nulla porttitor massa id neque aliquam vestibulum. Duis at tellus at urna condimentum mattis pellentesque id. Dignissim suspendisse in est ante in nibh mauris cursus mattis. Sit amet luctus venenatis lectus magna. In iaculis nunc sed augue lacus viverra. Pretium viverra suspendisse potenti nullam. Mi quis hendrerit dolor magna eget est lorem. Arcu ac tortor dignissim convallis aenean et tortor at risus. Cras adipiscing enim eu turpis. Eu non diam phasellus vestibulum lorem. Lorem mollis aliquam ut porttitor. Iaculis at erat pellentesque adipiscing commodo. Nec feugiat in fermentum posuere. Sed faucibus turpis in eu mi bibendum neque. Eget velit aliquet sagittis id consectetur. Nisl purus in mollis nunc sed id semper. Morbi tristique senectus et netus et. Nisi est sit amet facilisis magna etiam tempor orci eu. Bibendum ut tristique et egestas quis ipsum suspendisse ultrices gravida. Urna nec tincidunt praesent semper feugiat. Facilisi etiam dignissim diam quis enim lobortis scelerisque fermentum dui. Nisl condimentum id venenatis a. Vel fringilla est ullamcorper eget. Feugiat in fermentum posuere urna nec tincidunt praesent semper. Tristique nulla aliquet enim tortor at auctor urna nunc id. Aliquam etiam erat velit scelerisque in dictum non consectetur a. Ut diam quam nulla porttitor massa id neque aliquam vestibulum. Commodo elit at imperdiet dui accumsan sit. At volutpat diam ut venenatis tellus in metus vulputate. At in tellus integer feugiat scelerisque. Tristique nulla aliquet enim tortor. Ultrices mi tempus imperdiet nulla malesuada pellentesque elit eget gravida. Consequat semper viverra nam libero justo laoreet sit. Egestas tellus rutrum tellus pellentesque eu tincidunt tortor aliquam. Habitasse platea dictumst quisque sagittis purus. Maecenas accumsan lacus vel facilisis. Dictum non consectetur a erat. Aliquam nulla facilisi cras fermentum. Ut lectus arcu bibendum at. Lectus urna duis convallis convallis. Et molestie ac feugiat sed. Ultrices mi tempus imperdiet nulla. Eu augue ut lectus arcu bibendum at varius. Porttitor eget dolor morbi non arcu risus. Pharetra massa massa ultricies mi. Libero nunc consequat interdum varius sit. Elementum curabitur vitae nunc sed velit dignissim. Id nibh tortor id aliquet lectus proin nibh nisl. Tempus imperdiet nulla malesuada pellentesque. Sed libero enim sed faucibus turpis in. Tristique risus nec feugiat in fermentum posuere urna. Nulla facilisi morbi tempus iaculis urna id. Iaculis nunc sed augue lacus viverra vitae. Cras tincidunt lobortis feugiat vivamus at augue. Et pharetra pharetra massa massa ultricies mi quis hendrerit. Bibendum arcu vitae elementum curabitur vitae. Urna nunc id cursus metus aliquam eleifend. Senectus et netus et malesuada fames. Cursus euismod quis viverra nibh cras pulvinar mattis nunc. Risus sed vulputate odio ut enim blandit. Tortor at risus viverra adipiscing at in tellus integer feugiat. Lectus mauris ultrices eros in cursus turpis massa tincidunt. Quisque sagittis purus sit amet volutpat consequat mauris. Velit laoreet id donec ultrices tincidunt arcu non sodales. Id consectetur purus ut faucibus. Purus faucibus ornare suspendisse sed nisi lacus sed viverra. Porttitor leo a diam sollicitudin tempor id eu. Augue ut lectus arcu bibendum at varius vel. Mauris cursus mattis molestie a iaculis at erat pellentesque. A cras semper auctor neque. Massa placerat duis ultricies lacus. Pulvinar etiam non quam lacus suspendisse faucibus interdum posuere. At tempor commodo ullamcorper a lacus vestibulum. Faucibus vitae aliquet nec ullamcorper sit.";
var content_header = "ДЕНЬ УЧИТЕЛЯ";
var content_images = ["article_img_3.png", "article_img_2.png"];
var images = ["slider_image_0.png", "slider_image_1.png", "slider_image_2.png"];
var now = 2;
var header = ["Lorem", "Ipsum", "Dolor"];
var text = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit", "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua", "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat"];

function main() {
  let logo = document.getElementById("top_menu_logo");
  logo.style = "transform: rotate(360deg); transition: 0.5s; width: 3%;";
  let menu = document.getElementById("top_menu");
  menu.style = "width: 90%; transition: 0.5s";
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
  let h = document.querySelector(".content_title");
  h.innerHTML = content_header;
  let p = document.querySelector(".content_text");
  p.innerHTML = content_text;
  for (let i = 0; i < content_images.length; i++) {
    //<img id="content_img_0" class = "content_img" src="../static/img/article_img_3.png">
    let img = document.createElement('img');
    img.src = "../static/img/" + content_images[i];
    img.id = "content_img_" + str(i);
    img.style = "width: 40vw; height: auto;";
    let div = document.querySelector(".content_images");
    div.append(img);
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