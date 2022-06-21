// ============= Mobile Dropdown Open functionaility ======================
function closenav() {
  document.getElementById("extendednav").style.visibility = "collapse";
  document.getElementById("closebtn").style.display = "none";
  document.getElementById("morebtn").style.display = "inline-block";
}
function opennav() {
  document.getElementById("extendednav").style.visibility = "initial";
  document.getElementById("morebtn").style.display = "none";
  document.getElementById("closebtn").style.display = "inline-block";
}
