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

$('.password img').on('click', function () {
    var $passwd = $('.password input[name="password1"]')
    if ($passwd.attr('type') === 'text') {
        $passwd.attr('type', 'password')
    } else {
        $passwd.attr('type', 'text')
    }
})