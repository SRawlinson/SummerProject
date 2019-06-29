var APIKey = "kcje7882nvil0mgncl2kio5pudxvpsz3ym5ispkp42ig69yqw";
var baseJSONURL = "https://api.wordnik.com/v4/word.json/";
var relatedWords = "/relatedWords?useCanonical=false&limitPerRelationshipType=10&api_key=kcje7882nvil0mgncl2kio5pudxvpsz3ym5ispkp42ig69yqw";
var randomWordURL = "https://api.wordnik.com/v4/words.json/randomWord?hasDictionaryDef=true&maxCorpusCount=-1&minDictionaryCount=1&maxDictionaryCount=-1&minLength=5&maxLength=-1&api_key=kcje7882nvil0mgncl2kio5pudxvpsz3ym5ispkp42ig69yqw";
var hyphenationURL = "/hyphenation?useCanonical=false&limit=50&api_key=";

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

function textEntered() {
    var enterredText = document.getElementById("text-input").value;
    document.getElementById("scan-output").value = enterredText;
    // alert();
}

function getSyllables() {
    syllables(document.getElementById("text-input").value, function (returned) {
        alert("callback went");
        //insert for loop here 
        var s = "";
        // alert(s);
        // document.getElementById("scan-ouput").innerHTML = (s);

        for (var i = 0; i < returned.length; i++) {
            s += "text: " + returned[i].text + " "
            if (returned[i].type) {
                s += " stress ";
            }
        }
        // console.log(s);
        document.getElementById("scan-output").innerHTML = (s);
    });
}

function syllables(theWord, callback) {
    alert("syllables went");
    var thisurl = baseJSONURL + theWord + hyphenationURL + APIKey;
    var jxhr = $.ajax ({
        url: thisurl,
        dataType: "text" ,
        timeout: 30000
    })
    .success (function (data, status) {
        var array = JSON.parse(data);
        alert("success went");
        callback (array)
    })
    .error (function (status) {
        alert("Error went");

    });
}

function getRandom() {
    random("rainbow", function (words) {
    alert(words.word);
    document.getElementById("scan-output").innerHTML = words.word;
    });
}

function random(theWord, callback) {
    alert("random went");
    var jxhr = $.ajax ({
        url: randomWordURL,
        dataType: "text" ,
        timeout: 30000
    })
    .success (function (data, status) {
        var array = JSON.parse (data);
        alert(".success went");
        callback (array)
    })
    .error (function (status) {
        alert(".error went");
        console.log ("random: url ==" + url + ", error == " + JSON.stringify (status, undefined, 4));
    });


}

