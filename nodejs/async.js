//阻塞与非阻塞
var fs = require("fs");
var data = fs.readFileSync('input.txt');	//阻塞读取文件
console.log(data.toString());
console.log("程序执行结束");

console.log("=============================");
fs.readFile('input.txt', function(err, dt){//回调实现异步读取文件
	if(err) return console.log(err);
	console.log(dt.toString());
});
console.log("程序执行结束");