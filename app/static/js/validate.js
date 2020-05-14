$(document).ready(function(){
    $('#submitButton').click(function(){
        if ($('#contentInput').val() == ""){
            console.log($('#contentInput').val())
            $('#validateModal').modal('toggle')
            return false
        }else{
            return true

        }
    });
});