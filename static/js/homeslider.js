var slideNo = 0;
homeslide();

function homeslide()
{
  var i;
  var slideImg = document.getElementsByClassName("slide")
  for(i = 0; i < slideImg.length; i++)
  {
    slideImg[i].style.display = "none";
  }
  slideNo++;
  if (slideNo > slideImg.length)
  {
    slideNo = 1;
  }
  slideImg[slideNo-1].style.display = "block";
  setTimeout(homeslide,3000);
}
