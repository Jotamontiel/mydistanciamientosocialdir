var oFormCapsuleObject = document.forms['capsule_create_form'];
var oformCapsuleElementLat = oFormCapsuleObject.elements["lat"];
var oformCapsuleElementLng = oFormCapsuleObject.elements["lng"];

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else { 
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  oformCapsuleElementLat.value = position.coords.latitude;
  oformCapsuleElementLng.value = position.coords.longitude;
}