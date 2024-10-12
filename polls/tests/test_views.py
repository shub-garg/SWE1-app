import pytest
from django.urls import reverse
from django.utils import timezone
from polls.models import Question, Choice


@pytest.fixture
def create_question(db):
    """Fixture to create a question."""
    def make_question(question_text, days):
        """
        Create a question with the given `question_text` and publish the
        given number of `days` offset to now (negative for questions published
        in the past, positive for questions that have yet to be published).
        """
        time = timezone.now() + timezone.timedelta(days=days)
        return Question.objects.create(question_text=question_text, pub_date=time)
    return make_question


@pytest.fixture
def create_choice(db):
    """Fixture to create a choice."""
    def make_choice(question, choice_text):
        return Choice.objects.create(question=question, choice_text=choice_text, votes=0)
    return make_choice


@pytest.mark.django_db
def test_index_view(client, create_question):
    """Test the index view to ensure it shows the last 5 questions."""
    # Create 6 questions, only 5 should be displayed in the latest list
    for i in range(6):
        create_question(f"Question {i}", days=-i)

    response = client.get(reverse('polls:index'))
    
    assert response.status_code == 200
    assert 'latest_question_list' in response.context
    assert len(response.context['latest_question_list']) == 5
    assert b"Question 0" in response.content


@pytest.mark.django_db
def test_detail_view(client, create_question):
    """Test the detail view for a specific question."""
    question = create_question("Test Question", days=-1)

    url = reverse('polls:detail', args=(question.id,))
    response = client.get(url)

    assert response.status_code == 200
    assert 'question' in response.context
    assert response.context['question'] == question
    assert b"Test Question" in response.content


@pytest.mark.django_db
def test_results_view(client, create_question):
    """Test the results view for a specific question."""
    question = create_question("Test Question", days=-1)

    url = reverse('polls:results', args=(question.id,))
    response = client.get(url)

    assert response.status_code == 200
    assert 'question' in response.context
    assert response.context['question'] == question
    assert b"Test Question" in response.content


@pytest.mark.django_db
def test_vote_view(client, create_question, create_choice):
    """Test voting on a question."""
    question = create_question("Test Question", days=-1)
    choice = create_choice(question, "Test Choice")

    # Post a vote for the created choice
    response = client.post(reverse('polls:vote', args=(question.id,)), {'choice': choice.id})

    # After voting, should redirect to results page
    assert response.status_code == 302
    assert response.url == reverse('polls:results', args=(question.id,))

    # Refresh choice from db to check if vote was incremented
    choice.refresh_from_db()
    assert choice.votes == 1


@pytest.mark.django_db
def test_vote_view_invalid_choice(client, create_question):
    """Test voting with an invalid choice."""
    question = create_question("Test Question", days=-1)

    # Post a vote with an invalid choice id
    response = client.post(reverse('polls:vote', args=(question.id,)), {'choice': 999})

    # Print response content to inspect it
    print(response.content)

    assert response.status_code == 200  # Should redisplay the form
    # Adjust the assertion to match the HTML-encoded error message
    assert b"You didn&#x27;t select a choice." in response.content
