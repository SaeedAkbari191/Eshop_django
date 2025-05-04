// open & close Cart

var cart = document.querySelector('.cart');

function open_cart() {
    cart.classList.add("active")
}

function close_cart() {
    cart.classList.remove("active")
}

// open & close menu

var menu = document.querySelector('#menu');

function open_menu() {
    menu.classList.add("active")
}

function close_menu() {
    menu.classList.remove("active")
}

//change item image

let bigImage = document.getElementById("bigImg");
let show_large_image_modal = document.getElementById("show_large_image_modal");


function ChangeItemImage(img) {
    let bigImageUrl = img.getAttribute('data-big');
    bigImage.src = bigImageUrl
    show_large_image_modal.href = bigImageUrl
}

/* add itmes in cart */

var all_products_json;

var items_in_cart = document.querySelector(".items_in_cart");
let product_cart = [];

function addToCart(id, btn) {
    product_cart.push(all_products_json[id])
    btn.classList.add("active")

    console.log(id);
    getCartItems()
}

let count_item = document.querySelector('.count_item');
let count_item_cart = document.querySelector('.count_item_cart');
let price_cart_total = document.querySelector('.price_cart_total');

let price_cart_Head = document.querySelector('.price_cart_Head');

function getCartItems() {
    let total_price = 0;
    let items_c = "";

    for (let i = 0; i < product_cart.length; i++) {
        items_c += `

        <div class="item_cart">
                <img src="${product_cart[i].img}" alt="">
                <div class="content">
                    <h4>${product_cart[i].name}</h4>
                    <p class="price_cart">${product_cart[i].price}</p>
                </div>
                <button onClick="remove_from_cart(${i})" class="delete_item"><i class="fa-solid fa-trash-can"></i></button>
            </div>
        
        `
        total_price += product_cart[i].price

    }
    items_in_cart.innerHTML = items_c

    price_cart_Head.innerHTML = "$" + total_price
    count_item.innerHTML = product_cart.length

    count_item_cart.innerHTML = ` (${product_cart.length}Item in Cart)`
    price_cart_total.innerHTML = "$" + total_price
}


function remove_from_cart(index) {
    product_cart.splice(index, 1)
    getCartItems()

    let addToCartButtons = document.querySelectorAll(".fa-cart-plus");
    for (let i = 0; i < addToCartButtons.length; i++) {
        addToCartButtons[i].classList.remove("active")

        product_cart.forEach(product => {
            if (product.id == i) {
                addToCartButtons[i].classList.add("active")
            }
        })
    }
}


// back_to_top js

let back_to_top = document.querySelector(".back_to_top")

back_to_top.addEventListener("click", function () {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    })
})


// function toggleSubcategories(element) {
//     const subList = element.nextElementSibling;
//     const arrow = element.querySelector(".arrow");
//     subList.classList.toggle("open");
//     arrow.classList.toggle("rotate");
// }

// function toggleExclusive(clickedElement) {
//     const allSubLists = document.querySelectorAll('.subcategory-list');
//     const allArrows = document.querySelectorAll('.arrow');
//
//     allSubLists.forEach(list => list.classList.remove('open'));
//     allArrows.forEach(arrow => arrow.classList.remove('rotate'));
//
//     const subList = clickedElement.nextElementSibling;
//     const arrow = clickedElement.querySelector(".arrow");
//
//     subList.classList.add('open');
//     arrow.classList.add('rotate');
// }

function toggleExclusive(element) {
    const subcategoryList = element.nextElementSibling;
    const arrow = element.querySelector('.arrow');

    // اگر زیرشاخه باز است، آن را ببندید و جهت فلش را به حالت اول بازگردانید
    if (subcategoryList.classList.contains('open')) {
        subcategoryList.classList.remove('open');
        arrow.classList.remove('rotate');
    } else {
        // در غیر این صورت، اول همه زیرشاخه‌ها را ببندید
        const allSubcategories = document.querySelectorAll('.subcategory-list');
        allSubcategories.forEach(list => list.classList.remove('open'));

        // سپس فلش‌های همه را به حالت اولیه برگردانید
        const allArrows = document.querySelectorAll('.arrow');
        allArrows.forEach(arrow => arrow.classList.remove('rotate'));

        // زیرشاخه انتخاب‌شده را باز کرده و فلش را بچرخانید
        subcategoryList.classList.add('open');
        arrow.classList.add('rotate');
    }
}

setTimeout(() => {
    document.getElementById('alertBox').classList.add('alert-hidden');
}, 5000);

var filter = document.querySelector(".filter")

function open_close_filter() {
    filter.classList.toggle("active")
}

//  DD TO ORDER
function AddToOrder(product_id) {
    const count = $('#product-count').val();
    $.get('/order/add-to-order?product_id=' + product_id + '&count=' + count).then(response => {
        Swal.fire({
            title: "Are you sure?",
            text: response.text,
            icon: response.icon,
            showCancelButton: false,
            confirmButtonColor: "#3085d6",
            confirmButtonText: response.confirmButtonText
        }).then((result) => {

            if (result.isConfirmed && response.status ==='Not_Authorized') {

                window.location.href = '/login';

            }
        });
    })
}


