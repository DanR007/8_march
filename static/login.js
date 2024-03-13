document.addEventListener('DOMContentLoaded', function() {
    // Ваши операции с элементами DOM здесь

    document.getElementById("enter").addEventListener("click", function() {
        var user = document.getElementById('login').value;
        var pass = document.getElementById('password').value;
        var log = 
        {
            username : user,
            password : pass
        }
        console.log(log)
        // Для POST запроса
        fetch('/login', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json'
            },
            body: JSON.stringify(log)
        })
            .then(response => response.text())
            .then(data => {
                console.log(data)

                if (JSON.stringify(data) === JSON.stringify("Welcome"))
                {
                    window.location.href = 'authorized';
                }
            })
            .catch(error => console.error('Request failed', error));
    });
});
