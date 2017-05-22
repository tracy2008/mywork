function helloObj(){
	var name;

	this.setName=function(nameStr){
		name = nameStr;
	},
	this.sayHello=function(){
		console.log("hello," + name);
	}
}
module.exports = helloObj;