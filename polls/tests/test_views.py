from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from polls.models import Question, Choice


class PollsTests(TestCase):

    def create_question(self, question_text, days):
        """
        Helper method to create a question with the given `question_text` and
        publish the given number of `days` offset to now
        (negative for past, positive for future).
        """
        time = timezone.now() + timezone.timedelta(days=days)
        return Question.objects.create(question_text=question_text, pub_date=time)

    def create_choice(self, question, choice_text):
        """
        Helper method to create a choice for a question.
        """
        return Choice.objects.create(
            question=question, choice_text=choice_text, votes=0
        )

    def test_index_view(self):
        """Test the index view to ensure it shows the last 5 questions."""
        # Create 6 questions, only 5 should be displayed in the latest list
        for i in range(6):
            self.create_question(f"Question {i}", days=-i)

        response = self.client.get(reverse("polls:index"))

        self.assertEqual(response.status_code, 200)
        self.assertIn("latest_question_list", response.context)
        self.assertEqual(len(response.context["latest_question_list"]), 5)
        self.assertContains(response, "Question 0")

    def test_detail_view(self):
        """Test the detail view for a specific question."""
        question = self.create_question("Test Question", days=-1)

        url = reverse("polls:detail", args=(question.id,))
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn("question", response.context)
        self.assertEqual(response.context["question"], question)
        self.assertContains(response, "Test Question")

    def test_results_view(self):
        """Test the results view for a specific question."""
        question = self.create_question("Test Question", days=-1)

        url = reverse("polls:results", args=(question.id,))
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn("question", response.context)
        self.assertEqual(response.context["question"], question)
        self.assertContains(response, "Test Question")

    def test_vote_view(self):
        """Test voting on a question."""
        question = self.create_question("Test Question", days=-1)
        choice = self.create_choice(question, "Test Choice")

        # Post a vote for the created choice
        response = self.client.post(
            reverse("polls:vote", args=(question.id,)), {"choice": choice.id}
        )

        # After voting, should redirect to results page
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("polls:results", args=(question.id,)))

        # Refresh choice from db to check if vote was incremented
        choice.refresh_from_db()
        self.assertEqual(choice.votes, 1)

    def test_vote_view_invalid_choice(self):
        """Test voting with an invalid choice."""
        question = self.create_question("Test Question", days=-1)

        # Post a vote with an invalid choice id
        response = self.client.post(
            reverse("polls:vote", args=(question.id,)), {"choice": 999}
        )

        # Check if the form is redisplayed with an error message
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You didn&#x27;t select a choice.")
