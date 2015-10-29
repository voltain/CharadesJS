
if (window.innerHeight <= 600) {
    loadcss('css/iphone.css');
} else {
    loadcss('css/main.css');
}

function loadcss(file) {
    var el = document.createElement('link');
    el.setAttribute('rel', 'stylesheet');
    el.setAttribute('type', 'text/css');
    el.setAttribute('href', file);
    document.getElementsByTagName('head')[0].appendChild(el);
}
 
$(document).ready(function(){
 
        $(".slidingDiv").hide();
        $(".show_hide").show();
 
    $('.show_hide').click(function(){
    $(".slidingDiv").fadeIn('fast');
    });
    
    $('.hide').click(function(){
    $(".slidingDiv").fadeOut('fast');
    });
     

});
