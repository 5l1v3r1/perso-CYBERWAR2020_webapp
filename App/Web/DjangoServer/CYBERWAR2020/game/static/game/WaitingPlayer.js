

for(var i = 1; i < 6; i++){
  var CD = document.getElementById("CD".concat(i))

  //add event click on each to loop btw states
  CD.addEventListener('click', function(e){
    switch (e.target.alt) {
      case "NotBuildCD":
        e.target.alt = "BuildCD";
        e.target.src = srcBuildCD;
        break;
      case "BuildCD":
        e.target.alt = "DestroyedCD";
        e.target.src = srcDestroyedCD;
        break;
      case "DestroyedCD":
        e.target.alt = "NotBuildCD";
        e.target.src = srcNotBuildCD;
        break;
    }
  });

  var states = document.createElement("span");

}
