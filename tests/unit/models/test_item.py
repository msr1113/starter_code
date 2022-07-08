from unittest import TestCase

from models.item import ItemModel


class ItemTest(TestCase):
    def test_create_item(self):
        item = ItemModel('test',19.99)

        self.assertEqual(item.name,'tst',
                         "the name of the item after creation does not equal the constructor ")
        self.assertEqual(item.price,19.99,
                         "the price of the item after creation does not equal the constructor ")

    def test_item_json(self):
        item = ItemModel('test',19.99)
        expected = {
            'name':'test',
            'price':19.99
        }
        self.assertEqual(item.json(),expected,
                         "the json export of item is incorrect. received {},expected {}".format(item.json(),
                                                                                                expected))

