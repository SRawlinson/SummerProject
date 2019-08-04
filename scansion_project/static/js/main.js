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
    if (tabName != "Swap Words") {
        document.getElementById("word-to-be-edited").innerHTML = "";
        document.getElementById("radio-button-space").innerHTML = "";
        var words = document.getElementsByClassName("word");
        for (var i = 0; i < words.length; i++){
            words[i].style.backgroundColor = "transparent";
        }
    }
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

function highlight(inputString, highlightColour, evt) {
    var box = evt.currentTarget;
    if (box.checked == true) {
        var wordType = document.getElementsByClassName(inputString);
        for (var i = 0; i < wordType.length; i++) {
            wordType[i].style.backgroundColor = highlightColour;
        }
    } else {
        var wordType = document.getElementsByClassName(inputString);
        for (var i = 0; i < wordType.length; i++) {
            wordType[i].style.backgroundColor = "transparent";
        }
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
    var fullword = evt.currentTarget;
    var fullID = fullword.id;
    fullID = fullID.split(' ');
    // var id = fullID[0];
    var word = fullID[1];
    // alert(fullID + " " + id + " " + word);
    if (document.getElementById("Scanner").style.display == "block") {
        getDefinition(word);
        // alert(word.name);
    } else if (document.getElementById("Swap Words").style.display == "block") {
        document.getElementById("word-to-be-edited").innerHTML = "";
        document.getElementById("radio-button-space").innerHTML = "";
        var words = document.getElementsByClassName("word");
        for (var i = 0; i < words.length; i++){
            words[i].style.backgroundColor = "transparent";
        }
        evt.currentTarget.style.backgroundColor = "yellow";
        editWord(fullword, words, word);
        
    }
}


function editWord(word, words, wordString) {
    // var wordInput = evt.currentTarget.id;
    var space = document.getElementById("radio-button-space");

    var dropdownTent = word.getElementsByClassName("dropdown-content");
    var stringRep = "";
    for (var i = 0; i < dropdownTent.length; i++){
        stringRep += dropdownTent[i].innerHTML;
    }
    re = /<br>/g;
    newString = stringRep.replace(re, '\n');
    var allWordsText = document.createElement("P");
    var allWords = document.createTextNode("Highlight all occurences of \'" + wordString + "\':");
    allWordsText.appendChild(allWords);
    space.appendChild(allWordsText);
    makeCheckButton(wordString, word);
    var editorText = document.createElement("P");
    var t = document.createTextNode("Select or type a word to replace selected word:")
    // var innerText =  "Select or type a word to replace \"" + "\":";
    editorText.appendChild(t);

    space.appendChild(editorText);


    if (newString.match("Synonyms:")) {
        var n = newString.lastIndexOf(":");
        synsString = newString.substring(n+2);
        newString = newString.substring(0, n-9);    
        synsArray = synsString.split(" ");
        
        for (var i = 0; i < 3; i++) {
            makeRadioButton("radio", synsArray[i]);
        }

    } 
    document.getElementById("word-to-be-edited").innerHTML = newString;

    makeRadioButton("radio", "Choose your own:");
    textInput = document.createElement("input");
    textInput.setAttribute("type", "text");
    textInput.setAttribute("id", "customInput");
    label = document.createElement("small");
    label.setAttribute("value", "Enter another word to replace the selected one");
    label.appendChild(textInput);
    space.appendChild(label);
    linebreak = document.createElement("br");
    space.appendChild(linebreak);
}

function makeRadioButton(type, text) {
    // alert("Got here");
    var label = document.createElement("label");

    var element = document.createElement("input");
    text = text.replace('_', ' ');
    //Assign different attributes to the element.
    element.setAttribute("type", type);
    element.setAttribute("value", type);
    element.setAttribute("class", "editRadioButtons")
    element.setAttribute("name", text);

    label.appendChild(element);
    label.innerHTML += " " + text;

    var space = document.getElementById("radio-button-space");
    //Append the element in page (in span).
    space.appendChild(label);
    linebreak = document.createElement("br");
    space.appendChild(linebreak);
}

function makeCheckButton(word, fullWord) {
    var checkButtonLabel = "Highlight all examples of \"" + word + "\"";

    var label = document.createElement("label");
    var element = document.createElement("input");
    element.setAttribute("type", "checkbox");
    element.setAttribute("value", "checkbox");
    element.setAttribute("id", "highlighterCheckbox");
    var highlightAllExamplesText = 'highlightAllExamples(\'' + fullWord.id + '\', \'' + word + '\');';
    element.setAttribute("onclick", highlightAllExamplesText);
    // var clicky = element.getAttribute("onclick");
    // alert(clicky);
    element.onclick = function() {
        highlightAllExamples(fullWord.id, word);
    }
    label.appendChild(element);
    label.innerHTML += " " + checkButtonLabel;
    var space = document.getElementById("radio-button-space");
    space.appendChild(label);
    linebreak = document.createElement("br");
    space.appendChild(linebreak);
    space.appendChild(linebreak);

}

function highlightAllExamples(wordID, word) {
    var checkbox = document.getElementById("highlighterCheckbox");
    var words = document.getElementsByClassName("word");
    if (checkbox.checked == true) {
        for (var i = 0; i < words.length; i++) {
            if (words[i].id.match(word)) {
                words[i].style.backgroundColor = "yellow";
            }
        }
    } else {
        for (var i = 0; i < words.length; i++) {
            if (words[i].id != wordID) {
                words[i].style.backgroundColor = "transparent";
            }
        }
    }
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

//Functions for editing text below
var listOfEdits = [];
function addEdits() {
    // alert(document.getElementById("customInput").value);
    // alert("method went");
    var arrayToGoInListOfEdits = [];
    var editSpace = document.getElementById("word-to-be-edited");
    var textArray = editSpace.innerHTML;
    textArray = textArray.split(':');
    var text = textArray[0];
    arrayToGoInListOfEdits.push(text);
    var wordsToChange = [];
    var words = document.getElementsByClassName("word");
    for (var i = 0; i < words.length; i++) {
        if (words[i].style.backgroundColor == "yellow") {
            wordsToChange.push(words[i]);
        }
    }
    var textForUser = "";
    if (wordsToChange.length > 1) {
        textForUser = "Replace all instances of \"" + text + "\" with ";
        arrayToGoInListOfEdits.push("all");
    } else {
        textForUser = "Replace \"" + text + "\" with ";
        arrayToGoInListOfEdits.push(wordsToChange[0].id);
    }
    // alert(textForUser);
    var radioButtons = document.getElementsByClassName("editRadioButtons");
    var activeButton;
    for (var j = 0; j < radioButtons.length; j++) {
        if (radioButtons[j].checked) {
            activeButton = radioButtons[j];
            break;
        }
    }
    // alert(activeButton.name);
    if (activeButton.name.match("Choose your own:")) {
        textForUser += "\"" + document.getElementById("customInput").value + "\""; 
        arrayToGoInListOfEdits.push(document.getElementById("customInput").value);
    } else {
        textForUser += "\"" + activeButton.name + "\"";
        arrayToGoInListOfEdits.push(activeButton.name);
    }
    // textForUser += "\"" + activeButton.name + "\"";
    // alert(textForUser);
    var replaceWords = document.createElement("P");
    var lineBreak = document.createElement("br");
    listOfEdits.push(arrayToGoInListOfEdits);
    textForUser = listOfEdits.length + ": " + textForUser;
    var textNode = document.createTextNode(textForUser);
    replaceWords.appendChild(textNode);
    var space = document.getElementById("edit-space");
    space.appendChild(lineBreak);
    space.appendChild(replaceWords);
    space.appendChild(lineBreak);
    document.getElementById("word-to-be-edited").innerHTML = "";
    document.getElementById("radio-button-space").innerHTML = "";
    alert(listOfEdits);
}
