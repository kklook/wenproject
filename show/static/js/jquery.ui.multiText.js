/**
 * 
 */
(function($) {
	$.widget("ui.multiText", $.ui.textButton, {
		options : {
			triggerClassName : 'l-trigger',
			click : $.noop,
			disabled: false 
		},
		_create : function() {
			this._super();
	        var element = this.element,that = this;
	        this.disabled = element.attr('disabled') === undefined ? this.options.disabled  
            		: element.prop('disabled');
		},
		showView : function() {
			this._super();
		},
		showEdit : function() {
			this._super();
			if (!this.readonly && !this.disabled) {
				this.element.next().show();
			}else{ //否则就隐藏下拉框 
				this.element.next().hide();
				this.showView();
			}
			//this.element.bind({
				//mouseenter : function(){
					//$(this).next().show();
				//},
				//mouseleave : function(){
					//$(this).next().hide();
				//}
			//});
			
			//this.element.next().bind({
				//mouseenter : function(){
					//$(this).show();
				//},
				//mouseleave : function(){
					//$(this).hide();
				//}
			//});
		},
		_onSwitchButtonClick : function(e){
			var eventEle = this.getEventResource(e);
		 
			if($(eventEle).is('input')){
				hideDjcjSelectView();
				return;  // 如果是input框框点击，则直接返回， 不显示。
			}
			this.element.next().show();
			var pos = this.getEventPosition(e);
			var eleWidth = this.element.width();
			var eleHeight = this.element.height();
			//var eleWidth = this.element.next().width();
			//this.element.trigger("dblclick",[pos.x,pos.y]);
			showDjcjSelectView(this.element.attr("id"), pos.x - eleWidth,  pos.y + eleHeight);
		},
		getEventPosition : function(event){
		   event= event || window.event;
	       if(event.pageX || event.pageY){
	           return {x:event.pageX, y:event.pageY};
	       }
	       return {x:event.clientX + document.body.scrollLeft - document.body.clientLeft,
	           y:event.clientY + document.body.scrollTop - document.body.clientTop
	       };
		},
		getEventResource: function(event){
			event= event || window.event;
		    
			return event.target || $(event.srcElement);
			
		},
		destroy : function (){
			this._super();
		}
	});
})(jQuery);
