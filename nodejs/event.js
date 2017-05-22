//事件驱动程序
var events = require('events');

var eventEmitter = new events.EventEmitter();

//事件处理
var connectHandler = function connected(){
	console.log('连接成功');

	eventEmitter.emit('data_received');
}

//绑定事件connection处理方法
eventEmitter.on('connection', connectHandler);

//绑定事件data_received处理方法
eventEmitter.on('data_received', function(){
	console.log('数据接收成功');
});

//触发事件connection
eventEmitter.emit('connection');

console.log("程序执行结束");