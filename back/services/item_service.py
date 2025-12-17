from models.item_model import Item

# class ItemService:
#     @staticmethod
#     def get_all_items():
#         return Item.query.all()

#     @staticmethod
#     def get_item_by_id(item_id):
#         return Item.query.get(item_id)

#     @staticmethod
#     def create_item(data):
#         new_item = Item(name=data['name'], description=data.get('description', ''))
#         return new_item

#     @staticmethod
#     def update_item(item_id, data):
#         item = Item.query.get(item_id)
#         if not item:
#             return None
#         item.name = data.get('name', item.name)
#         item.description = data.get('description', item.description)
#         return item

#     @staticmethod
#     def delete_item(item_id):
#         item = Item.query.get(item_id)
#         if not item:
#             return None
#         return item

class ItemService:
    @staticmethod
    def get_all_items():
        return Item.query.all()

    @staticmethod
    def get_item_by_id(item_id):
        return Item.query.get(item_id)

    @staticmethod
    def create_item(data):
        new_item = Item(
            name=data['name'],
            description=data.get('description', ''),
            price=data['price'],
            stock=data['stock']
        )
        return new_item

    @staticmethod
    def update_item(item_id, data):
        item = Item.query.get(item_id)
        if not item:
            return None
        item.name = data.get('name', item.name)
        item.description = data.get('description', item.description)
        item.price = data.get('price', item.price)
        item.stock = data.get('stock', item.stock)
        return item

    @staticmethod
    def delete_item(item_id):
        item = Item.query.get(item_id)
        if not item:
            return None
        return item