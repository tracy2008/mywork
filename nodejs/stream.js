var fs = require("fs");
var zlib = require("zlib");

console.log("================读取数据流================")
// var data = '';

// var readerStream = fs.createReadStream("input.txt");

// readerStream.setEncoding('UTF8');

// readerStream.on('data', function(chunk){
// 	data += chunk;
// });

// readerStream.on('end', function(){
// 	console.log("readerStream..");
// 	console.log(data);
// });	

// readerStream.on('error', function(err){
// 	console.log(err);
// });

// console.log("================写入数据流=================")
// // data = "写入数据流";

// var writerStream = fs.createWriteStream('output.txt');
// writerStream.write(data, 'UTF8');

// writerStream.end();

// writerStream.on('finish', function(){
// 	console.log("写入完成");
// });

// writerStream.on('error', function(err){
// 	console.log(err.stack);
// });
// writerStream.setEncoding('UTF8');
// readerStream.pipe(writerStream);
// readerStream.pipe(zlib.createGzip()).pipe(fs.createWriteStream('input.txt.gz'));

fs.createReadStream('input.txt.gz').pipe(zlib.createGunzip()).pipe(fs.createWriteStream('input.txt'))
console.log("程序执行结束");
