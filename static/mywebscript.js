let RunSentimentAnalysis = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();  // Creates a new XMLHttpRequest object to handle HTTP requests asynchronously.
    // Defines a function that runs every time the request state changes. 
    // When the request is complete (readyState == 4) and successful (status == 200), it updates the HTML element with ID system_response to show the response from the server.
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            // readyState == 4 means the request finished and the full response is available.
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "sentimentAnalyzer?textToAnalyze"+"="+textToAnalyze, true);
    xhttp.send();
}
