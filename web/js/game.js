$(document).ready(function () {
    alert("Ready to start ~~~~~~~");
    eel.vendor_board()
});

$(document).keydown(function (e) {
    var keyNum = e.keyCode
    var key = String.fromCharCode(keyNum)
    if (65 <= keyNum && keyNum <= 90) {
        eel.input(key)
    }
    else if (keyNum == 8) {
        eel.input("BackSpace")
    }
    else if (keyNum == 13) {
        eel.init_game()
        eel.input("Enter")
    }
    else {
        alert("Valid Key")
    }
});  

eel.expose(vendorBoard)
function vendorBoard(ymax, xmax){
    let gameBoard = document.getElementById("gameBoard");
    for(let j=0; j<ymax; j++){
        let rowDiv = document.createElement("div");
        rowDiv.setAttribute("class", "row d-flex gap-3");
        rowDiv.setAttribute("id", "boardRow" + j);
        
        for(let i=0; i<xmax; i++){
            let colDiv = document.createElement("div");
            colDiv.setAttribute("class", "textBox");
            colDiv.setAttribute("id", "no" + (j*ymax + i));
            rowDiv.appendChild(colDiv)

            let span = document.createElement("span");
            span.setAttribute("class", "fs3");
            span.setAttribute("id", "noWord" + (j*ymax + i));
            colDiv.appendChild(span)
        }
        gameBoard.appendChild(rowDiv);
    }
}