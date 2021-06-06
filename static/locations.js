function edit(){
    id=this.getAttribute('name')
    var xhr1 = new XMLHttpRequest();
    xhr1.open('POST','/location_edit_id',true);
    xhr1.setRequestHeader('Content-type', 'application/json');
    xhr1.onload = function(){
        r=this.responseText
        if(r=='success'){
            window.location='/location_edit_page'
        }
    }
    data = {'id':id}
    xhr1.send(JSON.stringify(data)) 

}

function del(){
    id=this.getAttribute('name')
    console.log('delete-clicked')
    var xhr2 = new XMLHttpRequest();
    xhr2.open('POST','/location_delete',true);
    xhr2.setRequestHeader('Content-type', 'application/json');
    xhr2.onload = function(){
        r=this.responseText
        if(r=='success'){
            window.location='/locations'
        }
    }
    data = {'id':id}
    xhr2.send(JSON.stringify(data))

}

function view(){
    id=this.getAttribute('name')
    var xhr2 = new XMLHttpRequest();
    xhr2.open('POST','/location_view_id',true);
    xhr2.setRequestHeader('Content-type', 'application/json');
    xhr2.onload = function(){
        r=this.responseText
        if(r=='success'){
            window.location='/location_view_page'
        }
    }
    data = {'name':id}
    xhr2.send(JSON.stringify(data))



}




function init(){
var xhr = new XMLHttpRequest();
xhr.open('POST','/location_id_list',true);
xhr.setRequestHeader('Content-type', 'application/json');
xhr.onload = function () {
    r=this.responseText
    r = parseInt(r) 
    var i 
    for(i=1;i<=r;i++){
        t='edit-'+i.toString()
        document.getElementById(t).onclick = edit;
        t1='delete-'+i.toString() 
        document.getElementById(t1).onclick = del;
        t2='view-'+i.toString()
        document.getElementById(t2).onclick = view;
    }

    }

data = {'data':'data'}
xhr.send(JSON.stringify(data))
}

init()


