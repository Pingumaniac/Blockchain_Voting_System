let confirmDelete = () => {
    var currentID = document.getElementById("currentID").value;
    var currentPassword = document.getElementById("currentPassword").value;
    var confirmPassword = document.getElementById("confirmPassword").value;

    if (currentID.length < 1) {
        alert("Please enter your username.");
        return;
    } else if (currentPassword.length < 1) {
        alert("Please enter your password.");
        return;
    } else if (confirmPassword.length < 1) {
        alert("Please confirm your password.");
        return;
    }

    if (currentPassword != confirmPassword) {
        alert("Passwords do not match.");
    } else {
        var data = {
            currentID: currentID,
            currentPassword: currentPassword
        };

        fetch('/submit_delete_account_request', {
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
                    alert('Your account has been deleted successfully.');
                    window.location = '/signout';
                } else {
                    // handle failure case here
                    alert('Error: Please enter your username correctly.');
                    window.location = '/delete_account';
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
}