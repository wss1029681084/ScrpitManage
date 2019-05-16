from django.test import TestCase
from .utils import gethostname
from demo import models
# Create your tests here
#
from demo.models import Server


class QuestionModelTests(TestCase):
    def test1(self):
        print(Server.objects.all()[1])
        print(models.Publish.objects.all())
        self.assertIs(models.Publish.objects.all().values("Publish_name"),False)





