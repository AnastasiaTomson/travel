function ClickStep(obj, num) {
    let $parent = $('.create-user-trip')
    $parent.find(`.step-block`).hide()
    $parent.find(`.step-block-${num}`).show()
    if (num === 3) {
        CheckPlaceAjax()
    }
    if (num === 4) {
        $('#form').submit()
        $('.next').css('opacity', '0')
        $('.last').css('opacity', '1')
        $parent.find(`.line`).addClass('active')
        $(`.steps > span`).addClass('active')
    }
    if (num < 4) {
        $parent.find(`.line:gt(${num - 1})`).removeClass('active')
        if (num === 1) {
            $('.last').css('opacity', '0')
        } else {
            $('.last').css('opacity', '1')
        }
        $('.next').css('opacity', '1')
    }
    $parent.find(`.line-${num}`).addClass('active')
    $(`.steps > span:gt(${num - 1})`).removeClass('active')
    $(obj).addClass('active')
    $('.next').attr('onclick', `NextStep(${num + 1})`)
    $('.last').attr('onclick', `LastStep(${num - 1})`)
}

function NextStep(num) {
    $('.step-' + num).click()
}

function LastStep(num) {
    $('.step-' + num).click()
}

$(document).ready(function () {
    $('span.active').click()
})
