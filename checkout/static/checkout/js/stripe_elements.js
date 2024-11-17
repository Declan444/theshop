/*
Core logic/payments flow for this comes from here:
https://stripe.com/docs/payments/accept-a-payment

CSS from here:
https://stripe.com/docs/stripe-js
*/

// Extract public key and client secret from hidden elements
var stripePublicKey = $('#id_stripe_public_key').text().trim();
var clientSecret = $('#id_client_secret').text().trim();

// Initialize Stripe
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

// Define custom style for the card input
var style = {
    base: {
        color: '#445261',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#445261',
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


// Handl form submit
var form = document.getElementById('payment-form');
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true)
stripe.confirmCardPayment(clientSecret, {
    payment_method: {
        card: card,
       
    }
}).then(function(result) {
    if (result.error) {
        displayError.textContent = result.error.message;
        card.update({ 'disabled': false});
        $('#submit-button').attr('disabled', false)
    } else {
        //The payment has been processed
        if (result.paymentIntent.status === 'succeeded') {
            form.submit();
        }
    }
})