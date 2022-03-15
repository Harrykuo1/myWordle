$(document).ready(function () {
    alert("Ready to start ~~~~~~~");
    eel.init_game()
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