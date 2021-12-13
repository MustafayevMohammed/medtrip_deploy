const headerText = document.querySelector(".header-content .text--area");
const headerAnimation = document.querySelector(".header-content .image-area");
const headerSocialMedia = document.querySelector(
  ".header-content .sosial-icons"
);
const headerBottomText = document.querySelector(".slide-text .position");
const owlCarousel = document.querySelector(".owl-carousel");
const sanatoryHeader = document.querySelector(".section_title");
const sanatoryCard = document.querySelector(
  ".sanatory_sectio .sanatory_section_cardlist"
);
const reabilitation = document.querySelector(".reabilitation");
const cosmetelogyHeader = document.querySelector(
  ".sanatory_section2 .section_title2"
);
const cosmetelogyCard = document.querySelector(".cosmetology");
const healthyHeader = document.querySelector(
  ".sanatory_section .section_title "
);
const healthHead = document.querySelector(".healthyHead");
const healthyCard = document.querySelector(".healthy-card ");
const tourHeader = document.querySelector(".tourHeader");
const tourCard = document.querySelector(".tourCard");
const productHeader = document.querySelector(".facilities .title");
const productList = document.querySelector(".product-grid");
const formHeader = document.querySelector(".back .text");
const formInput = document.querySelector(".back .col-7");
const formImage = document.querySelector(".back .col-5");
const footer = document.querySelector(".footer");

const handleIntersection = (entries) => {
  entries.map((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("visible");
    }
  });
};

const observer = new IntersectionObserver(handleIntersection);
observer.observe(headerText);
observer.observe(headerAnimation);
observer.observe(reabilitation);
observer.observe(headerSocialMedia);
observer.observe(headerBottomText);
observer.observe(owlCarousel);
observer.observe(healthHead);
observer.observe(sanatoryHeader);
observer.observe(sanatoryCard);
observer.observe(cosmetelogyHeader);
observer.observe(cosmetelogyCard);
observer.observe(healthyHeader);
observer.observe(healthyCard);
observer.observe(tourHeader);
observer.observe(tourCard);
observer.observe(productHeader);
observer.observe(productList);
observer.observe(formHeader);
observer.observe(formInput);
observer.observe(formImage);
observer.observe(footer);
observer.observe(signIn);
observer.observe(lang);
