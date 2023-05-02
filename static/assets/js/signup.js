let signUp = () => {
    var userName = document.getElementById("userName").value;
    var password = document.getElementById("password").value;
    var confirmpassword = document.getElementById("confirmpassword").value;
    var fullName = document.getElementById("fullName").value;
    var email = document.getElementById("email").value;

    var data = {
        "userName": userName,
        "password": password,
        "confirmpassword": confirmpassword,
        "fullName": fullName,
        "email": email
    };

    if (userName == "" || password == "" || confirmpassword == "" || fullName == "" || email == "") {
        alert("Please fill in all the fields.");
        return;
    }

    if (password != confirmpassword) {
        alert("Passwords do not match.");
        return;
    }

    fetch('/signup_request', {
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
                window.location = '/signup';
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}