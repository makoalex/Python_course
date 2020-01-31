import unittest
from Activity_TDD import healthy, train


class TestActivity(unittest.TestCase):

    def test_health(self):
        self.assertEqual(
            healthy('broccoli', is_healthy=True),
            "I'm eating broccoli because my body is a temple "
        )

    def test_unhealth(self):
        self.assertEqual(
            healthy('KFC', is_healthy=False),
            "I'm eating KFC because YOLO"
        )

    def test_fail_health(self):
        with self.assertRaises(ValueError):
            healthy('pizza', is_healthy='no time for that')

    def test_train_hard(self):
        self.assertEqual(
            train(5),
            "i feel  good after 5 days of training"
        )
    def test_train_weak(self):
        self.assertEqual(
            train(1),
            '1 time a week  is not enough training for a healthy body'
        )
    if __name__ == '__main__':
        unittest.main()
