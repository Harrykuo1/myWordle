$(document).ready(function () {
    alert("Ready to start ~~~~~~~");
    eel.init_game()
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
        eel.input("Enter")
    }
    else {
        alert("Valid Key")
    }
});

eel.expose(vendorBoard)
function vendorBoard(ymax, xmax) {
    let gameBoard = document.getElementById("gameBoard");
    for (let j = 0; j < ymax; j++) {
        let rowDiv = document.createElement("div");
        rowDiv.setAttribute("class", "row d-flex gap-3");
        rowDiv.setAttribute("id", "boardRow" + j);

        for (let i = 0; i < xmax; i++) {
            let colDiv = document.createElement("div");
            colDiv.setAttribute("class", "textBox");
            colDiv.setAttribute("id", "no" + (j * xmax + i));
            rowDiv.appendChild(colDiv)

            let span = document.createElement("span");
            span.setAttribute("class", "fs3");
            span.setAttribute("id", "noWord" + (j * xmax + i));
            colDiv.appendChild(span)
        }
        gameBoard.appendChild(rowDiv);
    }
}
eel.expose(modifyBoard)
function modifyBoard(y, x, ymax, xmax, key) {
    let pos = y * xmax + x
    let item = document.getElementById("noWord" + pos)
    item.innerText = key
}

eel.expose(drawColor)
function drawColor(y, xmax, colorList) {
    let posBasic = y * xmax
    for (let i = 0; i < xmax; i++) {
        let block = document.getElementById("no" + (posBasic + i));
        if (colorList[i] == 0) {
            block.classList.add("myGrayBackground")
        }
        else if (colorList[i] == 1) {
            block.classList.add("myYellowBackground")
        }
        else {
            block.classList.add("myGreenBackground")
        }
    }
}

eel.expose(webAlert)
function webAlert(str) {
    alert(str)
}

/*
function start() {
    //   按下 start 後 id 為 timer 的 DIV 內容可以開始倒數到到 0。 
    var timer = document.querySelector("#timer");
    var number = 10;
    setInterval(function () {
        number--;
        if (number <= 0)
            number = 0;
        timer.innerText = number + 0
    }, 1000);
}*/