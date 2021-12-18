// for HAMBURGER MENU

const hamburgerMenu = document.querySelector(".hamburger-menu");
const ul = document.querySelector("nav ul");

hamburgerMenu.addEventListener("click", () => {
  hamburgerMenu.classList.toggle("hamburger-rotate");
  ul.classList.toggle("slide-out");
});



/// LOADING

window.addEventListener("load", function () {
  const loader = document.querySelector(".loader");
  loader.style.display = "none";
});

// SCROLL ICON

let scroollButtonVisibilite = () => {
  let windowpos = $(window).scrollTop();
  let scrollLink = $('.scroll-to-top');
  if (windowpos > 1000) {
      scrollLink.fadeIn(300);
  } else {
      scrollLink.fadeOut(300);
  }
}

scroollButtonVisibilite();

$(window).on('scroll', function () {
  scroollButtonVisibilite();
});


$(".scroll-to-top").on('click', function () {

  $('html, body').animate({
      scrollTop: $('body').offset().top
  }, 100);

});