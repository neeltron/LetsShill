let form = document.querySelector('form');
const smallMessage = document.getElementById('smallMessage');
const errorMessage = 'Incorrect Password or Username!';
const passw ="password";
const usern = "abcdef";
const submitBtn = document.getElementById('submit');


function authenticate(){
	let username = document.getElementById('username').value;
	let password = document.getElementById('password').value;
	if (password == passw && username == usern){
        form.innerHTML = '<h1>You are logged In!</h1><p class="success-message">Redirecting you to your profile in 5 seconds...</p>';
        setTimeout(function (){
               window.location.href = "chat.html";
            }, 5000);
	}
	else {
		smallMessage.textContent = errorMessage;	
		smallMessage.style.color = "red";
	}
}
	



