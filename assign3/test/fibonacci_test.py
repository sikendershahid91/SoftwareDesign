class fibonacciTest(object):
    def test_negative_position_throws_exception(self):
        self.assertRaises(ValueError, self.fibonacci, -1)

    def test_position_0_return_1(self):
        self.assertEqual(1, self.fibonacci(0))

    def test_position_1_return_1(self):
        self.assertEqual(1, self.fibonacci(1))

    def test_position_2_return_2(self):
        self.assertEqual(2, self.fibonacci(2))

    def test_position_4_return_5(self):
        self.assertEqual(5, self.fibonacci(4))

    def test_position_3_return_3(self):
        self.assertEqual(3, self.fibonacci(3))

    def test_position_5_return_8(self):
        self.assertEqual(8, self.fibonacci(5))

    def test_position_6_return_13(self):
        self.assertEqual(13, self.fibonacci(6))
