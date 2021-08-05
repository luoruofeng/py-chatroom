function format(e){
     if(e){
        return e.getHours()+":"+(e.getMinutes())+":"+e.getSeconds();
     }
}

function scrollBottom(){
    $('.message-body').eq(0).animate({ scrollTop: $('.message-body').eq(0).prop("scrollHeight")}, 1000);
}

var ws = new WebSocket("ws://127.0.0.1:5555/echo");

ws.onmessage = function (res) {
    console.log(res.data);

    var data = JSON.parse(res.data);
    if (data.msg_type == 'message') {
        nickname = data.nickname

        var messageheader = $("<div class=\"message-header\"></div>");
        var time = $("<code></code>");
        time.html(format(new Date()));
        var messagetext = $("<div class=\"message-text\"></div>");
        var messageitem = $("<div class=\"message-item\"></div>");
        var messagecontent = $("<div class=\"message-content\"></div>");

        messageheader.append(nickname);
        messageheader.append(time);
        messagetext.html("content");
        messageitem.append(messageheader);
        messagecontent.append(messagetext);
        messageitem.append(messagecontent);
        $(".message-body").eq(0).append(messageitem);

        scrollBottom();
    }

};

ws.onopen = function (event){
  // alert("WebSocket is open now.");
};

ws.onclose = function(event) {
    var code = event.code;
    var reason = event.reason;
    var wasClean = event.wasClean;
}

function send_msg() {
    var msg = document.getElementById("message").value;
    ws.send(msg);
     window.event.returnValue =false;//阻止表单跳转
}

function copy_content(id) {
    var copyText = $("#"+id);//获取对象
    copyText.select();//选择
    document.execCommand("Copy");//执行复制
    // alert("复制成功！");
}