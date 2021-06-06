document.getElementById('add-button').addEventListener('click',()=>{
    pname = document.getElementById('name').value 
    auth = document.getElementById('auth')
    if(pname==''){
        auth.innerHTML = 'Product Name Cannot be empty!'
    }
    else{
        const productname = {'name': pname}
    var xhr = new XMLHttpRequest();
    xhr.open('POST','/product_add',true);
    xhr.setRequestHeader('Content-type', 'application/json');
    xhr.onload = function () {
      // do something to response
      r = this.responseText
      if(r=='Product Exists!'){
        auth.innerHTML=r 
        auth.style['color'] = "red";
      }
      else{
        auth.innerHTML=r;
        auth.style['color'] = "green";

      }
  };
  xhr.send(JSON.stringify(productname))
    }
});

document.getElementById('back-button').addEventListener('click', ()=>{
    document.location ='/products'
});


document.addEventListener('keypress',function(event){
    if(event.keyCode==13){
        pname = document.getElementById('name').value 
    auth = document.getElementById('auth')
    if(pname==''){
        auth.innerHTML = 'Product Name Cannot be empty!'
    }
    else{
        const productname = {'name': pname}
    var xhr = new XMLHttpRequest();
    xhr.open('POST','/product_add',true);
    xhr.setRequestHeader('Content-type', 'application/json');
    xhr.onload = function () {
      // do something to response
      r = this.responseText
      if(r=='Product Exists!'){
        auth.innerHTML=r 
        auth.style['color'] = "red";
      }
      else{
        auth.innerHTML=r;
        auth.style['color'] = "green";

      }
  };
  xhr.send(JSON.stringify(productname))
    }

    }});