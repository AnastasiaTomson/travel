function AddPlaceToTrip(id) {
    $('.modal-block').children().hide()
    $('.modal-block').css('display', 'flex')
    $('.add-to-trip').show()
    $('.add-to-trip').attr('data-id_place', id)
    $('.trips button').removeAttr('disabled')
    $('.trips button').text('Добавить')
}

function AddPlaceToTripModal(obj, trip_id) {
    $.ajax({
        url: '/users/add_place_to_trip/',
        type: 'POST',
        data: {'trip_id': trip_id, 'place_id': $('.add-to-trip').attr('data-id_place')},
        headers: {
            "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()
        },
        success: function (json) {
            // Если запрос прошёл успешно и сайт вернул результат
            if (json.result) {
                $(obj).text('Добавлено')
                $(obj).attr('disabled', true)
            }
        }
    })
}

function CreateTripModal(obj, place_id){
    $('.modal-block').children().hide()
    $('.modal-block').css('display', 'flex')
    $('.create-trip').show()
    $('.create-trip input[name="place_id"]').val(place_id)
}