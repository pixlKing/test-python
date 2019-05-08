function setDic(){
	var getDic = document.forms['form-dic'].attributes.dic.value;
	$('#dic-select').val(getDic);
	console.log(getDic)
}
setDic()
