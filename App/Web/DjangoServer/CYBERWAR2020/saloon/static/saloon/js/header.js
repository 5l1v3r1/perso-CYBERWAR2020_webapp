
var headerBar = document.getElementById("myHeader")

headerBar.addEventListener('click', function(e){
  switch (e.target.class) {
    case "closed":
      e.target.class = "open";
      break;

    case "open":
      e.target.class = "closed";
      break;
  }
});
