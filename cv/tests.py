from django.test import TestCase

from django.utils import timezone

from .models import WorkExp

# Create your tests here.

class CvPageTest(TestCase):

    def saveOneWorkExp(self):
        response = self.client.post("/cv/workexp/new/", data={
            'startTime':'2020-02-02',
            'endTime':'2020-05-02',
            'company':'google',
            'desc':'test work',
        })
        return response

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/cv_view.html')

    def test_new_page_returns_correct_html(self):
        response = self.client.get('/cv/workexp/new/')
        self.assertTemplateUsed(response, 'cv/work_exp_edit.html')

    def test_can_save_a_Post_request(self):
        self.saveOneWorkExp()
        self.assertEqual(WorkExp.objects.count(), 1)
        new_item = WorkExp.objects.first()
        self.assertEqual(new_item.company, "google")
        self.assertEqual(new_item.desc, "test work")

    def test_redirects_after_POST(self):
        response = self.saveOneWorkExp()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv')

    def test_edit_page_returns_correct_html(self):
        self.saveOneWorkExp()
        response = self.client.get('/cv/workexp/1/edit/')
        self.assertTemplateUsed(response, 'cv/work_exp_edit.html')




class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = WorkExp()
        first_item.startTime = '2020-02-20'
        # first_item.endTime = timezone.now
        first_item.company = 'google'
        first_item.desc = 'My first job.'
        first_item.save()

        saved_items = WorkExp.objects.all()
        self.assertEqual(saved_items.count(), 1)

        first_saved_item = saved_items[0]
        self.assertEqual(first_saved_item.desc, 'My first job.')