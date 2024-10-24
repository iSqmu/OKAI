const $byn = $('#ByN')
const $dColors = $('#colors')

if(location.search == '?byn=active'){
	$byn.checked = true;
} else {
	$byn.checked = false;
}

$byn.addEventListener('click', () => {
	if($byn.checked){
		location.search = '?byn=active'
	} else {
		location.search = '?byn=inactive'
	}
})

$dColors.addEventListener('click', () => {
	if($dColors.checked){
		location.search = '?dcolors=active'
	} else {
		location.search = '?dcolors=inactive'
	}
})