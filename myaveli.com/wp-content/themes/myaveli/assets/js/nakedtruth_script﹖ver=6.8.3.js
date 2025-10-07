jQuery(function($) {
  // Object to store video URLs
  const videoUrls = {
    'angela': 'https://www.youtube.com/embed/lumJWAzQmS0?enablejsapi=1&rel=0',
    'valerie': 'https://www.youtube.com/embed/1z0C7HcBwlM?enablejsapi=1&rel=0',
    'diana': 'https://www.youtube.com/embed/-3oVBRAskcI?enablejsapi=1&rel=0',
    'erika': 'https://www.youtube.com/embed/JEEvEAbJsXM?enablejsapi=1&rel=0'
  };

  // Function to pause all videos
  function pauseAllVideos() {
    $('.watch-success-story').each(function() {
      $(this)[0].contentWindow.postMessage('{"event":"command","func":"pauseVideo","args":""}', '*');
    });
  }

  // Function to handle clicking on watch buttons
  function handleWatchButtonClicks() {
    pauseAllVideos();

    // Get the name from the button id
    const name = this.id.replace('btn-', '').replace('thumbnail-', '').toLowerCase();
    
    // Update the iframe src
    const newSrc = videoUrls[name];
    if (newSrc) {
      $('.video-iframe.watch-success-story').attr('src', newSrc);
    }

    $('.close-btn').show();
    $('#watch-all').stop(true, true).slideDown(700);
    $('html, body').animate({
      scrollTop: $('#success-stories').offset().top
    }, 400);
  }

  // Event listeners for buttons and thumbnails
  $('[id^="btn-"], [id^="thumbnail-"]').on('click', handleWatchButtonClicks);

  // Close button handler
  $('.close-btn').on('click', function() {
    pauseAllVideos();
    $('#watch-all').stop(true, true).slideUp(700);
    $(this).hide();
  });
	
// 	to make header video autoplay on mobile
	$(document).ready(function() {
		var $video = $('video');

		if ($video.length) {
			// Set playsinline attribute
			$video.attr('playsinline', '');

			// Enable muted autoplay
			$video.prop('muted', true);
			$video.prop('autoplay', true);

			// Remove controls attribute
			$video.removeAttr('controls');

			// Handle play attempt
			$video.on('canplay', function() {
			  $(this)[0].play();
			}).on('error', function(e) {
// 			  console.log("Autoplay was prevented:", e.target.error.message);
			});
		  }
	});


  // Run the script once the window finishes loading
  $(window).on('load', function() {
    // Ensure all YouTube iframes have enablejsapi=1 in their src
    $('.watch-success-story').each(function() {
      var src = $(this).attr('src');
      if (src && src.indexOf('enablejsapi=1') === -1) {
        $(this).attr('src', src + (src.indexOf('?') === -1 ? '?' : '&') + 'enablejsapi=1');
      }
    });
  });
});