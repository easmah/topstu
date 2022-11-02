import unittest
from Testing.survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):

    def test_store_single_response(self):
        question = "What language did you first learn to speak?: "
        my_survey = AnonymousSurvey(question)
        my_survey.store_response("English")
        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        question = "What first 3 languages did you learn?: "
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Java', 'Python']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == '___main___':
    unittest.main()
