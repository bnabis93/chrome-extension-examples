const button = document.getElementById("capture-button");
let isCrosshair = false;

button.addEventListener("click", function () {
    if (isCrosshair) {
        button.style.cursor = "default";
        isCrosshair = false;
    } else {
        button.style.cursor = "crosshair";
        isCrosshair = true;
    }
});