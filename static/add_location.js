document.getElementById('add-button').addEventListener('click',()=>{
    lname = document.getElementById('name').value 
    auth = document.getElementById('auth')
    if(lname==''){
        auth.innerHTML = 'Location Name Cannot be empty!'
    }
    else{
        const locationname = {'name': lname}
    var xhr = new XMLHttpRequest();
    xhr.open('POST','/location_add',true);
    xhr.setRequestHeader('Content-type', 'application/json');
    xhr.onload = function () {
      // do something to response
      r = this.responseText
      if(r=='Location Exists!'){
        auth.innerHTML=r 
        auth.style['color'] = "red";
      }
      else{
        auth.innerHTML=r;
        auth.style['color'] = "green";

      }
  };
  xhr.send(JSON.stringify(locationname))
    }
});

document.getElementById('back-button').addEventListener('click', ()=>{
    document.location ='/locations'
});


document.addEventListener('keypress',function(event){
    if(event.keyCode==13){
        lname = document.getElementById('name').value 
        auth = document.getElementById('auth')
        if(lname==''){
            auth.innerHTML = 'Location Name Cannot be empty!'
        }
        else{
            const locationname = {'name': lname}
        var xhr = new XMLHttpRequest();
        xhr.open('POST','/location_add',true);
        xhr.setRequestHeader('Content-type', 'application/json');
        xhr.onload = function () {
          // do something to response
          r = this.responseText
          if(r=='Location Exists!'){
            auth.innerHTML=r 
            auth.style['color'] = "red";
          }
          else{
            auth.innerHTML=r;
            auth.style['color'] = "green";
    
          }
      };
      xhr.send(JSON.stringify(locationname))
        }

    }});