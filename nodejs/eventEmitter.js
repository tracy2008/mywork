//eventEmitter对象的使用
//
var events = require("events");

var eventEmitter = new events.EventEmitter();

//监听器1

var listen1 = function listen1(){
	console.log("执行listen1");
} 

var listen2 = function listen2(){
	console.log("执行listen2");
}

eventEmitter.on('connection', listen1);

eventEmitter.on('connection', listen2);

var listenerCount = events.EventEmitter.listenerCount(eventEmitter, 'connection');
console.log("监听connection的监听器数量：" + listenerCount);

eventEmitter.emit('connection');

eventEmitter.removeListener('connection', listen1);
console.log("listen1不再监听");

eventEmitter.emit('connection');
listenerCount = events.EventEmitter.listenerCount(eventEmitter, 'connection');
console.log("监听connection的监听器数量：" + listenerCount);

console.log("程序执行结束");
