
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

    function displayNormalText() {
        var stressContent = document.getElementsByClassName("stress");
        for (var i = 0; i < stressContent.length; i++) {
            var text = stressContent[i].innerHTML;
            stressContent[i].innerHTML = text.toLowerCase();
            stressContent[i].style.color = "black";
        }
        var unstressContent = document.getElementsByClassName("unstressed");
        for (var i = 0; i < unstressContent.length; i++) {
            var text = unstressContent[i].innerHTML;
            unstressContent[i].innerHTML = text.toLowerCase();
            unstressContent[i].style.color = "black";
        }

    }

    function displayColours() {
        var stressContent = document.getElementsByClassName("stress");
        for (var i = 0; i < stressContent.length; i++) {
            var text = stressContent[i].innerHTML;
            stressContent[i].innerHTML = text.toLowerCase();
            stressContent[i].style.color = "red";
        }
        var unstressContent = document.getElementsByClassName("unstressed");
        for (var i = 0; i < unstressContent.length; i++) {
            var text = unstressContent[i].innerHTML;
            unstressContent[i].innerHTML = text.toLowerCase();
            unstressContent[i].style.color = "blue";
        }
    }

    function displayCapitals() {
        var stressContent = document.getElementsByClassName("stress");
        for (var i = 0; i < stressContent.length; i++) {
            stressContent[i].style.color = "black";
            var text = stressContent[i].innerHTML;
            // alert(text.toUpperCase());
            stressContent[i].innerHTML = text.toUpperCase();
            
        }
        var unstressContent = document.getElementsByClassName("unstressed");
        for (var i = 0; i < unstressContent.length; i++) {
            unstressContent[i].style.color = "black";
        }
    }