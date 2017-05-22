//创建一个服务器，监听请求
var http = require('http');
var url = require('url');
//创建一个服务监听端口8888
// http.createServer(function(request, response){
// 	response.writeHead(200,{'content-Type':'text/plain'});
// 	response.end('hello world\n');

// }).listen(8888);
// console.log('Server running at http://127.0.0.1:8888/');

function start(route){
	function onRequest(request, response){
		var pathname = url.parse(request.url).pathname;
		console.log("request pathname:"+pathname + " reviced");

        route(pathname);

		response.writeHead(200, {"content-Type": "text/plain"});
		response.write("hello world");
		response.end();
	}
	http.createServer(onRequest).listen(8888);
	console.log("server has started..");
}
exports.start = start;