document.addEventListener('keypress',function(event){
    if(event.keyCode==13){
        // console.log('clicked');
    username = document.getElementById('username').value 
    password = document.getElementById('password').value 
    const user = {username: username, password:password} 
    var xhr = new XMLHttpRequest();
    xhr.open('POST','/auth',true);
    xhr.setRequestHeader('Content-type', 'application/json');
    xhr.onload = function () {
      r = this.responseText
      if(r=='success'){
        console.log('redirect call')
        window.location = "/loginredirect"
      }
      else{
        document.getElementById('auth').innerHTML=r;
      }
  };
  xhr.send(JSON.stringify(user))
}
});

document.getElementById('login-button').addEventListener('click', ()=>{
  username = document.getElementById('username').value 
    password = document.getElementById('password').value 
    const user = {username: username, password:password} 
    var xhr = new XMLHttpRequest();
    xhr.open('POST','/auth',true);
    xhr.setRequestHeader('Content-type', 'application/json');
    xhr.onload = function () {
      // do something to response
      r = this.responseText
      if(r=='success'){
        console.log('redirect call')
        window.location = "/loginredirect"
      }
      else{
        document.getElementById('auth').innerHTML=r;
      }
  };
  xhr.send(JSON.stringify(user))
});


