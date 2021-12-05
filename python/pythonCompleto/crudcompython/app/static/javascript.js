(function (win, doc) {
  "use strict";

  if (doc.querySelector(".btnDel")) {
    let btndel = doc.querySelectorAll(".btnDel");
    for (let i = 0; i < btndel.length; i++) {
      btndel[i].addEventListener("click", function (event) {
        if (confirm("Deseja mesmo apagar esse dado")) {
          return true;
        } else {
          event.preventDefault();
        }
      });
    }
  }

  //ajax do form
  if (doc.querySelector("#form")) {
    let form = doc.querySelector("#form");
    function sendForm(event) {
      event.preventDefault();
      let data = new FormData(form);
      let ajax = new XMLHttpRequest();
      let token = doc.querySelectorAll("input")[0].value;
      ajax.open("POST", form.action);
      ajax.setRequestHeader("X-CSRF-TOKEN", token);
      ajax.onreadystatechange = function(){
          if(ajax.status === 200 && ajax.readyState === 4){
              let result = doc.querySelector("#result");
              result.innerHTML = "Operação realizada com sucesso";
              result.classList.add("alert");
              result.classList.add("alert-success");
          }
      }
      ajax.send(data);
      form.reset();
    }
    form.addEventListener("submit", sendForm, false);
  }
})(window, document);