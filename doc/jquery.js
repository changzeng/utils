// 绑定窗口加载完成后执行函数
$.ready(function(){});

// 绑定点击事件
$(".clas-name").click(function(){});

// post提交数据
$.post("/url_path",{key: val},function(data){
	$("span").html(data);
});
