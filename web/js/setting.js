var wordLengthSlider = document.getElementById("wordLengthSlider");
var wordLengthOutput = document.getElementById("showWordLength");
wordLengthOutput.innerHTML = wordLengthSlider.value; 
wordLengthSlider.oninput = function() {
    wordLengthOutput.innerHTML = this.value;
}

var guessLimitSlider = document.getElementById("guessLimitSlider");
var guessLimitOutput = document.getElementById("showGuessLimit");
guessLimitOutput.innerHTML = guessLimitSlider.value; 

guessLimitSlider.oninput = function() {
    guessLimitOutput.innerHTML = this.value;
}


function saveSetting(){
    console.log(wordLengthSlider.value, guessLimitSlider.value)
    eel.save_setting(wordLengthSlider.value, guessLimitSlider.value)
    alert("Save success!")
}