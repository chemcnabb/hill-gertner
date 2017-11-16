



$(document).ready(function(){
    $('.hamburger').click(function(){
        $(this).toggleClass('is-active');
    });
    $( "#nav-drawer" ).hide();
    $( "#nav-toggle" ).click(function() {

        $( "#nav-drawer" ).slideToggle( 350, function() {
            // Animation complete.
        });
    });
});


// $(document).ready(function() {

    // init controller
// var controller = new ScrollMagic.Controller();
//
// // create a scene
// new ScrollMagic.Scene({
//         duration: 1500,    // the scene should last for a scroll distance of 100px
//         offset: 674        // start this scene after scrolling for 50px
//     })
//     .setPin("#company") // pins the element for the the scene's duration
//     .addTo(controller); // assign the scene to the controller
// });
//








$(document).ready(function(){
    // Cache selectors
    var lastId,
        topMenu = $("#nav-drawer"),
        topMenuHeight = topMenu.outerHeight()+15,
        // All list items
        menuItems = topMenu.find("a"),
        // Anchors corresponding to menu items
        scrollItems = menuItems.map(function(){
            var item = $($(this).attr("href"));
            if (item.length) { return item; }
        });

// Bind click handler to menu items
// so we can get a fancy scroll animation
    menuItems.click(function(e){
        var href = $(this).attr("href"),
            offsetTop = href === "#" ? 0 : $(href).offset().top;
        $('html, body').stop().animate({
            scrollTop: offsetTop
        }, 300);
        e.preventDefault();
    });

// Bind to scroll
    $(window).scroll(function(){
        // Get container scroll position
        var fromTop = $(this).scrollTop()+5;

        // Get id of current scroll item
        var cur = scrollItems.map(function(){
            if ($(this).offset().top < fromTop)
                return this;
        });
        // Get the id of the current element
        cur = cur[cur.length-1];
        var id = cur && cur.length ? cur[0].id : "";

        if (lastId !== id) {
            console.log(id);
            lastId = id;
            // Set/remove active class
            menuItems
                .parent().removeClass("active")
                .end().filter("[href='#"+id+"']").parent().addClass("active");
            window.location.hash = id;
        }
    });
});


