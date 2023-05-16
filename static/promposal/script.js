var allElement = document.getElementById("all");
var plsElement = document.getElementById("pls");
var confettiContainer = document.querySelector(".confetti");
var hamsterContainer = document.getElementById('hamster-container');

function letsgo(){
  document.title = "🎉";

  // Trigger explosion animation
  allElement.classList.add("explosion");
  // TODO: disable buttons

  // show hamsters
  hamsterContainer.style.display = 'flex';

  // Trigger confetti effect
  var confettiCount = 666;
  var fragment = document.createDocumentFragment();
  for (var i = 0; i < confettiCount; i++) {
    var confettiPiece = document.createElement("div");
    confettiPiece.setAttribute("id", "p" + i);
    confettiPiece.classList.add("confetti-inner");
    confettiPiece.style.left = Math.random() * 100 + "%";
    confettiPiece.style.animationDelay = Math.random() * 4 + "s";
    confettiPiece.style.backgroundColor = randomHsl();
    fragment.appendChild(confettiPiece);

    // document.addEventListener("mousemove", function(event) {
    //   var x = event.clientX;
    //   var y = event.clientY;
    //   confettiPiece.style.transition = "transform 0.5s ease";
    //   confettiPiece.style.transform = "translate(" + x + "px, " + y + "px)";
    // });
  }
  confettiContainer.appendChild(fragment);

  // Reset explosion animation and remove confetti after animation ends
//   setTimeout(function() {
//     allElement.classList.remove("explosion");
//     // confettiContainer.innerHTML = "";
//   }, 2000);

//   document.addEventListener("mousemove", function(event) {
//     var x = event.clientX;
//     var y = event.clientY;
//     // for (var i = 0; i < confettiCount; i++) {
//     //   var confettiPiece = document.getElementById("p" + i);
//     //   confettiPiece.style.transition = "transform 0.5s ease";
//     //   confettiPiece.style.transform = "translate(" + x + "px, " + y + "px)";
//     // }
//     confettiContainer.style.transition = "transform 0.5s ease";
//     confettiContainer.style.transform = "translate(" + x + "px, " + y + "px)";
//   });

}

let click_counter = 0;
let font_size_increment_px = 10;
function pls() {
  document.title = "🧎🏾‍♂️";

  var existingText = plsElement.innerText;
  // Append "please"
  plsElement.innerText = existingText + " please ";

  // Increase font size with certain probability
  if (click_counter >= 16) {
    var randomNum = Math.random();
    if (randomNum < 0.5) {
      var currentFontSize = parseInt(window.getComputedStyle(plsElement).fontSize);
      plsElement.style.fontSize = (currentFontSize + font_size_increment_px) + "px";
    }
  }

  // Change colors in hsl space
  if (click_counter >= 32) {
    var randomColor = randomHsl();
    plsElement.style.color = randomHsl();
  }
  click_counter ++;
}
function randomHsl() {
  return 'hsla(' + (Math.random() * 360) + ', 100%, 70%, 1)';
}
