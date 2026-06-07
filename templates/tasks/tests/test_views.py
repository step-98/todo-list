from django.test import TestCase
from django.urls import reverse

from tasks.models import Task, Tag


TAG_URL = reverse("tasks:tag-list")
TASK_URL = reverse("tasks:task-list")


class TagTest(TestCase):
    def test_retrieve_tag(self):
        Tag.objects.create(name="test")
        response = self.client.get(TAG_URL)
        tags = Tag.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["tag_list"]), list(tags))
        self.assertTemplateUsed(response, "tasks/tag_list.html")


class TaskTest(TestCase):
    def test_retrieve_task(self):
        task = Task.objects.create(
            content="Test",
            deadline="2026-06-21",
        )
        task.tags.add(Tag.objects.create(name="test"))
        response = self.client.get(TASK_URL)
        self.assertEqual(response.status_code, 200)
        tasks = Task.objects.all()
        self.assertEqual(list(response.context["task_list"]), list(tasks))
        self.assertTemplateUsed(response, "tasks/task_list.html")

    def test_toggle_task(self):
        task = Task.objects.create(
            content="Test",
            deadline="2026-06-21",
            is_done=False
        )
        url = reverse("tasks:toggle-task", args=[task.id])
        self.client.post(url)
        task.refresh_from_db()
        self.assertTrue(task.is_done)

        self.client.post(url)
        task.refresh_from_db()
        self.assertFalse(task.is_done)
