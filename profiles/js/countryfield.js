let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', '#445261');
}
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $('#id_default_country').css('color', '#445261');
    } else {
        $('#id_default_country').css('color', '#000'); 
    }
});