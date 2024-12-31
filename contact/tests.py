from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from .models import Contact  
from .forms import ContactForm


class ContactViewTests(TestCase):
    def test_get_contact_page(self):
        """
        Test that the contact page loads correctly with the form.
        """
        response = self.client.get(reverse("contact"))  
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact/contact.html")
        self.assertIsInstance(response.context["form"], ContactForm)

    def test_post_valid_contact_form(self):
        """
        Test submitting a valid form, ensuring it saves and redirects.
        """
        form_data = {
            "name": "Test User",
            "email": "testuser@example.com",
            "subject": "Test Subject",
            "message": "Test message content.",
        }
        response = self.client.post(reverse("contact"), data=form_data)
        
        # Check the form submission saves correctly
        self.assertEqual(Contact.objects.count(), 1)
        self.assertRedirects(response, reverse("contact_success"))

        # Check success message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Your message has been sent successfully! We will get back to you soon.")

    def test_post_invalid_contact_form(self):
        """
        Test submitting an invalid form, ensuring it doesn't save and errors are shown.
        """
        invalid_form_data = {
            "name": "",  
            "email": "invalidemail",  
            "subject": "Test Subject",
            "message": "Test message content.",
        }
        response = self.client.post(reverse("contact"), data=invalid_form_data)
        
        # Check the form does not save
        self.assertEqual(Contact.objects.count(), 0)
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, "contact/contact.html")
        self.assertContains(response, "An error occurred. Please try again.")

        # Check error messages in the form
        form = response.context["form"]
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)
        self.assertIn("email", form.errors)
