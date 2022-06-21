var slideNo = 0;
carousel();

function carousel()
{
  var i;
  var slideImg = document.getElementsByClassName("slides")
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
  setTimeout(carousel,9000);
}
