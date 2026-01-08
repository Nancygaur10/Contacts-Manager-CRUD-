from django.test import TestCase
from .models import Contact

class ContactTest(TestCase):
    def test_create_contact(self):
        contact = Contact.objects.create(
            name="John",
            email="john@test.com",
            phone="1234567890"
        )
        self.assertEqual(Contact.objects.count(), 1)

    def test_soft_delete(self):
        contact = Contact.objects.create(
            name="Jane",
            email="jane@test.com",
            phone="1234567890"
        )
        contact.is_deleted = True
        contact.save()
        self.assertTrue(contact.is_deleted)
