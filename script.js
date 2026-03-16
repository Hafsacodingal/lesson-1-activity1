function validate(e) {

    e.preventDefault();

    const email = document.getElementById("email").value;

    const password = document.getElementById("Password").value;

    const Age = document.getElementById("Age").value;

    const msgbox = document.getElementById("message");

    let message = '';

    if (email === '') {

        message = 'Please enter an email.';

        msgbox.style.color = 'red';

    }

    else if (password === '') {

        message = 'Please enter password.';

        msgbox.style.color = 'red';

    }

    else if (Age === '') {

        message = 'Please enter your Age.';

        msgbox.style.color = 'red';

    }

    else {

        message = 'Login successfully';

        msgbox.style.color = 'green';

    }

    msgbox.innerHTML = message;

}

document.getElementById("login").onsubmit = validate;