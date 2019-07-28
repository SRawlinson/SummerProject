
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

    // function separateSylls() {
    //     displayNormalText();
    //     var stress = document.getElementsByClassName("stress");
    //     for (var i = 0; i < stress.length; i++) {
    //         stress[i].innerHTML += " | "
    //     }
    //     var unstressed = document.getElementsByClassName("unstressed");
    //     for (var i = 0; i < unstressed.length; i++) {
    //         unstressed[i].innerHTML += " | "
    //     }
    // }

    // function displayCapitals() {
    //     var stressContent = document.getElementsByClassName("stress");
    //     for (var i = 0; i < stressContent.length; i++) {
    //         stressContent[i].style.color = "black";
    //         var text = stressContent[i].innerHTML;
    //         // alert(text.toUpperCase());
    //         stressContent[i].innerHTML = text.toUpperCase();
            
    //     }
    //     var unstressContent = document.getElementsByClassName("unstressed");
    //     for (var i = 0; i < unstressContent.length; i++) {
    //         unstressContent[i].style.color = "black";
    //     }
    function getDefinition(evt) {
        // getMeaning("banana", function (wordDef) {
        //     alert(wordDef);
        //     document.getElementById("definition-output").innerHTML = wordDef;
        // });
        alert(evt.currentTarget);
        var defURL = baseJSONURL + wordInput + definitionURL + APIKey;
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if(this.readyState == 4 && this.status == 200) {
                var data = JSON.parse(this.responseText);
                document.getElementById("definition-output").innerHTML = data[0].text;
            }
        };
        xhttp.open("GET", defURL, true);
        xhttp.send();
    }

    var APIKey = "kcje7882nvil0mgncl2kio5pudxvpsz3ym5ispkp42ig69yqw";
    var baseJSONURL = "https://api.wordnik.com/v4/word.json/";
    var relatedWords = "/relatedWords?useCanonical=false&limitPerRelationshipType=10&api_key=kcje7882nvil0mgncl2kio5pudxvpsz3ym5ispkp42ig69yqw";
    var randomWordURL = "https://api.wordnik.com/v4/words.json/randomWord?hasDictionaryDef=true&maxCorpusCount=-1&minDictionaryCount=1&maxDictionaryCount=-1&minLength=5&maxLength=-1&api_key=kcje7882nvil0mgncl2kio5pudxvpsz3ym5ispkp42ig69yqw";
    var hyphenationURL = "/hyphenation?useCanonical=false&limit=50&api_key=";
    var definitionURL = "/definitions?limit=200&includeRelated=false&useCanonical=false&includeTags=false&api_key=";
    var fullURL = "https://api.wordnik.com/v4/word.json/banana/definitions?limit=200&includeRelated=false&useCanonical=false&includeTags=false&api_key=kcje7882nvil0mgncl2kio5pudxvpsz3ym5ispkp42ig69yqw";


    function getMeaning(theWord, callback) {
        thisURL = baseJSONURL + theWord + definitionURL + APIKey;
        alert("Got here")
        var jxhr = $.ajax({
            url: fullURL,
            type: "GET",
            async: false, 
            dataType: "text",
            timeout:3000,
            error: function(status) {
                var statusmessage = JSON.stringify(status.responseText, undefined, 4);
                if (statusmessage.error === "timeout") {
                    alert("callAPI timed out!");
                } else if (statusmessage.match(/404/)) {
                    alert("Coudn't find word");
                } else {
                    alert(statusmessage);
                }
            },
            success: function (data, status) {
                alert("success");
                var array = JSON.parse (data);
                callback(array)
            }

        });

    }