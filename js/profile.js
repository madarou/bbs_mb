//一个profile就是列表中的一项，包含了学校头像，学校来源吧，工作title，发布时间，工作类型，等等信息的展示
var avatars = {"QINGHUA":"img/QINGHUA.jpg","PKU":"img/PKU.jpg","FDU":"img/FDU.jpg","SJ":"img/SJ.jpg","NJU":"img/NJU.jpg"};
var jobtypes = {"FULL":"全职","PART":"兼职","BOTH":"全兼"};
var sources ={"QINGHUA":"清华大学","PKU":"北京大学","FDU":"复旦大学","SJ":"上海交通大学","NJU":"南京大学"};
var bgcolors = {"FULL":"#EA2424","PART":"#27c181","BOTH":"#8c0707"};
;(function($,window,undifined){
	var Profile = function(options){
		this.settings=$.extend({},Profile.defaults,options);
		this.init();
	}
	
	Profile.prototype={
			//初始化
			init:function(){
				this.create();
			},
			//创建，主要创建html元素和css
			create:function(){
				//构造模板
				var template ='<div class="about-img">'+
									'<img src="'+window.avatars[this.settings.source]+'" />'+
								'</div>'+
								'<a  style="text-decoration:initial" href="'+this.settings.href+'?id='+this.settings.id+'"><div class="about-sDetails">'+
									'<h3>'+this.settings.title+'</h3>'+
									'<h4>来源:'+window.sources[this.settings.source]+'</h4>'+
									'<h4>时间:'+this.settings.time+'</h4>'+
								'</div></a>'+
								'<div class="about-openBtn active">'+
									'<a class="o-type" style="background:'+window.bgcolors[this.settings.jobtype]+'"><i class="fa fa-user-secret"></i>'+window.jobtypes[this.settings.jobtype]+'</a>'+
								'</div>';
				//加入父页面
				this.profile=$('<div>').addClass('o-team-person').html(template).appendTo(this.settings.parent);
			}
	}
	
	Profile.defaults={
			id:0,//id，作为参数传到下一页面
			title:'公安部第三研究所 2017届校园招聘火热启动',
			time:'2016-10-29 20:15:00',
			jobtype:'FULL',
			source:'NJU',
			href:'detail.html',//详情地址
			parent:'body'//父元素，以#xxx的id形式传入
	}
	var profile=function(options){
		return new Profile(options);
	}
	window.profile = $.profile = profile;
})(window.JQuery||window.Zepto,window);