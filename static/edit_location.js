document.getElementById('back-button').addEventListener('click', () => {
    document.location = '/locations'
  });
  
  
  document.getElementById('edit-button').addEventListener('click', () => {
    pname = document.getElementById('name').value
    id = document.getElementById('id').innerText
    auth = document.getElementById('auth')
    console.log(pname, id)
    if (pname == '') {
      auth.innerHTML = 'Location Name Cannot be empty!'
    }
    else {
      const data = { 'id': id, 'name': pname }
      var xhr = new XMLHttpRequest();
      xhr.open('POST', '/location_edit_function', true);
      xhr.setRequestHeader('Content-type', 'application/json');
      xhr.onload = function () {
        // do something to response
        r = this.responseText
        if (r == 'success') {
          auth.innerHTML = r
          auth.style['color'] = 'green'
        }
  
      }
      xhr.send(JSON.stringify(data))
    };
  
  
  
  })
  
  document.addEventListener('keypress', function (event) {
    if (event.keyCode == 13) {
        pname = document.getElementById('name').value
        id = document.getElementById('id').innerText
        auth = document.getElementById('auth')
        console.log(pname, id)
        if (pname == '') {
          auth.innerHTML = 'Location Name Cannot be empty!'
        }
        else {
          const data = { 'id': id, 'name': pname }
          var xhr = new XMLHttpRequest();
          xhr.open('POST', '/location_edit_function', true);
          xhr.setRequestHeader('Content-type', 'application/json');
          xhr.onload = function () {
            // do something to response
            r = this.responseText
            if (r == 'success') {
              auth.innerHTML = r
              auth.style['color'] = 'green'
            }
      
          }
          xhr.send(JSON.stringify(data))
        };
    }
  })