function CheckPlaceAjax() {
    jQuery.ajax({
        url: '/users/set_formset_user_trip/',
        type: 'POST',
        headers: {
            "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()
        },
        data: {'place': true},
        success: function (json) {
            // Если запрос прошёл успешно и сайт вернул результат
            if (json.result) {
                $(".places-pagination").replaceWith(json.articles); // Заменяем div со списком статей на новый
                $('.places-pagination .time').clockTimePicker({
                    colors: {
                        selectorColor: '#0499dd',
                        popupHeaderBackgroundColor: '#0499dd',
                        buttonTextColor: '#0499dd',
                        timeFormat: 'h:i a'
                    },
                    fonts: {
                        buttonFontSize: 18,
                    },
                    i18n: {
                        cancelButton: "Отмена",
                    },
                });
                $('.date').datepicker({
                    format: 'dd.mm.yyyy',
                    language: 'ru-RU',
                    startDate: 'now',
                    filter: function (date, view) {
                        if (date.getDay() === 0 && view === 'day') {
                            return false; // Disable all Sundays, but still leave months/years, whose first day is a Sunday, enabled.
                        }
                    }
                });
            }
        }
    });
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
        $('.download').attr('href', request['url'])
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