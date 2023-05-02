const get_election_list_html = (name, prompt, privateKey, endDate, userID, yesVotes, noVotes) => {
    var html = "<h5> Election Name:</h5>";
    html += "<h5 class='small text-success'>" + name + "</h5><br>";
    html += "<h5> Election Prompt:</h5>";
    html += "<h5 class='small text-success'>" + prompt + "</h5><br>";
    html += "<h5> Election End Date:</h5>";
    html += "<h5 class='small text-success'>" + endDate + "</h5><br>";
    html += "<h5> Election Yes Votes:</h5>";
    html += "<h5 class='small text-success'>" + yesVotes + "</h5><br>";
    html += "<h5> Number of No Votes:</h5>";
    html += "<h5 class='small text-success'>" + noVotes + "</h5><br>";
    html += "<a href='/elections/view_details'>";
    html += "<button type='button'class='btn btn-sn btn-outline-success btn-sm lift'>Link</button></a>";
    return html;
}

const noElection = () => {
    var html = "<h5>There is no elections to display.</h5>";
    return html;
}

fetch('/get_my_elections', {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json; charset=utf-8'
    },
})
    .then(response => response.json())
    .then(data => {
        my_election_list = document.getElementById("current_election_list");
        if (data.length == 0) {
            const list_group_item = document.createElement("div");
            list_group_item.classList.add("list-group-item");
            const html = noElection();
            list_group_item.innerHTML = html;
            my_election_list.appendChild(list_group_item);
        } else {
            for (var i = 0; i < data.length; i++) {
                console.log(data[i]);
                const list_group_item = document.createElement("div");
                list_group_item.classList.add("list-group-item");
                const html = get_election_list_html(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6]);
                list_group_item.innerHTML = html
                my_election_list.appendChild(list_group_item);
            }
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });