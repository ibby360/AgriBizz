/* Code for changing active link on clicking */
var btns = $(".classynav ul li");

for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function () {
    var current = document.getElementsByClassName("active");

    current[0].className = current[0].className.replace(" active", "");

    this.className += " active";
  });
}


// Changing hover class on product cards
$(document).ready(function() {
	
	$('.card').delay(1800).queue(function(next) {
		$(this).removeClass('hover');
		$('a.hover').removeClass('hover');
		next();
	});
});