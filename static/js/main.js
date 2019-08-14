function uploadImg(){
    const realFile = document.getElementById("real-file");
    realFile.click();
}
function uploadnir(){
    const realFilenir = document.getElementById("real-file_nir");
    realFilenir.click();
}
function checkForm(){
    var img=document.getElementById('real-file').value;
    var nir=document.getElementById('real-file_nir').value;
    var alg=document.getElementById('algorithm').value;
    var sp=document.getElementById('errormsg');
    flag = false;
    if (img==''){
        sp.style.display='block';
        sp.innerHTML='!please select image';
        return flag;    
    }
    if (alg=='0'){
        sp.style.display='block';
        sp.innerHTML='!please select any algorithm';
        return flag;
    }
    if (alg=="fndvi" && nir){
        sp.style.display='block';
        sp.innerHTML='!cant select nir for VARI';
        return flag;
    }
    if(alg=="rndvi" && nir==''){
        sp.style.display='block';
        sp.innerHTML='!please select nir image for NDVI';
        return flag;
    }
}