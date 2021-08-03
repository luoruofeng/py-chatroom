var ws = new WebSocket("ws://127.0.0.1:5555/echo");
ws.onmessage = function (res) {
    console.log(res.data);
    // var ptag = document.createElement("p");
    // ptag.innerText = res.data;
    // document.getElementById("chat-content-div").appendChild(ptag);
};

ws.onopen = function (event){
  // alert("WebSocket is open now.");
};

ws.onclose = function(event) {
    var code = event.code;
    var reason = event.reason;
    var wasClean = event.wasClean;

    alert(event)
    alert(reason)
    alert(wasClean)
};

function send_msg() {
    var msg = document.getElementById("message").value;
    ws.send(msg);
     window.event.returnValue =false;//阻止表单跳转
}
