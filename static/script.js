async function generateCode(){

    const input =
    document.getElementById("userInput").value;

    const response = await fetch('/generate', {

        method:'POST',

        headers:{
            'Content-Type':'application/json'
        },

        body:JSON.stringify({
            input:input
        })
    });

    const data = await response.json();

    document.getElementById("pythonOutput").textContent =
    data.python;

    document.getElementById("javaOutput").textContent =
    data.java;

    document.getElementById("cOutput").textContent =
    data.c;
}

/* COPY FUNCTION */

function copyCode(id){

    const text =
    document.getElementById(id).textContent;

    navigator.clipboard.writeText(text);

    alert("Code Copied!");
}