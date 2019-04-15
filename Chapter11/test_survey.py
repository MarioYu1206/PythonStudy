import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['python','c++','c','java']
        my_survey.store_response(responses)
        self.assertIn(responses,my_survey.responses)




    def setUp(self):
        """创建一个调查对象和一组答案，供使用的测试方法使用"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['python','c++','c','java']

    def test_store_single_response2(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_all_response2(self):
        self.my_survey.store_response(self.responses)
        self.assertIn(self.responses,self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()
