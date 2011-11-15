"""Test cases for Objectapp's admin"""
from django.test import TestCase
from django.contrib.auth.models import User

from objectapp import settings
from objectapp.models import GBObject
from objectapp.models import Objecttype


class GBObjectAdminTestCase(TestCase):
    """Test case for GBObject Admin"""
    urls = 'objectapp.tests.urls'

    def setUp(self):
        self.original_wysiwyg = settings.WYSIWYG
        settings.WYSIWYG = None
        User.objects.create_superuser('admin', 'admin@example.com', 'password')
        objecttype_1 = Objecttype.objects.create(title='Objecttype 1', slug='cat-1')
        Objecttype.objects.create(title='Objecttype 2', slug='cat-2',
                                parent=objecttype_1)

        self.client.login(username='admin', password='password')

    def tearDown(self):
        settings.WYSIWYG = self.original_wysiwyg

    def test_gbobject_add_and_change(self):
        """Test the insertion of an GBObject"""
        self.assertEquals(GBObject.objects.count(), 0)
        post_data = {'title': u'New gbobject',
                     'template': u'objectapp/gbobject_detail.html',
                     'creation_date_0': u'2011-01-01',
                     'creation_date_1': u'12:00:00',
                     'start_publication_0': u'2011-01-01',
                     'start_publication_1': u'12:00:00',
                     'end_publication_0': u'2042-03-15',
                     'end_publication_1': u'00:00:00',
                     'status': u'2',
                     'sites': u'1',
                     'content': u'My content'}

        response = self.client.post('/admin/objectapp/gbobject/add/', post_data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(GBObject.objects.count(), 0)

        post_data.update({'slug': u'new-gbobject'})
        response = self.client.post('/admin/objectapp/gbobject/add/',
                                    post_data, follow=True)
        self.assertEquals(response.redirect_chain,
                          [('http://testserver/admin/objectapp/gbobject/', 302)])
        self.assertEquals(GBObject.objects.count(), 1)


class ObjecttypeAdminTestCase(TestCase):
    """Test cases for Objecttype Admin"""
    urls = 'objectapp.tests.urls'

    def setUp(self):
        User.objects.create_superuser('admin', 'admin@example.com', 'password')
        self.client.login(username='admin', password='password')

    def test_objecttype_add_and_change(self):
        """Test the insertion of a Objecttype, change error, and new insert"""
        self.assertEquals(Objecttype.objects.count(), 0)
        post_data = {'title': u'New objecttype',
                     'slug': u'new-objecttype'}
        response = self.client.post('/admin/objectapp/objecttype/add/',
                                    post_data, follow=True)
        self.assertEquals(response.redirect_chain,
                          [('http://testserver/admin/objectapp/objecttype/', 302)])
        self.assertEquals(Objecttype.objects.count(), 1)

        post_data.update({'parent': u'1'})
        response = self.client.post('/admin/objectapp/objecttype/1/', post_data)
        self.assertEquals(response.status_code, 200)

        response = self.client.post('/admin/objectapp/objecttype/add/', post_data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(Objecttype.objects.count(), 1)

        post_data.update({'slug': u'new-objecttype-2'})
        response = self.client.post('/admin/objectapp/objecttype/add/',
                                    post_data, follow=True)
        self.assertEquals(response.redirect_chain,
                          [('http://testserver/admin/objectapp/objecttype/', 302)])
        self.assertEquals(Objecttype.objects.count(), 2)
