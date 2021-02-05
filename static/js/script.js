$(document).ready(function(){
    $('.carousel').carousel({
    interval: 3000
    });
});

function displayModal(e)
{
    console.log(e.id);
    var modal = document.getElementById(e.id);
    modal.style.display = "block";

    $(".close").click(function() {
        modal.style.display = "none";
    });

}
