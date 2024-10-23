$(document).ready(function () {
	$('input[type="checkbox"]').change(function () {
		var checkboxName = $(this).attr('name');
		var checkboxValue = $(this).prop('checked');

		$.ajax({
			type: 'POST',
			url: '/process',
			data: { checkbox_name: checkboxName, checkbox_value: checkboxValue },
			success: function (data) {
				console.log('Checkbox updated successfully!');
			},
		});
	});
});
