// Increment quantity
$('.increment-qty').click(function(e) {
    e.preventDefault();
    var closestInput = $(this).closest('.input-group').find('.qty_input');
    var currentValue = parseInt(closestInput.val());
    
    console.log('Current Value:', currentValue);  // Debugging

    if (currentValue < 99) {
        closestInput.val(currentValue + 1);
    }
});

// Decrement quantity
$('.decrement-qty').click(function(e) {
    e.preventDefault();
    var closestInput = $(this).closest('.input-group').find('.qty_input');
    var currentValue = parseInt(closestInput.val());

    console.log('Current Value:', currentValue);  // Debugging

    if (currentValue > 1) {  // Prevent going below 1
        closestInput.val(currentValue - 1);
    }
});
