from django.test import TestCase
from .models import Image, Profile

# Create your tests here.


class ImageTestClass(TestCase):
    """
    Test class for image module
    """

    def setUp(self):
        """
        Method to create an instance of the image before each test
        """

        self.new_image = Image(
            image='image.jpg', image_name='sample_name', image_caption='Restricted', profile=2)
        self.new_image.save()

    def tearDown(self):
        Image.objects.all().delete()

    def test_instance(self):
        """
        Test method to check for correct instantiation
        """
        self.assertTrue(isinstance(self.new_image, Image))

    def test_save_method(self):
        """
        Test method for save method
        """
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)


class ProfileTestClass(TestCase):
    def setUp(self):
        """
        Method to create an instance of the image before each test
        """

        self.new_profile = Profile(photo='image.jpg', user=2)
        self.new_image.save()

    def test_instance(self):
        """
        Test method to check for correct instantiation
        """
        self.assertTrue(isinstance(self.new_profile, Profile))
