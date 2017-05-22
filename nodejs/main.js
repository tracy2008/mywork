// var hello = require("./hello.js");
// var helloObj = require("./helloObj.js");
// hello.hello();
// var hel = new helloObj();
// hel.setName("张三");
// hel.sayHello();
// 

var server = require("./server.js");
var router = require("./router.js");
server.start(router.route);