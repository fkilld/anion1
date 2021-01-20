$('#myCarousel').carousel({
   interval: 3000,
})

$(function() {
        $('.material-card > .mc-btn-action').click(function () {
            var card = $(this).parent('.material-card');
            var icon = $(this).children('i');
            icon.addClass('fa-spin-fast');

            if (card.hasClass('mc-active')) {
                card.removeClass('mc-active');

                window.setTimeout(function() {
                    icon
                        .removeClass('fa-arrow-left')
                        .removeClass('fa-spin-fast')
                        .addClass('fa-bars');

                }, 800);
            } else {
                card.addClass('mc-active');

                window.setTimeout(function() {
                    icon
                        .removeClass('fa-bars')
                        .removeClass('fa-spin-fast')
                        .addClass('fa-arrow-left');

                }, 800);
            }
        });
    });




// vars
'use strict'
var	testim = document.getElementById("testim"),
		testimDots = Array.prototype.slice.call(document.getElementById("testim-dots").children),
    testimContent = Array.prototype.slice.call(document.getElementById("testim-content").children),
    testimLeftArrow = document.getElementById("left-arrow"),
    testimRightArrow = document.getElementById("right-arrow"),
    testimSpeed = 4500,
    currentSlide = 0,
    currentActive = 0,
    testimTimer,
		touchStartPos,
		touchEndPos,
		touchPosDiff,
		ignoreTouch = 30;
;

window.onload = function() {

    // Testim Script
    function playSlide(slide) {
        for (var k = 0; k < testimDots.length; k++) {
            testimContent[k].classList.remove("active");
            testimContent[k].classList.remove("inactive");
            testimDots[k].classList.remove("active");
        }

        if (slide < 0) {
            slide = currentSlide = testimContent.length-1;
        }

        if (slide > testimContent.length - 1) {
            slide = currentSlide = 0;
        }

        if (currentActive != currentSlide) {
            testimContent[currentActive].classList.add("inactive");            
        }
        testimContent[slide].classList.add("active");
        testimDots[slide].classList.add("active");

        currentActive = currentSlide;
    
        clearTimeout(testimTimer);
        testimTimer = setTimeout(function() {
            playSlide(currentSlide += 1);
        }, testimSpeed)
    }

    testimLeftArrow.addEventListener("click", function() {
        playSlide(currentSlide -= 1);
    })

    testimRightArrow.addEventListener("click", function() {
        playSlide(currentSlide += 1);
    })    

    for (var l = 0; l < testimDots.length; l++) {
        testimDots[l].addEventListener("click", function() {
            playSlide(currentSlide = testimDots.indexOf(this));
        })
    }

    playSlide(currentSlide);

    // keyboard shortcuts
    document.addEventListener("keyup", function(e) {
        switch (e.keyCode) {
            case 37:
                testimLeftArrow.click();
                break;
                
            case 39:
                testimRightArrow.click();
                break;

            case 39:
                testimRightArrow.click();
                break;

            default:
                break;
        }
    })
		
		testim.addEventListener("touchstart", function(e) {
				touchStartPos = e.changedTouches[0].clientX;
		})
	
		testim.addEventListener("touchend", function(e) {
				touchEndPos = e.changedTouches[0].clientX;
			
				touchPosDiff = touchStartPos - touchEndPos;
			
				console.log(touchPosDiff);
				console.log(touchStartPos);	
				console.log(touchEndPos);	

			
				if (touchPosDiff > 0 + ignoreTouch) {
						testimLeftArrow.click();
				} else if (touchPosDiff < 0 - ignoreTouch) {
						testimRightArrow.click();
				} else {
					return;
				}
			
		})
}

//---------------------------------start---------------------------//
var citiesByState = {
    College: ["BSc","BCom","BE/BTech, IT","BE/BTech Computer, IT","BE/BTech Civil","BE/BTech Mechanical","BE/BTech Electronics","BE/BTech ENT"],
    School: ["11","12"],
    Experience: ["0","1","2","3","4","5","6"],
    Fresher: ["0"]
    }
    function makeSubmenu(value) {
    if(value.length==0) document.getElementById("citySelect").innerHTML = "<option></option>";
    else {
    var citiesOptions = "";
    for(cityId in citiesByState[value]) {
    citiesOptions+="<option>"+citiesByState[value][cityId]+"</option>";
    }
    document.getElementById("citySelect").innerHTML = citiesOptions;
    }
    }
    function displaySelected() { var country = document.getElementById("countrySelect").value;
    var city = document.getElementById("citySelect").value;
    alert(country+"\n"+city);
    }
    function resetSelection() {
    document.getElementById("countrySelect").selectedIndex = 0;
    document.getElementById("citySelect").selectedIndex = 0;
    }

//--------------------------------end-------------------------------//

//-----------------------city------------------------------//
// var citiesByState = {
//     Chhattisgrah: ["BSc","BCom","BE/BTech, IT","BE/BTech Computer, IT","BE/BTech Civil","BE/BTech Mechanical","BE/BTech Electronics","BE/BTech ENT"]
    
//     }
//     function makeSubmenu(value) {
//     if(value.length==0) document.getElementById("citySelect").innerHTML = "<option></option>";
//     else {
//     var citiesOptions = "";
//     for(cityId in citiesByState[value]) {
//     citiesOptions+="<option>"+citiesByState[value][cityId]+"</option>";
//     }
//     document.getElementById("citySelect").innerHTML = citiesOptions;
//     }
//     }
//     function displaySelected() { var country = document.getElementById("countrySelect").value;
//     var city = document.getElementById("citySelect").value;
//     alert(country+"\n"+city);
//     }
//     function resetSelection() {
//     document.getElementById("countrySelect").selectedIndex = 0;
//     document.getElementById("citySelect").selectedIndex = 0;
//     }
    //-----------------------end------------------------//



