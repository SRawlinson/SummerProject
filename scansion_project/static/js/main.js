
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
    }

    function separateSylls() {
        displayNormalText();
        var stress = document.getElementsByClassName("stress");
        for (var i = 0; i < stress.length; i++) {
            stress[i].innerHTML += " | "
        }
        var unstressed = document.getElementsByClassName("unstressed");
        for (var i = 0; i < unstressed.length; i++) {
            unstressed[i].innerHTML += " | "
        }
    }

    function boldSylls() {
        displayNormalText();
        var stressed = document.getElementsByClassName("stress");
        for (var i = 0; i < stressed.length; i++) {
            stressed[i].style.fontWeight = "bold";
        }
    }
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
