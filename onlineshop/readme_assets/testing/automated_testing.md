### Automated Testing
 **Contact Us Form Test** 
| **Test Name**         | **Description**                                                | **Assertion/Result**          |
|-----------------------|----------------------------------------------------------------|-------------------------------|
| test_get_contact_page | Tests that the contact page loads correctly with the form. | Passed - Verifies the page returns a 200 status code, uses the correct template, and contains a ContactForm. |
| test_post_valid_contact_form | Tests submitting a valid form, ensuring it saves the data and redirects. | Passed - Verifies that the contact form submission results in saving the form data to the database and redirects to the success page. Confirms the success message is displayed. |
| test_post_invalid_contact_form | Tests submitting an invalid form, ensuring errors are shown and the data is not saved. | Passed - Verifies that submitting an invalid form does not save data, shows appropriate error messages, and keeps the user on the contact page with validation errors displayed. |
|

 