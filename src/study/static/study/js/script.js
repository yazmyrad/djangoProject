
const lightmode = 'sunny-outline.svg';
const darkmode  = 'moon-outline.svg';


function changecolor(event) {
    event.preventDefault();
    document.body.classList.toggle("dark-mode");
    document.getElementById('short-text').style.color = 'white';
}




let prevScrollpos = window.scrollY;
window.onscroll = function() {
  let currentScrollPos = window.scrollY;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navbar").style.top = "2vh";
  } else {
    document.getElementById("navbar").style.top = "-50px";
  }
  prevScrollpos = currentScrollPos;
}