function menuOpen(x) {
  x.classList.toggle("change");
  // insertMenu()
  var dropdowns= document.getElementById("menuDropdown");
  if (!dropdowns.classList.contains('show')){
    dropdowns.classList.toggle('show');
  }
  else if (dropdowns.classList.contains('show')) {
    dropdowns.classList.remove('show');
  }
}

