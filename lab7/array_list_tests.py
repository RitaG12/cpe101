import unittest
from array_list import *

class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.
    def test_interface(self):
        pass
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)

    def test_init(self):
        arr = empty_list()
        l = List(arr, 0, 10)
        self.assertEqual(l, List(arr, 0, 10))

    def test_eq1(self): #if statemtn 1
        templist = empty_list()
        ans = List([None]*10, 0, 10)
        self.assertTrue(templist.__eq__(ans))

    def test_eq2(self):  # for loop false
        l = empty_list()
        l1 = add(l, 0, 1)
        ans = empty_list()
        an = add(ans, 0, 2)
        self.assertFalse(l1.__eq__(an))

    def test_eq3(self):  # for loop false
        l = empty_list()
        l1 = add(l, 0, 1)
        ans = empty_list()
        self.assertFalse(l1.__eq__(ans))


    def test_repr1(self):
        l = empty_list()
        ans = "List = %r, size=%r, capacity=%r"%([None, None, None, None, None, None, None, None, None, None],0, 10)
        self.assertEqual(repr(l), ans)

    def test_empty(self):
        l = empty_list()
        ans = List([None]*10, 0, 10)
        self.assertEqual(l, ans)

    def test_add1(self):
        l = empty_list()
        ans = List([1, None, None, None, None, None, None, None, None, None], 1, 10)
        #print(add(l,0,1))
        self.assertEqual(add(l, 0, 1), ans)
    def test_add2(self):
        l = empty_list()
        with self.assertRaises(IndexError):
            add(l, -1,3)
    def test_add3(self):
        l = empty_list()
        with self.assertRaises(IndexError):
            add(l, 2, 3)
    def test_add4(self):

        l = empty_list()
        l1=add(l, 0, 1)
        #rint(l1)
        #print("TEST 4")
        #print()
        l2 = add(l1, 1, 2)
        #print(l2)
        ans = List([1, 2, None, None, None, None, None, None, None, None], 2, 10)
        self.assertEqual(l2, ans)
    def test_add5(self):
        l = empty_list()
        l1=add(l, 0, 1)
        #print(l1)
        #print("TEST 4")
        #print()
        l2 = add(l1, 1, 2)
        #print(l2)
        l3 = add(l2, 2,3)
        #print(l3)
        ans = List([1, 2, 3, None, None, None, None, None, None, None], 3, 10)
        self.assertEqual(l3, ans)
    def test_add6(self):
        l = empty_list()
        l1=add(l, 0, 1)
        #print(l1)
        #print("TEST 4")
        #print()
        l2 = add(l1, 1, 2)
        l3 = add(l2, 2,3)
        #print(l3)
        l4 = add(l3, 0, 100)
        #print(l4)
        ans = List([100, 1, 2, 3, None, None, None, None, None, None], 4, 10)
        self.assertEqual(l4, ans)
    def test_add7(self):
        l = empty_list()
        l1=add(l, 0, 1)
        l2 = add(l1, 1, 2)
        #print(l2)
        l3 = add(l2, 2,3)
        l4 = add(l3, 3, 4)
        l5 = add(l4, 4, 5)
        l6 = add(l5, 5, 6)
        l7 = add(l6, 6, 7)
        l8 = add(l7, 7, 8)
        l9 = add(l8, 8, 9)
        l10 = add(l9, 9, 10)
       #print(l10)
        ans = List([1, 2, 3, 4,5,6,7,8,9,10], 10, 10)
        self.assertEqual(l10, ans)
    def test_add8(self):
        l = empty_list()
        l1=add(l, 0, 1)
        l2 = add(l1, 1, 2)
        #print(l2)
        l3 = add(l2, 2,3)
        l4 = add(l3, 3, 4)
        l5 = add(l4, 4, 5)
        l6 = add(l5, 5, 6)
        l7 = add(l6, 6, 7)
        l8 = add(l7, 7, 8)
        l9 = add(l8, 8, 9)
        l10 = add(l9, 9, 10) #size = 10
        l11 = add(l10, 10, 11) #should be testing line 33
        #print("ll1")
        #print(l11)
        ans = List([1, 2, 3, 4,5,6,7,8,9,10,11, None, None, None, None, None, None, None, None, None], 11, 20)
        self.assertEqual(l11, ans)
    def test_length1(self):
        l = empty_list()
        self.assertEqual(length(l), 0)
    def test_length2(self):
        l = empty_list()
        l1 = add(l, 0, 1)
        self.assertEqual(length(l1), 1)
    def test_length3(self):
        l = empty_list()
        l1 = add(l, 0, 1)
        l2 = add(l1, 1, 2)
        # print(l2)
        l3 = add(l2, 2, 3)
        l4 = add(l3, 3, 4)
        l5 = add(l4, 4, 5)
        l6 = add(l5, 5, 6)
        l7 = add(l6, 6, 7)
        l8 = add(l7, 7, 8)
        l9 = add(l8, 8, 9)
        l10 = add(l9, 9, 10)
        l11 = add(l10, 10, 11)
        self.assertEqual(length(l11), 11)

    def test_get1(self):
        l = empty_list()
        l1 = add(l, 0, 1)
        self.assertEqual(get(l1, 0),1)
    def test_get2(self):
        l = empty_list()
        l1 = add(l, 0, 1)
        l2 = add(l1, 1, 2)
        l3 = add(l2, 2, 3)
        self.assertEqual(get(l3, 2), 3)
    def test_get3(self):
        l = empty_list()
        with self.assertRaises(IndexError):
            get(l,0)
    def test_get4(self):
        l = empty_list()
        l1 = add(l, 0, 1)
        l2 = add(l1, 1, 2)
        l3 = add(l2, 2, 3)
        l4 = add(l3, 3, 4)
        with self.assertRaises(IndexError):
            get(l,5)
    def test_get5(self):
        l = empty_list()
        l1 = add(l, 0, 1)
        l2 = add(l1, 1, 2)
        with self.assertRaises(IndexError):
            get(l,-1)

    def test_set1(self):
        l = empty_list()
        with self.assertRaises(IndexError):
            set(l,0,100)
    def test_set2(self):
        l = empty_list()
        l1 = add(l, 0, 1)
        l2 = add(l1, 1, 2)
        l3 = add(l2, 2, 3)
        l4 = add(l3, 3, 4)
        with self.assertRaises(IndexError):
            set(l,5,100)
    def test_set3(self):
        l = empty_list()
        l1 = add(l, 0, 1)
        l2 = add(l1, 1, 2)
        with self.assertRaises(IndexError):
            set(l,-1,100)
    def test_set4(self):
        l = empty_list()
        l1 = add(l, 0, 1)
        #print("L1")
        #print(l1)
        ans = List([100, None, None, None, None, None, None, None, None, None],1,10)
        #print("ANS")
        #print(ans)
        self.assertEqual(set(l1, 0,100),ans )
    def test_set5(self):
        l = empty_list()
        l1=add(l, 0, 1)
        l2 = add(l1, 1, 2)
        l3 = add(l2, 2,3)
        ans = List([1, 100, 3, None, None, None, None, None, None, None], 3, 10)
        self.assertEqual(set(l3, 1, 100),ans)

    def test_remove1(self):
        l = empty_list()
        with self.assertRaises(IndexError):
            remove(l, 0)
    def test_remove2(self):
        l = empty_list()
        l1 = add(l, 0, 1)
        l2 = add(l1, 1, 2)
        l3 = add(l2, 2, 3)
        l4 = add(l3, 3, 4)
        with self.assertRaises(IndexError):
            remove(l, 5)
    def test_remove3(self):
        l = empty_list()
        l1 = add(l, 0, 1)
        l2 = add(l1, 1, 2)
        with self.assertRaises(IndexError):
            remove(l, -1)
    def test_remove4(self):
        l = empty_list()
        l1 = add(l, 0, 1)
        ans = (1,List([None, None, None, None, None, None, None, None, None, None],0,10))
        self.assertEqual(remove(l1, 0),ans )

    def test_remove5(self):
        l = empty_list()
        l1=add(l, 0, 1)
        l2 = add(l1, 1, 2)
        l3 = add(l2, 2, 3)
        ans = (2, List([1, 3, None, None, None, None, None, None, None, None], 2, 10))
        self.assertEqual(remove(l3, 1),ans)


if __name__ == '__main__':
    unittest.main()
