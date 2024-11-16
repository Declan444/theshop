/*
Core logic/payments flow for this comes from here:
https://stripe.com/docs/payments/accept-a-payment

CSS from here:
https://stripe.com/docs/stripe-js
*/

// Extract public key and client secret from hidden elements
var stripe_public_key = $('#id_stripe_public_key').text().trim();
var client_secret = $('#id_client_secret').text().trim();

// Initialize Stripe
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

// Define custom style for the card input
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

// Create and mount the card element
var card = elements.create('card', { style: style });
card.mount('#card-element');

// Add error handling (optional but recommended)
card.addEventListener('change', function(event) {
    var displayError = document.getElementById('card-errors');
    if (event.error) {
        displayError.textContent = event.error.message;
    } else {
        displayError.textContent = '';
    }
});
