$(document).ready(function (){

});

function showLogin(){
    $('#myModal').modal("show");
}

function login(){
    if($("#password-input").val() == "" || $("#password-password").val() == ""){
        return;
    }

    $("#login-form").submit();
    // window.location.href = window.location.protocol+"//"+window.location.host+"/index/"+$("#roomnum-input").val()+"/"+$("#password-input").val()

    $('#myModal').modal('hide');//隐藏modal
    $('.modal-backdrop').remove();//去掉遮罩层
}