from django.test import TestCase
from tasks.models import Task, Tag


class ModelsTest(TestCase):
    def test_tag(self):
        tag = Tag.objects.create(name="test")
        self.assertEqual(str(tag), tag.name)

    def test_task(self):
        task = Task.objects.create(content="test")
        self.assertEqual(str(task), task.content)

    def test_task_tag(self):
        task = Task.objects.create(content="test")
        tag = Tag.objects.create(name="test")
        task.tags.add(tag)
        self.assertEqual(task.tags.count(), 1)
        self.assertIn(tag, task.tags.all())
