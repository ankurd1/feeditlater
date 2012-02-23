$(function() {
    loadOptions();
    $("#secret").focus(function() {
        $("#saved").hide();
    });
});

function loadOptions() {
    var currentSecret = localStorage["secret"];
    $("#secret").val(currentSecret);
}

function saveOptions() {
    localStorage["secret"] = $("#secret").val();
    $("#saved").fadeIn();
}
