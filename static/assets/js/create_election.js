let increaseRow = (event) => {
    let textarea = event.target;
    textarea.style.height = 'auto';
    textarea.style.height = textarea.scrollHeight + 'px';
}

let electionTitle = document.getElementById("electionTitle");
electionTitle.addEventListener("input", increaseRow);

let electionPrompt = document.getElementById("electionPrompt");
electionPrompt.addEventListener("input", increaseRow);

let title = document.getElementById('title');
let text = document.getElementById('text');

let titleCharacterCount = document.getElementById('titleCharacterCount');
let promptCharacterCount = document.getElementById('promptCharacterCount');

let CharacterCount = () => {
    titleCharacterCount.innerHTML = electionTitle.value.length;
    promptCharacterCount.innerHTML = electionPrompt.value.length;
    if (titleCharacterCount > 256) {
        titleCharacterCount.style.color = 'red';
    }
}

setInterval(CharacterCount, 250);

let currentDate = new Date().toISOString().split('T')[0];
let datepicker = document.getElementById('datepicker');
datepicker.setAttribute('min', currentDate);

let createElection = () => {
    let election_title = document.getElementById("electionTitle").value;
    let election_prompt = document.getElementById("electionPrompt").value;
    let election_username = document.getElementById("electionUserName").value;
    let election_pk = document.getElementById("electionPK").value;
    let selectedDate = datepicker.value;

    if (election_title.length < 1) {
        alert("Please enter a title for your election.");
        return;
    } else if (election_title.length > 256) {
        alert("Please enter a title for your election that is less than 256 characters.");
        return;
    } else if (election_prompt.length < 1) {
        alert("Please enter a prompt for your election.");
        return;
    } else if (election_username.length < 1) {
        alert("Please enter a username for your election.");
        return;
    } else if (election_pk.length < 1) {
        alert("Please enter a private key for your election.");
        return;
    }

    var currentDate = new Date().toISOString().split('T')[0];
    // Compare the selected date with the current date
    if (selectedDate >= currentDate) {
        // The selected date is at least today
        console.log('Selected date is at least today');
    } else {
        // The selected date is before today
        alert('Error: Selected date is before today');
        return;
    }

    var data = {
        "title": election_title,
        "prompt": currentPassword,
        "username": election_username,
        "pk": election_pk,
        "endDate": selectedDate
    };

    fetch('/submit_create_election_request', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json; charset=utf-8'
        },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(result => {
            if (result.success) {
                // handle success case here
                alert('Your election has been created successfully.');
                window.location = '/my_elections/view';
            } else {
                // handle failure case here
                alert('Failed to create election.', result.reason);
                window.location = '/my_elections/create';
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}