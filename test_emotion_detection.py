import unittest
from  EmotionDetection.emotion_detection import emotion_detector

class testEmotions(unittest.TestCase):

    def test_joy(self):
        test = emotion_detector("I am glad this happened")
        self.assertEqual(test["dominant_emotion"], 'joy')

    def test_anger(self):
        test = emotion_detector("I am really mad about this")
        self.assertEqual(test["dominant_emotion"], 'anger')

    def test_disgust(self):
        test = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(test["dominant_emotion"], 'disgust')

    def test_sadness(self):
        test = emotion_detector("I am so sad about this")
        self.assertEqual(test['dominant_emotion'], 'sadness')

    def test_fear(self):
        test = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(test['dominant_emotion'], 'fear')
    
if __name__ == "__main__":
    unittest.main()