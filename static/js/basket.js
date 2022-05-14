window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        let target = event.target;
        let basketID = target.name
        let basketQuantity = target.value

        $.ajax({
            url: "/baskets/basket_edit/" + basketID + '/' + basketQuantity + '/',
            success: function (data) {
                $('.basket_list').html(data.result);
            }
        })
    })
}

window.onload = function () {
    $('.card-footer').on('click', 'a[type="button"]', function () {
        let target = event.target;
        let product_id = target.href.product.id;
        $.ajax({
            url: '/baskets/basket_add/' + product_id + '/',
            success: function (data) {
                $('.card-footer').html(data.request);
            }
        })
    })
}


