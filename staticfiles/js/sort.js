// Code to sort from the sort box on the products.html page

// Scroll to the top of the page when ".btt-link" is clicked
$(".btt-link").click(function () {
    window.scrollTo(0, 0);
});

// Update sorting parameters in the URL based on #sort-selector value
$("#sort-selector").change(function () {
    const selector = $(this);
    const currentUrl = new URL(window.location);

    // Get the selected sorting value
    const selectedVal = selector.val();

    if (selectedVal !== "reset") {
        const [sort, direction] = selectedVal.split("_");

        // Update URL parameters for sorting and direction
        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);
    } else {
        // If "reset" is selected, clear sorting parameters from the URL
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");
    }

    // Redirect to the updated URL
    window.location.replace(currentUrl);
});

