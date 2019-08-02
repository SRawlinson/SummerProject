function toggleNavBar() {
    var panel = document.getElementById("panel");
    if (panel.style.display === "block") {
        panel.style.display = "none";
    } else {
        panel.style.display = "block";
    }
}

function textEntered() {
    var enterredText = document.getElementById("text-input").value;
    document.getElementById("scan-output").value = enterredText;
}

function openTab(evt, tabName) {
    var i, tabcontent, tablinks;

    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    tablinks =document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

function openViewTab(evt, viewtabName) {
    var i, viewtabcontent, viewtablinks;

    viewtabcontent = document.getElementsByClassName("viewtabcontent");
    for (i = 0; i < viewtabcontent.length; i++) {
        viewtabcontent[i].style.display = "none";
    }

    viewtablinks =document.getElementsByClassName("viewtablinks");
    for (i = 0; i < viewtablinks.length; i++) {
        viewtablinks[i].className = viewtablinks[i].className.replace(" active", "");
    }

    document.getElementById(viewtabName).style.display = "block";
    evt.currentTarget.className += " active";
}

//Display text functions here
// var displayText = document.getElementById("lines-scans-output").innerHTML;

function displayNormalText() {
    var stressContent = document.getElementsByClassName("stress");
    for (var i = 0; i < stressContent.length; i++) {
        stressContent[i].style.color = "black";
        stressContent[i].style.fontWeight = "normal";
    }
    var unstressContent = document.getElementsByClassName("unstressed");
    for (var i = 0; i < unstressContent.length; i++) {
        unstressContent[i].style.color = "black";
        unstressContent[i].style.fontWeight = "normal";

    }
    var unknownWords = document.getElementsByClassName("unknown");
    for (var i = 0; i < unknownWords.length; i++) {
        unknownWords[i].style.color = "black";
        unknownWords[i].style.fontWeight = "normal";

    }

}

function displayColours() {
    displayNormalText();
    var stressContent = document.getElementsByClassName("stress");
    for (var i = 0; i < stressContent.length; i++) {
        stressContent[i].style.color = "red";

    }
    var unstressContent = document.getElementsByClassName("unstressed");
    for (var i = 0; i < unstressContent.length; i++) {
        unstressContent[i].style.color = "blue";

    }
    var unknownWords = document.getElementsByClassName("unknown");
    for (var i = 0; i < unknownWords.length; i++) {
        unknownWords[i].style.color = "purple";
    }
}

function boldSylls() {
    displayNormalText();
    var stressed = document.getElementsByClassName("stress");
    for (var i = 0; i < stressed.length; i++) {
        stressed[i].style.fontWeight = "bold";
    }
}
function toggleDetails() {
    var info = document.getElementById("detailsInfo");
    if (info.style.display === "none") {
        info.style.display = "block";
    } else {
        info.style.display = "none";
    }
}

function getDefinitionOrEdit(evt) {
    var word = evt.currentTarget;
    // highlightText(word.id);
    if (document.getElementById("Scanner").style.display == "block") {
        getDefinition(word.id);
    } else {
        editWord(word);
    }
}

// function highlightText(word) {
//     // alert("Started highlight");
//     var inputText = document.getElementById("lines-scan-output");
//     var innerHTML = inputText.value;
//     alert("Finished highlight");

    // var index = innerHTML.indexOf(word);
    // alert("Got halfway through highlight");
    // if (index >= 0) {
    //     innerHTML = innerHTML.substring(0, index) + "<span class ='highlight'>" + innerHTML.substring(index, index+text.length) + "</span>" + innerHTML.substring(index + text.length);
    //     inputText.innerHTML = innerHTML;
    // }
// }

function editWord(word) {
    // var wordInput = evt.currentTarget.id;
    var dropdownTent = word.getElementsByClassName("dropdown-content");

    var stringRep = "";
    for (var i = 0; i < dropdownTent.length; i++){
        stringRep += dropdownTent[i].innerHTML;
    }
    re = /<br>/g;
    newString = stringRep.replace(re, '\n');
    var n = newString.lastIndexOf(":");
    synsString = newString.substring(n+2);
    newString = newString.substring(0, n-9);
    document.getElementById("word-to-be-edited").innerHTML = newString;

    synsArray = synsString.split(" ");
    for (var i = 0; i < 3; i++) {
        makeRadioButton("radio", synsArray[i]);
    }
    makeRadioButton("radio", "Custom");
    textInput = document.createElement("input");
    textInput.setAttribute("type", "text");
    label = document.createElement("small");
    label.setAttribute("value", "Enter another word to replace the selected one");
    label.appendChild(textInput);
    var space = document.getElementById("radio-button-space");
    space.appendChild(label);
    linebreak = document.createElement("br");
    space.appendChild(linebreak);
}

function makeRadioButton(type, text) {
    // alert("Got here");
    var label = document.createElement("label");

    var element = document.createElement("input");
    //Assign different attributes to the element.
    element.setAttribute("type", type);
    element.setAttribute("value", type);
    element.setAttribute("name", type);

    label.appendChild(element);
    label.innerHTML += " " + text;

    var space = document.getElementById("radio-button-space");
    //Append the element in page (in span).
    space.appendChild(label);
    linebreak = document.createElement("br");
    space.appendChild(linebreak);
}
// API related functions + data below
var APIKey = "kcje7882nvil0mgncl2kio5pudxvpsz3ym5ispkp42ig69yqw";
var baseJSONURL = "https://api.wordnik.com/v4/word.json/";
var relatedWords = "/relatedWords?useCanonical=false&limitPerRelationshipType=10&api_key=kcje7882nvil0mgncl2kio5pudxvpsz3ym5ispkp42ig69yqw";
var randomWordURL = "https://api.wordnik.com/v4/words.json/randomWord?hasDictionaryDef=true&maxCorpusCount=-1&minDictionaryCount=1&maxDictionaryCount=-1&minLength=5&maxLength=-1&api_key=kcje7882nvil0mgncl2kio5pudxvpsz3ym5ispkp42ig69yqw";
var definitionURL = "/definitions?limit=200&includeRelated=false&useCanonical=false&includeTags=false&api_key=";

function getDefinition(word) {
    // var wordInput = evt.currentTarget.id;
    var defURL = baseJSONURL + word + definitionURL + APIKey;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200) {
            var data = JSON.parse(this.responseText);
            var definition = word + ": \n\n" + data[0].text;
            document.getElementById("definition-output").innerHTML = definition;
        }
    };
    xhttp.open("GET", defURL, true);
    xhttp.send();
}

