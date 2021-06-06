document.getElementById('add-button').addEventListener('click', () => {
    auth = document.getElementById('auth')
    from = document.getElementById('from').value
    to = document.getElementById('to').value
    if (from == '' && to == '') {
        auth.innerHTML = 'Both From and To cannot be empty'
        auth.style['color'] = "red";
    }
    else {
        product = document.getElementById('product').value
        quantity = document.getElementById('qty').value
        const data = { 'from': from, 'to': to, 'product': product, 'quantity': quantity }
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/movement_add', true);
        xhr.setRequestHeader('Content-type', 'application/json');
        xhr.onload = function () {
            // do something to response
            r = this.responseText
            auth.innerHTML = r;
            auth.style['color'] = "green";
        };
        xhr.send(JSON.stringify(data))
    }

});

document.getElementById('back-button').addEventListener('click', () => {
    document.location = '/movements'
});


document.addEventListener('keypress', function (event) {
    if (event.keyCode == 13) {
        auth = document.getElementById('auth')
        from = document.getElementById('from').value
        to = document.getElementById('to').value
        product = document.getElementById('product').value
        quantity = document.getElementById('qty').value
        if (from == '' && to == '') {
            auth.innerHTML = 'Both From and To cannot be empty'
            auth.style['color'] = "red";
        }
        else if (product=='' || quantity==''){
            auth.innerHTML = 'Product or Quantity cannot be empty'
            auth.style['color'] = "red";

        }
        else {
            
            const data = { 'from': from, 'to': to, 'product': product, 'quantity': quantity }
            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/movement_add', true);
            xhr.setRequestHeader('Content-type', 'application/json');
            xhr.onload = function () {
                // do something to response
                r = this.responseText
                auth.innerHTML = r;
                auth.style['color'] = "green";
            };
            xhr.send(JSON.stringify(data))
        }
    }
});