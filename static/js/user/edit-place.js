function AddBlockShow(obj) {
    $('.step-edit-block .active').removeClass('active')
    $(obj).addClass('active')
    $('.edit-my-trip-place').hide()
    $('.add-my-trip-place').show()
}

function EditBlockShow(obj) {
    $('.step-edit-block .active').removeClass('active')
    $(obj).addClass('active')
    $('.add-my-trip-place').hide()
    $('.edit-my-trip-place').show()
    CheckPlaceAjax()
}

function ToggleImageDelete(obj) {
    let $parent = $(obj).closest('.block-place')
    let $input = $(obj).find('input')
    if ($input.is(':checked')) {
        $parent.find('.text').css('opacity', '0.5')
        $parent.find('.image').css('opacity', '0.5')
        $parent.find('.checkbox-delete div').addClass('check-delete')
    } else {
        $parent.find('.text').css('opacity', '1')
        $parent.find('.image').css('opacity', '1')
        $parent.find('.checkbox-delete div').removeClass('check-delete')
    }
}

function CheckPlaceAjax() {
    $.ajax({
        type: 'GET',
        url: '/users/place_get/',
        cache: false,
    }).done(function (response) {
        let $parent = $('.edit-my-trip-place')
        for (let i = 0; i < response.length; i++) {
            let $placeBlock = $('.edit-my-trip-place .block-place').last().clone();
            let id_place = $placeBlock.find("input[id$='-place']").attr('id');
            let id_visit_date = $placeBlock.find("input[id$='-visit_date']").attr('id');
            let id_visit_time = $placeBlock.find("input[id$='-visit_time']").attr('id');
            let id_delete = $placeBlock.find("input[id$='-DELETE']").attr('id');
            let parts_place = id_place.split('-')
            let parts_visit_date = id_visit_date.split('-')
            let parts_visit_time = id_visit_time.split('-')
            let parts_delete = id_delete.split('-')
            let n = parseInt(parts_place[1]) + 1;
            id_place = parts_place[0] + '-' + n + '-' + parts_place[2];
            id_visit_date = parts_visit_date[0] + '-' + n + '-' + parts_visit_date[2];
            id_visit_time = parts_visit_time[0] + '-' + n + '-' + parts_visit_time[2];
            id_delete = parts_delete[0] + '-' + n + '-' + parts_delete[2];
            $placeBlock.find("input[id$='-place']").attr('id', id_place);
            $placeBlock.find("input[id$='-visit_date']").attr('id', id_visit_date);
            $placeBlock.find("input[id$='-visit_time']").attr('id', id_visit_time);
            $placeBlock.find("input[id$='-DELETE']").attr('id', id_delete);
            let name_place = id_place.substring(3);
            let name_visit_date = id_visit_date.substring(3);
            let name_visit_time = id_visit_time.substring(3);
            let name_delete = id_delete.substring(3);
            $placeBlock.find("input[id$='-visit_time']").val('')
            $placeBlock.find("input[id$='-visit_date']").val('')
            $placeBlock.find("input[id$='-place']").attr('name', name_place);
            $placeBlock.find("input[id$='-place']").val(response[i].id)
            $placeBlock.find("input[id$='-visit_date']").attr('name', name_visit_date);
            $placeBlock.find("input[id$='-visit_time']").attr('name', name_visit_time);
            $placeBlock.find("input[id$='-DELETE']").attr('name', name_delete);

            $placeBlock.find('.image').css('background-image', "url('" + response[i].image[0].img + "')")
            $placeBlock.find('.text h5').text(response[i].title)
            $placeBlock.find('.text p').text('Город: ' + response[i].city.title)
            $parent.append($placeBlock)
            // Изменяем количество полей на странице на +1
            let $totalForms = $('#id_userplace_set-TOTAL_FORMS');
            let totalFormsCount = parseInt($totalForms.val());
            $totalForms.val(totalFormsCount + 1);
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