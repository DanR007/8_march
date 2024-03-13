document.addEventListener('DOMContentLoaded', function() {
  // Ваши операции с элементами DOM здесь

  document.getElementById("Login").addEventListener("click", function() {
      // Для GET запроса
      fetch('/login')
      .then(response => response.text())
      .then(data => {
        console.log(data)
        window.location.href = 'login';
      })
      .catch(error => console.error('Request failed', error));
  });
});