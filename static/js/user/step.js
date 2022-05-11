function ClickStep(num) {
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
    $parent.find(`.step-${num}`).addClass('active')
    $('.next').attr('onclick', `NextStep(${num + 1})`)
    $('.last').attr('onclick', `LastStep(${num - 1})`)
}

function NextStep(num) {
    if ($('input[name="title"]').val() === ''){
        $('.next').attr('disabled', true)
        $('input[name="title"]').css('border', '1px solid #C60000')
        $('input[name="title"]').attr('placeholder', 'Обязательное поле')
    }else {
        ClickStep(num)
    }
}

function LastStep(num) {
    ClickStep(num)
}

$(document).ready(function () {
    ClickStep(1)
})

$('input[name="title"]').on('change', function (){
    if ($(this).val() === ''){
        $('.next').attr('disabled', true)
        $(this).css('border', '1px solid #C60000')
        $(this).attr('placeholder', 'Обязательное поле')
    }else{
        $('.next').removeAttr('disabled')
        $(this).css('border', '1px solid #D4D5DA')
        $(this).attr('placeholder', '')
    }
})