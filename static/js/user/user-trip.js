function CheckPlaceAjax() {
    $.ajax({
        type: 'GET',
        url: '/users/place_get/',
        cache: false,
    }).done(function (response) {
        let $parent = $('.third-step-block')
        $parent.find('.block-place').eq(0)
        $parent.find('.block-place:gt(0)').remove()
        for (let i = 0; i < response.length; i++) {
            let $placeBlock = $('.third-step-block .block-place').last().clone().css('display', 'grid');
            let id_place = $placeBlock.find("input[id$='-place']").attr('id');
            let id_visit_date = $placeBlock.find("input[id$='-visit_date']").attr('id');
            let id_visit_time = $placeBlock.find("input[id$='-visit_time']").attr('id');
            let parts_place = id_place.split('-')
            let parts_visit_date = id_visit_date.split('-')
            let parts_visit_time = id_visit_time.split('-')
            let n = parseInt(parts_place[1]) + 1;
            id_place = parts_place[0] + '-' + n + '-' + parts_place[2];
            id_visit_date = parts_visit_date[0] + '-' + n + '-' + parts_visit_date[2];
            id_visit_time = parts_visit_time[0] + '-' + n + '-' + parts_visit_time[2];
            $placeBlock.find("input[id$='-place']").attr('id', id_place);
            $placeBlock.find("input[id$='-visit_date']").attr('id', id_visit_date);
            $placeBlock.find("input[id$='-visit_time']").attr('id', id_visit_time);
            let name_place = id_place.substring(3);
            let name_visit_date = id_visit_date.substring(3);
            let name_visit_time = id_visit_time.substring(3);
            $placeBlock.find("input[id$='-place']").attr('name', name_place);
            $placeBlock.find("input[id$='-place']").val(response[i].id)
            $placeBlock.find("input[id$='-visit_date']").attr('name', name_visit_date);
            $placeBlock.find("input[id$='-visit_time']").attr('name', name_visit_time);

            $placeBlock.find('.image').css('background-image', "url('" + response[i].image[0].img + "')")
            $placeBlock.find('.text h5').text(response[i].title)
            $placeBlock.find('.text p').text('Город: ' + response[i].city.title)
            $parent.append($placeBlock)
            // Изменяем количество полей на странице на +1
            let $totalForms = $('#id_userplace_set-TOTAL_FORMS');
            let totalFormsCount = parseInt($totalForms.val());
            $totalForms.val(totalFormsCount + 1);
        }
        if ($('.third-step-block .block-place').length !== 1) {
            $('.third-step-block .block-place').first().remove();
        }else{
            $('.third-step-block .block-place').first().hide();
        }
    })
}

function CheckPlace(obj, id, check) {
    if (check) {
        $(obj).attr('src', '/static/img/user/check-place.svg')
        $(obj).attr('onclick', `CheckPlace(this, ${id}, false)`)
    } else {
        $(obj).attr('src', '/static/img/user/checked-place.svg')
        $(obj).attr('onclick', `CheckPlace(this, ${id}, true)`)
    }
    $.ajax({
        url: '/users/set_cache/',
        type: 'GET',
        cache: false,
        data: {'id': id}
    })
}


$('.switch-date').on('click', function () {
    let $parent = $(this).closest('.add-date')
    if ($(this).is(':checked')) {
        $parent.find('.drop-block').show()
    } else {
        $parent.find('.drop-block').hide()
    }
})

function setCookie(name, value, options = {}) {

    options = {
        path: '/users/create_user_trip/',
    };

    if (options.expires instanceof Date) {
        options.expires = options.expires.toUTCString();
    }

    let updatedCookie = encodeURIComponent(name) + "=" + encodeURIComponent(value);

    for (let optionKey in options) {
        updatedCookie += "; " + optionKey;
        let optionValue = options[optionKey];
        if (optionValue !== true) {
            updatedCookie += "=" + optionValue;
        }
    }

    document.cookie = updatedCookie;
}

function deleteCookie(name) {
    setCookie(name, "", {
        'max-age': -1
    })
}

function getCookie(name) {
    let matches = document.cookie.match(new RegExp(
        "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}

$('#form').ajaxForm(function (request) {
    if (!request['status']) {
        $('.error').show()
        $('.step-block-4').hide()
    } else {
        $('.error').hide()
        $('.step-block-4').show()
    }
});

const title = document.getElementById("id_title");


title.addEventListener("input", function (event) {
    if (title.validity.valueMissing) {
        $('.next').attr('disabled', true);
    } else {
        title.setCustomValidity("");
    }
});