from django.test import TestCase, RequestFactory
from .models import Hairclip, Ordershop, Positions
from django.urls import reverse
from django.contrib.auth.models import User

class ClipGoTests(TestCase):
    print("ПОЕХАЛИ")
    print()

    @classmethod
    def setUpTestData(cls):
        crab =Hairclip.objects.create(category='краб', title='Желтый',
        img='/home/katerina/PycharmProjects/shop/mysite/media/hairclip/цветы_полевые_P67292b.jpg',
        characteristic='пластик', price='10')

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

        #print(len(response.context['homepage_list']))
        # # print(len(response.context['page_obj']))
        # # print(len(response.context['hairclip_list']))
        # # print(len(response.context['paginator']))
        # print(response.context)

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

# class UserTests(TestCase):
#     def setUp(self):
#
#         #user = User.objects.create_user(username='katrinkbalakina@gmail.com', password='k')
#         #request.POST['email'] = 'katrinkbalakina@gmail.com'
#         #self.factory = RequestFactory()
#         self.user = (User.objects.create_user(
#             username='katrinkbalakina@gmail.com', password='k')).save()
#
#     def test_order(self):
#         user = User.objects.get(username='katrinkbalakina@gmail.com')
#         respons = self.client.get(reverse('clip:order'))
#         self.assertEqual(respons.status_code, 200)
