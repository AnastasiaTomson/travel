function CheckPlace(obj) {
    let $parent = $(obj)
    let $input = $parent.find('input')
    if ($input.is(':checked')) {
        $parent.find('img').attr('src', '/static/img/user/checked-place.svg')
    }else {
        $parent.find('img').attr('src', '/static/img/user/check-place.svg')
    }
}