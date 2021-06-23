let updateBtn = document.getElementsByClassName('update-cart')
let navbar = document.getElementsByClassName('product-nav')
let cartCard = document.getElementsByClassName('cart-card')
let cartTotal = document.getElementById('cart-total')
const flashContainer = document.getElementById('flash-container')


        for (var i = 0 ; i < updateBtn.length; i++) {
            updateBtn[i].addEventListener('click', function(){
                
                var productId = this.dataset.product
                var action = this.dataset.action
            
               
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




function updateUserOrder(productId,action){

    var url = '/update_item/'

    fetch(url, {
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
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log(data)
        cartTotal.textContent = data.cart_items
    })
}


function flashMessage(){
    const para = document.createElement('P')
    para.classList.add('flash')
    para.innerHtml = "Added to Cart &times;"
    console.log("Hello")
    flashContainer.appendChild(para)
    para.classList.add('fade-out')

    setTimeout(() => {
        flashContainer.removeChild(para)

    },3000);
}