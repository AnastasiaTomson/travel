// Изменение картинки - для кастомизированного инпута изображения
var _URL = window.URL || window.webkitURL;

// Изменение картинки - для кастомизированного инпута изображения
function ChangeImage(obj) {
    let input = obj;
    var img = new Image();
    img.onload = function () {
        $('#image').attr('style', `background-image: url("${img.src}")`)
    }
    img.src = _URL.createObjectURL(input.files[0]);
}