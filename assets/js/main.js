function uploadImg(){
    const realFile = document.getElementById("real-file");
    realFile.click();
};
function checkform(){
    var img=document.getElementById('real-file').value;
    var alg=document.getElementById('algorithm').value;
    var sp=document.getElementById('errormsg');
    flag = false;
    if (img==''){
        sp.style.display='block';
        sp.innerHTML='please select image';
        return flag;    
    }
    if (alg=='0'){
        sp.style.display='block';
        sp.innerHTML='please select any algorithm';
        return flag;
    }
}