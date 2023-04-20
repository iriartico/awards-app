import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question


# Models and views
class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_questions(self):
        """was_published_recently returns False for questions whose pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="¿Quién es el mejor Course Director de mi academia?", pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)


def create_question(question, days):
    """Create a question with the given "question_text", and published the given numbers of the day
       offset to now(negative for questions published in the past, positive for questions that have
       yet to be published)"""
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question, pub_date=time)


class QuestionIndexViewTests(TestCase):

    def test_no_questions(self):
        """If not question exist, an appropiate message is displayed"""
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_no_future_question_are_displayed(self):
        """If a future question is created in the database, this question isn't show until his pub_date
           is equal to the present time"""
        response = self.client.get(reverse("polls:index"))
        future_question = create_question("Who is the best student?", 30)
        self.assertNotIn(future_question, response.context["latest_question_list"])
    
    def test_past_question(self):
        """Question with a pub_date in the past are displayed on the index page"""
        past_question = create_question("Past question", -10)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [past_question])

    def test_future_question_and_past_question(self):
        """Even if both past and future question exists only past question are displayed"""
        past_question = create_question("Past question", -30)
        future_question = create_question("Future question", 30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [past_question])
        self.assertNotIn(future_question, response.context["latest_question_list"])

    def test_two_past_question(self):
        """The question index page may display multiple questions """
        past_question_1 = create_question("Past question", -30)
        past_question_2 = create_question("Past question", -40)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [past_question_1, past_question_2])

    def test_two_future_question(self):
        """The question index page should not display any questions """
        future_question_1 = create_question("Future question 1", 30)
        future_question_2 = create_question("Future question 2", 40)
        response = self.client.get(reverse("polls:index"))
        self.assertNotIn([future_question_1, future_question_2], response.context["latest_question_list"])
