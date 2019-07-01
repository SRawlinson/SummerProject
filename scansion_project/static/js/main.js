//Methods for page/display, tabs etc. 

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

function clearOutputArea() {
    document.getElementById("scan-output").innerHTML = "";
}
//Methods and data do with calling the API

var APIKey = "kcje7882nvil0mgncl2kio5pudxvpsz3ym5ispkp42ig69yqw";
var baseJSONURL = "https://api.wordnik.com/v4/word.json/";
var relatedWords = "/relatedWords?useCanonical=false&limitPerRelationshipType=10&api_key=kcje7882nvil0mgncl2kio5pudxvpsz3ym5ispkp42ig69yqw";
var randomWordURL = "https://api.wordnik.com/v4/words.json/randomWord?hasDictionaryDef=true&maxCorpusCount=-1&minDictionaryCount=1&maxDictionaryCount=-1&minLength=5&maxLength=-1&api_key=kcje7882nvil0mgncl2kio5pudxvpsz3ym5ispkp42ig69yqw";
var hyphenationURL = "/hyphenation?useCanonical=false&limit=50&api_key=";

var outputText = "";
 
//So this seems to work but its v delicate - doesn't like misspelled words or hyphens etc. Need some error handling. 
//Also it relies upon the ajax being synchronous, which i feel is amateurish or hacky or something. 
function scanText(){
    var textForScan = document.getElementById("text-input").value;
    textForScan.trim();
    // alert(textForScan);
    outputText = "";
    var linesArray = textForScan.split("\n");

    for (var i = 0; i < linesArray.length; i++) {
        var line = linesArray[i];
        var txt = line.match(/[a-z']+/ig);

        for (var j = 0; j < txt.length; j++) {
            getSyllables(txt[j]);
        }
        outputText += "\n" + line + "\n";
    }

    document.getElementById("scan-output").innerHTML = outputText;
    alert("finished");
}

//This works fine for individual words but at the moment stores output in a global variable. 
function getSyllables(wordForScan) {
    // alert("get syllables for: " + wordForScan);
    var thisurl = baseJSONURL + wordForScan + hyphenationURL + APIKey;

    callAPI(thisurl, function (returned) {
        // alert("callback")
        var s = "";
        var vowelFound = false;
        var vowels = /[aeiou]/i;
        //for each syllable in the word
        for (var i = 0; i < returned.length; i++) {
            //for each letter in the syllable
            for (var j = 0; j < returned[i].text.length; j++) {
                var letter = returned[i].text.charAt(j);
                //If it's the first vowel
                if (vowels.test(letter) && vowelFound == false) {
                    //and it's stressed
                    if (returned[i].type) {
                        s += "/";
                    } else {
                        s += "x";
                    }
                    vowelFound = true;
                } else {
                    s += "  ";
                }
            } 
            vowelFound = false;
        }
        outputText += s;

    });

}


//Not strictly needed atm but was a test run of the API
function getRandom() {
    callAPI(randomWordURL, function (words) {
    document.getElementById("scan-output").innerHTML = words.word;
    });
}

//Main api function - simply calls the url supplied as parameter and sends back a parsed object. 
function callAPI(theURL, callback) {
    var jxhr = $.ajax ({
        url: theURL,
        async: false,
        dataType: "text" ,
        timeout: 30000
    })
    .success (function (data, status) {
        var array = JSON.parse (data);
        callback (array)
    })
    .error (function (status) {
        console.log ("callAPI error: url ==" + url + ", error == " + JSON.stringify (status, undefined, 4));
        alert ("callAPI error: url ==" + url + ", error == " + JSON.stringify (status, undefined, 4));

    });


}

