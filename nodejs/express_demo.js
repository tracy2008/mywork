var express = require("express");
var app = express();

//get请求
//
app.get('/', function(req, res){
	res.send('this is express demo');
})

var server = app.listen(8081, function(){
	var host = server.address().address;
	var port = server.address().port;
	console.log("访问地址及端口：%s:%s", host, port);
});

