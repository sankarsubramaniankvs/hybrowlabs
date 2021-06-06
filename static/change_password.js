document.getElementById('change-button').addEventListener('click', ()=>{
    current = document.getElementById('current').value 
    new_password = document.getElementById('new-password').value 
    confirm = document.getElementById('confirm-password').value
    message = document.getElementById('auth')
    if(current==''){
      message.innerHTML = 'Current password cannot be empty!';
      message.style['color'] = 'red';
    }
    else if(new_password==''){
      message.innerHTML = 'New password cannot be empty!';
      message.style['color'] = 'red';
    }
    else if(new_password != confirm){
      message.innerHTML='Passwords do not match!';
      message.style['color'] = 'red';
    }
    else if(current==new_password){
      message.innerHTML='New password cannot be the same as old one!'
      message.style['color'] = 'red';
    }
    else{

    const data ={current: current, new: new_password, confirm: confirm}
    var xhr = new XMLHttpRequest();
    xhr.open('POST','/change_pass',true);
    xhr.setRequestHeader('Content-type', 'application/json');
    xhr.onload = function () {
      // do something to response
      r = this.responseText
      if(r=='Current password incorrect!'){
        message.innerHTML=r;
        message.style['color'] = 'red';

      }
      else if(r=='Password change successful'){
        message.innerHTML=r;
        message.style['color'] = 'green';

      }

  };
  xhr.send(JSON.stringify(data))
}
});


document.addEventListener('keypress',function(event){
  if(event.keyCode==13){
    current = document.getElementById('current').value 
    new_password = document.getElementById('new-password').value 
    confirm = document.getElementById('confirm-password').value
    message = document.getElementById('auth')
    if(current==''){
      message.innerHTML = 'Current password cannot be empty!';
      message.style['color'] = 'red';
    }
    else if(new_password==''){
      message.innerHTML = 'New password cannot be empty!';
      message.style['color'] = 'red';
    }
    else if(new_password != confirm){
      message.innerHTML='Passwords do not match!';
      message.style['color'] = 'red';
    }
    else if(current==new_password){
      message.innerHTML='New password cannot be the same as old one!'
      message.style['color'] = 'red';
    }
    else{

    const data ={current: current, new: new_password, confirm: confirm}
    var xhr = new XMLHttpRequest();
    xhr.open('POST','/change_pass',true);
    xhr.setRequestHeader('Content-type', 'application/json');
    xhr.onload = function () {
      // do something to response
      r = this.responseText
      if(r=='Current password incorrect!'){
        message.innerHTML=r;
        message.style['color'] = 'red';

      }
      else if(r=='Password change successful'){
        message.innerHTML=r;
        message.style['color'] = 'green';

      }

  };
  xhr.send(JSON.stringify(data))
}


  }
});


document.getElementById('back-button').addEventListener('click', ()=>{
    document.location ='/loginredirect'
});