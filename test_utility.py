import unittest
import utility

# python3 -m unittest -v <.py>


class TestProcess(unittest.TestCase):

    def test_replace_string(self):
        data_list = []
        target = []
        replace = []
        want = []

        # 1.
        data_list.append(["1.txt", "2.txt", "3.txt", "4.txt", "5.txt"])
        target.append("txt")
        replace.append("jpg")
        want.append(["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"])
        # 2.
        data_list.append(["Hello World"])
        target.append("World")
        replace.append("Good Morning")
        want.append(["Hello Good Morning"])

        for i in range(len(data_list)):
            result = utility.replace_string(
                data_list[i], target[i], replace[i])
            self.assertEqual(want[i], result)

    def test_remove_string(self):
        data_list = []
        target = []
        want = []

        # 1.
        data_list.append(["1.txt", "2.txt", "3.txt", "4.txt", "5.txt"])
        target.append("txt")
        want.append([])
        # 2.
        data_list.append(["1.txt", "2.txt", "3.txt", "4.txt", "5.txt"])
        target.append("2")
        want.append(["1.txt", "3.txt", "4.txt", "5.txt"])

        for i in range(len(data_list)):
            result = utility.remove_string(
                data_list[i], target[i])
            self.assertEqual(want[i], result)

    def test_keep_string(self):
        data_list = []
        target = []
        want = []

        # 1.
        data_list.append(["1.txt", "2.txt", "3.txt", "4.txt", "5.txt"])
        target.append("txt")
        want.append(["1.txt", "2.txt", "3.txt", "4.txt", "5.txt"])
        # 2.
        data_list.append(["1.txt", "2.txt", "3.txt", "4.txt", "5.txt"])
        target.append("2")
        want.append(["2.txt"])

        for i in range(len(data_list)):
            result = utility.keep_string(
                data_list[i], target[i])
            self.assertEqual(want[i], result)


if __name__ == '__main__':
    unittest.main()
