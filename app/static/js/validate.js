$(document).ready(function(){
    $('#submitButton').click(function(){
        if ($('#contentInput').val() == ""){
            $('#validateModal').modal('toggle')
            return false
        }else{
            return true

        }
    });
});
