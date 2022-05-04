// to get current year
function getYear() {
    const currentDate = new Date();
    document.querySelector("#displayYear").innerHTML = currentDate.getFullYear();
}

getYear();

if (localStorage.getItem('cart') == null) {
    console.log("Nothing in cart")
    setCartCount(0)
} else {
    let cart = JSON.parse(localStorage.getItem('cart'));
    let all_slugs = []
    if (cart.length > 0) {
        setCartCount(Object.keys(cart).length)
        for (const cartItem of cart) {
            console.log("cartItem.slug: ", cartItem.slug)
            all_slugs.push(cartItem.slug)
        }

        let allbuttons = $(".addToCartBtn")
        // console.log("allbuttons: ",allbuttons)
        for (const button of allbuttons) {
            let slug = button.getAttribute('data-slug')
            // console.log("button: ", slug, button)
            if ($.inArray(slug, all_slugs) > -1) {
                // the value is in the array
                $(button).text("Remove from cart")
            }

        }
        computeCartDetails()

    } else {
        setCartCount(0)
    }
}

function search(nameKey, myArray) {
    console.log("searching for ", nameKey, " in ", myArray)
    for (let i = 0; i < myArray.length; i++) {
        if (myArray[i].slug === nameKey) {
            return myArray[i];
        }
    }
}

$("#checkoutBtn").click(function () {
    console.log("checkoutBtn clicked ")
    let itemsArray = localStorage.getItem('cart') ? JSON.parse(localStorage.getItem('cart')) : []
    if (itemsArray.length === 0) {
        alert("Add some items to your cart.")
    }else{
        window.location = '/checkout/'
    }
});


$(".addToCartBtn").click(function () {
    // Holds the product ID of the clicked element
    let slug = $(this).attr('data-slug').replace(/\s+/g, '')

    let products = localStorage.getItem('cart') ? JSON.parse(localStorage.getItem('cart')) : []
    let findSlugInProducts = search(slug, products);
    console.log("findSlugInProducts: ", findSlugInProducts)

    if (findSlugInProducts) {
        console.log("product present in localStorage. So remove")
        removeFromCart(slug)
        $(this).text("Add to cart")
        return
    }

    // console.log("addToCartBtn slug: ", $(this).attr('data-slug').replace(/\s+/g, ''))
    // console.log("price: ", $(this).parent().find('span.price').text().replace(/\s+/g, '').replace('$', ''))
    let imgSrc = $(this).parent().parent().parent().find('img').attr('src')
    let title = $(this).parent().parent().find('a.title').text()
    let price = $(this).parent().find('span.price').text().replace(/\s+/g, '').replace('₦', '')
    const product = {
        title: title, slug: slug, price: price, imgSrc: imgSrc
    }
    // turn button to remove from cart
    $(this).text("Remove from cart")
    addToCart(product)
});


function removeFromCart(slug) {
    console.log('removeFromCart ', slug)
    let products = localStorage.getItem('cart') ? JSON.parse(localStorage.getItem('cart')) : []
    products = products.filter(arr => arr.slug !== slug)
    console.log('removeFromCart products', products)
    setCartCount(products.length)
    localStorage.setItem('cart', JSON.stringify(products))
    computeCartDetails()
}

function addToCart(product) {
    console.log('Adding to cart ', product)
    let itemsArray = localStorage.getItem('cart') ? JSON.parse(localStorage.getItem('cart')) : []
    itemsArray.push(product)
    setCartCount(itemsArray.length)
    localStorage.setItem('cart', JSON.stringify(itemsArray))
    computeCartDetails()
}

function computeCartDetails() {
    // formats the details of the cart from localstorage
    console.log('computing Cart Details')
    let itemsArray = localStorage.getItem('cart') ? JSON.parse(localStorage.getItem('cart')) : []
    let shoppingCartItems = document.getElementById('shoppingCartItems')
    shoppingCartItems.innerHTML = '' // clear previous items
    let totalPriceCart = 0
    $('span#totalPriceCart').text(`₦0`)

    if (itemsArray.length > 0) {
        for (const cartItem of itemsArray) {
            console.log("cartItem: ", cartItem)
            let li = document.createElement("li")
            li.className = "clearfix"
            li.setAttribute("data-slug", `${cartItem.slug}`);
            li.innerHTML = `
            <img src="${cartItem.imgSrc}" alt="${cartItem.title}"/>
            <div class="d-inline-block">
                <span class="item-name">${cartItem.title}</span>
                <span class="item-detail">Full service</span>
                <span class="item-price">₦${cartItem.price}</span>
            </div>`
            shoppingCartItems.prepend(li)
            totalPriceCart += parseFloat(cartItem.price)
        }
        $('span#totalPriceCart').text(`₦ ${totalPriceCart}`)

    }

}


function setCartCount(number) {
    console.log('setCartCount to number ', number)
    const text = `Cart <span class="badge">${number}</span>`

    $('span#cartTotal').html(text)
    $('span#badgeHeader').text(number)
}

// ----------------------------------------------------------------------------------------------------------------

(function () {
    $(document).click(function () {
        let $item = $(".shopping-cart");
        if ($item.hasClass("active")) {
            $item.removeClass("active");
        }
    });

    $('.shopping-cart').each(function () {
        let delay = $(this).index() * 50 + 'ms';
        $(this).css({
            '-webkit-transition-delay': delay,
            '-moz-transition-delay': delay,
            '-o-transition-delay': delay,
            'transition-delay': delay
        });
    });

    $('#cartBtn').click(function (e) {
        e.stopPropagation();
        $(".shopping-cart").toggleClass("active");
    });


})();
