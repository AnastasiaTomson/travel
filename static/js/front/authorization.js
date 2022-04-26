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
        $(this).attr({'src': '/static/img/front/eye.png', 'style': 'height:8px; top:24px'})
    } else {
        $passwd.attr('type', 'text')
        $(this).attr({'src': '/static/img/front/eye_open.png', 'style': 'height:18px; top:17px'})
    }
})