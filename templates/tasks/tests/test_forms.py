from django.test import TestCase

from tasks.forms import TaskForm
from tasks.models import Tag


class TaskFormTest(TestCase):
    def test_task_form_is_valid(self):
        tag = Tag.objects.create(name="tag")
        form = TaskForm(data={
            "content": "Test",
            "tag": tag
        })
        self.assertTrue(form.is_valid())
