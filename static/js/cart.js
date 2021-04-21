let updateBtn = document.getElementsByClassName('update-cart')

for(let i=0; i< updateBtn.length;i++){
    updateBtn[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log(productId, action,updateBtn[i])

        if(user == 'AnonymousUser'){
            console.log('Not logged in')
        }

        else{
            updateUserOrder(productId, action)
        }
    })
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
        location.reload()
    })
}