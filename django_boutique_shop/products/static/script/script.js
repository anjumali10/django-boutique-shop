document.querySelectorAll('.size-btn').forEach(button => {
    button.addEventListener('click', function() {
        // Remove 'selected' class from all buttons
        document.querySelectorAll('.size-btn').forEach(btn => btn.classList.remove('selected'));
        
        // Add 'selected' class to the clicked button

        this.classList.add('selected');

        // Update the hidden input value with the selected size
        const selectedSize = this.getAttribute('data-size');
        document.getElementById('selected-size').value = selectedSize;

        // console.log('Selected size:', selectedSize); // Optional: For debugging
    });
});

document.addEventListener('DOMContentLoaded', () => {
    // Initialize the total when the page loads
    updateOverallTotal();
});
// Function for cart quantity
let quantity = 1;
// let total_price = document.querySelector('.total_price');
let pricePerUnit = document.querySelector('.total_price').textContent.split('.')[1];

function updateQuantity(button, change) {
    // Get the card element that the button belongs to
    const card = button.closest('.cart-card');
    
    // Get the current quantity and price elements
    let quantityElement = card.querySelector('#quantity');
    let totalPriceElement = card.querySelector('.total_price');

    // Get the price per unit from the total price element
    // let pricePerUnit = parseInt(totalPriceElement.textContent.split('.')[1]);

    // Get the current quantity
    // let quantity = parseInt(quantityElement.textContent);
    
    // Update the quantity
    quantity += change;

    // Ensure quantity doesn't go below 1
    if (quantity < 1) {
        card.remove()
    }

    // Update the displayed quantity
    quantityElement.textContent = quantity;

    // Calculate and update total price for this card
    let totalPrice = pricePerUnit * quantity;
    totalPriceElement.textContent = `RS.${totalPrice}.00`;

    // Update the overall total
    updateOverallTotal();
}

function updateOverallTotal() {
    let total = document.querySelector('.total');
    let cards = document.querySelectorAll('.cart-card');
    let total_price = 0;

    for (const card of cards) {
        let pricePerCart = parseInt(card.querySelector('.total_price').textContent.split('.')[1]);
        total_price += pricePerCart; // Multiply by quantity for total
    }
    
    total.textContent = `Total: RS.${total_price}.00 PKR`;
}



