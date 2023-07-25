const inputs = document.querySelectorAll(".input");

function focusFunc() {
  let parent = this.parentNode;
  parent.classList.add("focus");
}

function blurFunc() {
  let parent = this.parentNode;
  if (this.value == "") {
    parent.classList.remove("focus");
  }
}

inputs.forEach((input) => {
  input.addEventListener("focus", focusFunc);
  input.addEventListener("blur", blurFunc);
});

function sendEmail() {
  
  Email.send({
    SecureToken : "2739f558-cd4a-4346-b7f5-552b28386611 ",
    
    To : "techdrill6@gmail.com",
    From : document.getElementById("email").value,
    Subject : "For contact enquiry",
    Body : "Name : " + document.getElementById("name").value
            + " <br> Email : " + document.getElementById("email").value
            +  " <br> Phone no : " + document.getElementById("phone no").value
            + " <br> Message : " + document.getElementById("Message").value
  }).then(  
    message => alert("Message sent succesfully")
  );
}
