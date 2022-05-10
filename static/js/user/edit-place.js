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