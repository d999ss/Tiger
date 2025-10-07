jQuery.noConflict();
jQuery(document).ready(function($){
	var pathname = window.location.pathname;
  var queryParams = window.location.search;
  if (pathname == '/career/' && queryParams != '') {
    $('html, body').animate({
      scrollTop: $('section#career-job-list-section').offset().top
    }, 500)
  }
});
