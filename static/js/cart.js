let updateBtn = document.getElementsByClassName('update-cart')
let navbar = document.getElementsByClassName('product-nav')
let cartCard = document.getElementsByClassName('cart-card')
let cartTotal = document.getElementById('cart-total')

cartTotal.textContent = cart_total

const flashContainer = document.getElementById('flash-container')

for (var i = 0 ; i < updateBtn.length; i++) {
    updateBtn[i].addEventListener('click', function(){
        
        let productId = this.dataset.product
        let action = this.dataset.action
        
        if(user == 'AnonymousUser'){
            addCookieItem(productId, action)
        }

        else{
            updateUserOrder(productId, action)
        }
    })
}
  
function addCookieItem(productId, action){
   if(action == "add"){
        if(cart[productId] == undefined){
            cart[productId] = {'quantity':1}
        }
        else{
            cart[productId]['quantity'] += 1
        }
   }
   if (action == 'remove'){
       cart[productId]['quantity'] -= 1

       if(cart[productId]['quantity'] <=0){
           delete cart[productId]
       }
   }
   document.cookie = 'cart='+ JSON.stringify(cart) + ";domain=;path=/"
   location.reload()
}


/* For Updating User Order */

function updateUserOrder(productId,action){

    fetch('/update_item/', {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken
        },
        body:JSON.stringify({
            'productId':productId,
            'action':action
        })
    })
    .then((response) =>  response.json())
    .then((data) => {
        location.reload();
    })
}


function flashMessage(){
    const para = document.createElement('P')
    para.classList.add('flash')
    para.innerHtml = "Added to Cart &times;"
    flashContainer.appendChild(para)
    para.classList.add('fade-out')

    setTimeout(() => {
        flashContainer.removeChild(para)

    },3000);
}