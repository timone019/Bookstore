document.addEventListener('DOMContentLoaded', function() {

    // Example: Add an event listener to the login button
    const loginButton = document.querySelector('.btn');
    loginButton.addEventListener('click', function() {
        alert('Login button clicked!');
    });

    // Example: Add a dynamic greeting based on the time of day
    const greeting = document.createElement('p');
    const hours = new Date().getHours();
    if (hours < 12) {
        greeting.textContent = 'Good Morning!';
    } else if (hours < 18) {
        greeting.textContent = 'Good Afternoon!';
    } else {
        greeting.textContent = 'Good Evening!';
    }
    document.querySelector('main').prepend(greeting);
});