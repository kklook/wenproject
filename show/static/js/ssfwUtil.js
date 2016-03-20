/**
 * 合并表格
 * 参数：表格ID (必须)
 * 参数：需要合并第几列，如果为空合并全部列。
 * 示例：合并id是tableId表格第1、3列，uniteTable('tableId',1,3);
 */
function uniteTable(tb) {
	if(typeof tb !== 'string'){
		return;
	}
	tb = document.getElementById(tb);
	if(!tb){
		return ;
	}
//			if (!checkTable(tb))
//				return;
	var column = [];
	if(arguments.length > 1){
		for(var x = 1; x < arguments.length;x++ ){
			column[column.length] = arguments[x];
		}
	}
	var i = 0;
	var j = 0;

	var rowCount = tb.rows.length; 
	var colCount = tb.rows[0].cells.length; 
	var obj1 = null;
	var obj2 = null;
	for (i = 0; i < rowCount; i++) {
		for (j = 0; j < colCount; j++) {
			tb.rows[i].cells[j].id = tb.id + "tb__" + i.toString() + "_"
					+ j.toString();
		}
	}
	for (i = 0; i < colCount; i++) {
		if(column.length){
			var flag = false;
			for(var k = 0; k < column.length ; k++){
				if(column[k] === (i + 1)){
					flag =  true;
					break;
				}
			}
			if(!flag){
			    continue;	
			}
		}
        obj1 = document.getElementById( tb.id + "tb__0_" + i.toString());
		for (j = 1; j < rowCount; j++) {
			obj2 = document.getElementById( tb.id + "tb__" + j.toString() + "_"
					+ i.toString());
			if($.trim(obj1.innerText) == "" || $.trim(obj2.innerText) == ""){
				continue;
			}
				if (obj1.innerText == obj2.innerText) {
					obj1.rowSpan++;
					obj2.parentNode.removeChild(obj2);
				} else {
					obj1 = document.getElementById( tb.id + "tb__" + j.toString()
							+ "_" + i.toString());
				}
			
		}
	}
}


function checkTable(tb) {
	if (tb.rows.length == 0)
		return false;
	if (tb.rows[0].cells.length == 0)
		return false;
	for ( var i = 0; i < tb.rows.length; i++) {
		if (tb.rows[0].cells.length != tb.rows[i].cells.length)
			return false;
	}
	return true;
}
		
		
/**
 * == 分页代码 ==
 */

//设置每页显示条数
//var iDisplayLength = 10;
function getLastPage(){
	var totalSize = $("#totalSize").val();
	var iDisplayLength = $("#iDisplayLength").val();
	return Math.ceil(totalSize/iDisplayLength);
}
function isLastPage(){
	var pageNo = $("#curPageNo").val();
	return (parseInt(pageNo,"10") + 1) > getLastPage() ? true : false;
}

function isFirstPage(){
	var pageNo = $("#curPageNo").val();
	return pageNo == "1" ? true:false;
}
//绑定分页按钮事件
function bindPagingEvent(formId){
	//首页
	$("#dataView_first").bind('click',function(){
		if(isFirstPage()){
			return;
		}
		queryPreViewJxb(formId,1);
	});
	//上一页
	$("#dataView_previous").bind('click',function(){
		if(isFirstPage()){
			return;
		}
		var pageNo = $("#curPageNo").val();
		queryPreViewJxb(formId,parseInt(pageNo,"10")-1);
	});
	
	$("#dataView_next").bind('click',function(){
		if(isLastPage()){
			return;
		}
		var pageNo = $("#curPageNo").val();
		queryPreViewJxb(formId,parseInt(pageNo,"10")+1);
	});
	//尾页
	$("#dataView_last").bind('click',function(){
		if(isLastPage()){
			return;
		}
		queryPreViewJxb(formId,getLastPage());
	});
}


function queryPreViewJxb(formId,pageNo){
	//$("#iDisplayLength").val(iDisplayLength);
	//当前显示页数
	$("#curPageNo").val(pageNo);
	$("#"+ formId).submit();
}

/**
 * == 分页结束 == 
 */




/**
 * 实现全选反选功能
 */

function selectAll(){
	if($("input[selector=checkbox]").is(":checked") > 0){
		$("input[selector=checkbox]").attr("checked",false);
	}else{
		$("input[selector=checkbox]").attr("checked",true);
	}
}
		