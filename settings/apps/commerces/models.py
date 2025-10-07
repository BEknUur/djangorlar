#Python modules 
from django.db.models import (
    Model, 
    CharField, 
    TextField,
    DateTimeField, 
    BooleanField, 
    ForeignKey, 
    ManyToManyField,
    IntegerField,
    CASCADE
)

from apps.catalogs.models import MenuItem, Option

class User(Model):
    """
    Model representing a user.
    Fields:
    - name: The name of the user.
    """

    name = CharField(max_length=100)

class Address(Model):
    """
    Model representing a user's address.
    Fields:
    - user: ForeignKey linking to the User model.
    """

    user_id = ForeignKey(User, on_delete=CASCADE, related_name='addresses')
    address = TextField()


class Order(Model):
    """
    Model representing an order.
    Fields:
    - user: ForeignKey linking to the User model.
    - address: ForeignKey linking to the Address model.
    - order_date: The date and time of the order.
    """
    STATUS_CHOICES = (
        (0, "pending"),
        (1, "confirmed"),
        (2, "delivered"),
        (3, "done"), 
        (4, "canceled")

    )
    user_id = ForeignKey(User, on_delete=CASCADE, related_name='orders')
    address_id = ForeignKey(Address, on_delete=CASCADE, related_name='orders')
    order_date = DateTimeField(auto_now_add=True)

    total_price = CharField(max_length=100)
    status = IntegerField(choices=STATUS_CHOICES, default=0)


class OrderItem(Model):
    """
    Model representing an item in an order.
    Fields:
    - order: ForeignKey linking to the Order model.
    - menu_item: ForeignKey linking to the MenuItem model.
    - quantity: The quantity of the menu item in the order.
    """
    order_id = ForeignKey(Order, on_delete=CASCADE, related_name='order_items')
    menu_item_id = ForeignKey(MenuItem, on_delete=CASCADE, related_name='order_items')      
    
    quantity = IntegerField()
    price = CharField(max_length=100)

class OrderItemOption(Model):
    """
    Model representing an option for an item in an order.
    Fields:
    - order_item: ForeignKey linking to the OrderItem model.
    - option: ForeignKey linking to the Option model.
    """
    order_item_id = ForeignKey(OrderItem, on_delete=CASCADE, related_name='order_item_options')
    option_id = ForeignKey(Option, on_delete=CASCADE, related_name='order_item_options')
    is_default = BooleanField(default=False)
    price = CharField(max_length=100)   


