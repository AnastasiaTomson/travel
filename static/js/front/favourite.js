function CheckFavouritePlace(obj, id){
    $.ajax({
        url: '/place/favourite_place/'+id,
        type: 'GET',
        success: function (response){
            if (response.status) {
                if (response.type === 'active') {
                    $(obj).attr('src', '/static/img/front/like-active.svg')
                } else {
                    $(obj).attr('src', '/static/img/front/like.svg')
                }
            }
        }
    })
}