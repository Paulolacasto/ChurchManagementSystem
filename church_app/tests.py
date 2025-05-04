from django.test import TestCase
from .models import Member, FirstTimer

class MemberModelTest(TestCase):
    def setUp(self):
        self.member = Member.objects.create(
            first_name="John",
            last_name="Doe",
            age=30,
            gender="Man",
            phone="1234567890",
            address="123 Church Street",
        )

    def test_member_str(self):
        self.assertEqual(str(self.member), "John Doe")

    def test_member_age_positive(self):
        self.assertTrue(self.member.age > 0)

class FirstTimerModelTest(TestCase):
    def setUp(self):
        self.first_timer = FirstTimer.objects.create(
            first_name="Jane",
            last_name="Smith",
            phone="0987654321",
            invited_by="Pastor Mike",
            born_again=True,
            service_feedback="Loved the sermon!",
            would_like_visit=True,
            available_for_fellowship=False,
        )

    def test_first_timer_str(self):
        self.assertEqual(str(self.first_timer), "Jane Smith")

    def test_first_timer_born_again_boolean(self):
        self.assertIsInstance(self.first_timer.born_again, bool)
