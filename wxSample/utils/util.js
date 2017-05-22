exports.formatTime = function(obj) {
  return obj.getFullYear() + "-" + (obj.getMonth() + 1) + "-" + obj.getDate() + " " + obj.getHours() + ":" + obj.getMinutes() + ":" + obj.getSeconds();
}