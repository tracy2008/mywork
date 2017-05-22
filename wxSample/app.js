//小程序入口，注册一个小程序，管理小程序生命周期，只能注册一个
App({
  //初始化完触发（全局触发一次），此时还未生成page
  onLaunch:function(){
    //调用api从本地缓存中获取数据
    var logs = wx.getStorageSync("logs") || [];
    logs.unshift(Date.now());
    wx.setStorageSync("logs", logs);
  },
  //监听显示（关闭小程序、或home键，小程序并不销毁）
  onShow:function(){

  },
  onHide:function(){

  },
  getUserInfo:function(cb){
    var that = this;
    if(this.globalData.userInfo){
      typeof cb == "function" && cb(this.globalData.userInfo)
    }else{
      wx.login({
        success:function(){
          wx.getUserInfo({
            success:function(res){
              that.globalData.userInfo = res.userInfo;
              typeof cb == "function" &&　cb(that.globalData.userInfo)
            }
          })
        }
      });
    }
  },
  //全局数据
  globalData:{
    userInfo: null
  }


})