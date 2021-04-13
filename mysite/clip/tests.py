from django.test import TestCase
from .models import Hairclip
from django.urls import reverse


class ClipGoTests(TestCase):
    print("ПОЕХАЛИ")
    print()

    def test_category_crab_go(self):

        hairclip = Hairclip.objects.filter(category='краб')
        response = self.client.get(reverse('clip:category_crab'))
        self.assertEqual(response.status_code, 200,)
        self.assertTrue('page_obj' in response.context)
        self.assertTemplateUsed(response, 'clip/category_crab.html')
        self.assertEqual(len(hairclip), 1)

    def test_category_spring_go(self):
        hairclip = Hairclip.objects.filter(category='пружинки')
        response = self.client.get(reverse('clip:category_spring'))
        self.assertEqual(response.status_code, 200,)
        self.assertTrue('page_obj' in response.context)
        self.assertTemplateUsed(response, 'clip/spring_list.html')
        self.assertEqual(len(hairclip), 0)

    def test_HomePageView(self):
        hairclip = Hairclip.objects.all()
        response = self.client.get(reverse('clip:all'))
        self.assertTemplateUsed(response, 'clip/all.html')
        self.assertEqual(response.status_code, 200, )
        self.assertEqual(len(hairclip), 1)

    def test_emty_order_go(self):
        response = self.client.get(reverse('clip:emty_order'))
        self.assertEqual(response.status_code, 200, )
        self.assertTemplateUsed(response, 'clip/order.html')

    def test_in_cart_go(self):
        response = self.client.get(reverse('clip:in_cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'clip/cart_list.html')

    def test_redirect_manage_cart(self):
        response = self.client.get(reverse('clip:manage_cart'))
        self.assertRedirects(response, '/in_cart')

    def test_cart(self):
        response = self.client.get(reverse('clip:cart'))
        self.assertRedirects(response, '/all/')
