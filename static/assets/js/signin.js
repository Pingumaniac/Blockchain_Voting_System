let signIn = () => {
    var userName = document.getElementById("userName").value;
    var password = document.getElementById("password").value;
    var data = {
        "userName": userName,
        "password": password
    };

    if (userName == "" || password == "") {
        alert("Please fill in all the fields.");
        return;
    }

    fetch('/signin_request', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json; charset=utf-8'
        },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(result => {
            console.log(result);
            if (result.success) {
                // handle success case here
                window.location = '/home';
            } else {
                // handle failure case here
                alert(result.message);
                window.location = '/signin';
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}