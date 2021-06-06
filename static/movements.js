function edit(){
    id=this.getAttribute('name')
    var xhr1 = new XMLHttpRequest();
    xhr1.open('POST','/movement_edit_id',true);
    xhr1.setRequestHeader('Content-type', 'application/json');
    xhr1.onload = function(){
        r=this.responseText
        if(r=='success'){
            window.location='/movement_edit_page'
        }
    }
    data = {'id':id}
    xhr1.send(JSON.stringify(data)) 

}

function del(){
    id=this.getAttribute('name')
    console.log('delete-clicked')
    var xhr2 = new XMLHttpRequest();
    xhr2.open('POST','/movement_delete',true);
    xhr2.setRequestHeader('Content-type', 'application/json');
    xhr2.onload = function(){
        r=this.responseText
        if(r=='success'){
            window.location='/movements'
        }
    }
    data = {'id':id}
    xhr2.send(JSON.stringify(data))

}




function init(){
var xhr = new XMLHttpRequest();
xhr.open('POST','/movement_id_list',true);
xhr.setRequestHeader('Content-type', 'application/json');
xhr.onload = function () {
    r=this.responseText
    console.log(r)
    r = parseInt(r) 
    var i 
    for(i=1;i<=r;i++){
        t='edit-'+i.toString()
        document.getElementById(t).onclick = edit;
        t1='delete-'+i.toString() 
        document.getElementById(t1).onclick = del;
    }

    }

data = {'data':'data'}
xhr.send(JSON.stringify(data))
}

init()


from=document.getElementsByClassName('movement-from')
for(var i=0;i<from.length;i++){
    if(from[i].innerHTML==''){
        from[i].innerHTML='Nil'
    }
}


from=document.getElementsByClassName('movement-to')
for(var i=0;i<from.length;i++){
    if(from[i].innerHTML==''){
        from[i].innerHTML='Nil'
    }
}