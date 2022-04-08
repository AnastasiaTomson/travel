function ShowAuthorization() {
    $('.modal-block').css('display', 'flex')
}

$('.modal-block').on('click', function (e) {
    if ($('.modal-block').is(':visible')) {
        if (!$('.modal-window').is(e.target) && $('.modal-window').has(e.target).length === 0) {
            $('.modal-block').hide()
        }
    }
})