
async function GetData() {
    const url = "http://127.0.0.1:5000";
    try {

        const response = await fetch(url);

        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }


        const json = await response.json();
        console.log(json);
        displayData(json);
    } catch (error) {
        console.error(error.message);
    }
}

function startUpdate(interval) {
    GetData();
    setInterval(GetData, interval);
}

function displayData(data) {
    const UltmessageContainer = document.getElementById('Ultmessage-container');
    const messageContainer = document.getElementById('message-container');
    messageContainer.innerHTML = `<p>${data.Message}</p>`;
    const usernameContainer = document.getElementById('username-container');
    usernameContainer.innerHTML = `<p>${data.Username}</p>`;
}

window.onload = () => startUpdate(1000);
GetData();


function openTab(evt, tab) {
    var i, tabcontent, tablinks;

    tabcontent = document.getElementsByClassName("tabcontent");

    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }


    document.getElementById(tab).style.display = "block";
    evt.currentTarget.className += " active";
}
