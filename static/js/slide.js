$(".second-slide").owlCarousel({
    loop: true,
    dots: false,
    items: 2,
    autoWidth: true,
    margin: 20,
    nav: false,
    autoplay: true,
    autoplayTimeout: 2000,
    autoplayHoverPause: true,
});

$(".product-slide").owlCarousel({
    loop: true,
    nav: true,
    items: 1,
    dots: false,
    navText: [
        "<img src='./static/img/arrowRight.png'>",
        "<img src='./static/img/arrow-right.png'>",
    ],
});