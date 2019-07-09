
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