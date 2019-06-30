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

//Methods and data do with calling the API

var APIKey = "kcje7882nvil0mgncl2kio5pudxvpsz3ym5ispkp42ig69yqw";
var baseJSONURL = "https://api.wordnik.com/v4/word.json/";
var relatedWords = "/relatedWords?useCanonical=false&limitPerRelationshipType=10&api_key=kcje7882nvil0mgncl2kio5pudxvpsz3ym5ispkp42ig69yqw";
var randomWordURL = "https://api.wordnik.com/v4/words.json/randomWord?hasDictionaryDef=true&maxCorpusCount=-1&minDictionaryCount=1&maxDictionaryCount=-1&minLength=5&maxLength=-1&api_key=kcje7882nvil0mgncl2kio5pudxvpsz3ym5ispkp42ig69yqw";
var hyphenationURL = "/hyphenation?useCanonical=false&limit=50&api_key=";

function getSyllables() {
    var thisurl = baseJSONURL + document.getElementById("text-input").value + hyphenationURL + APIKey;

    callAPI(thisurl, function (returned) {
        var s = "";
        var vowelFound = false;

        for (var i = 0; i < returned.length; i++) {
            for (var j = 0; j < returned[i].text.length; j++) {
                s += "x";


            } 
        }



        s += "\n" 
        for (var i = 0; i < returned.length; i++) {
            s += returned[i].text;
            // if (i === returned.length-1) {

            // } else {
            //     s += " | ";
            // }
        }




        // for (var i = 0; i < returned.length; i++) {
        //     s += "text: " + returned[i].text + " "
        //     if (returned[i].type) {
        //         s += " stress ";
        //     }
        // }
        document.getElementById("scan-output").innerHTML = (s);
    });
}



function getRandom() {
    callAPI(randomWordURL, function (words) {
    // alert(words.word);
    document.getElementById("scan-output").innerHTML = words.word;
    });
}

function callAPI(theURL, callback) {
    // alert("callAPI went");
    var jxhr = $.ajax ({
        url: theURL,
        dataType: "text" ,
        timeout: 30000
    })
    .success (function (data, status) {
        var array = JSON.parse (data);
        // alert(".success went");
        callback (array)
    })
    .error (function (status) {
        // alert(".error went");
        console.log ("random: url ==" + url + ", error == " + JSON.stringify (status, undefined, 4));
    });


}

