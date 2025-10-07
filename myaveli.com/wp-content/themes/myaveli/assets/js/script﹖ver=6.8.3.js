jQuery(function($) {

    // Add custom script here. Please backup the file before editing/modifying. Thanks
    $("#slider").on("input change", (e)=>{
        const sliderPos = e.target.value;
        // Update the width of the foreground image
        $('.foreground-img').css('width', `${sliderPos}%`)
        // Update the position of the slider button
        $('.slider-button').css('left', `calc(${sliderPos}% - 45px)`)
      });


    // Run the script once the document is ready

    $(document).ready(function() {
    $('.navbar-toggler').on('click', function() {
        // Check if the navbar collapse is shown
        if ($('.navbar-collapse').hasClass('show')) {
          // Close the navbar collapse
          $('.navbar-collapse').removeClass('show');
          $('.navbar-toggler').addClass('collapsed');
          // Show the original icon and hide the alternate icon
          $('.navbar-toggler').removeClass('navbar-toggler-icon-alt');
        } else if (!$('.navbar-collapse').hasClass('collapsing')) {
          $('.navbar-collapse').addClass('show');
          $('.navbar-toggler').removeClass('collapsed');
        }
    });


        // Add click event listener to toggle between original and alternate icons
        $('.navbar-toggler').on('click', function() {
            // Toggle the class to switch between the original and alternate icons
            $(this).toggleClass('navbar-toggler-icon-alt');
        });

    

    });


    // Run the script once the window finishes loading
    $(window).load(function(){
        
    });

});
