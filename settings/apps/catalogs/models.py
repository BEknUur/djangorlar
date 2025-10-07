#Python modules 
from django.db.models import (
    Model, 
    CharField, 
    TextField,
    DateTimeField, 
    BooleanField, 
    ForeignKey, 
    ManyToManyField,
    CASCADE
)

class Restaurant(Model):
    """
    Model representing a restaurant.
    Fields:
    - name: The name of the restaurant.
    - description: A brief description of the restaurant.
    """
    name = CharField(max_length=255)
    description = TextField()


class MenuItem(Model):
    """
    Model representing a menu item in a restaurant.
    Fields:
    - restaurant: ForeignKey linking to the Restaurant model.
    - name: The name of the menu item.
    - price: The price of the menu item.
    - availability: Boolean indicating if the item is available.
    """
    restaurant_id = ForeignKey(Restaurant, on_delete=CASCADE, related_name='menu_items')
    name = CharField(max_length=255)
    price = CharField(max_length=100)
    availability = BooleanField(default=True)


class Category(Model):
    """
    Model representing a category for menu items.
    Fields:
    - name: The name of the category.
    """
    menu_items = ManyToManyField(MenuItem, related_name='categories')

class MenuItemCategory(Model):
    """
    Model representing a category for menu items.
    Fields:
    - name: The name of the category.
    """
    menu_item_id = ForeignKey(MenuItem, on_delete=CASCADE, related_name='menu_item_categories')
    category_id = ForeignKey(Category, on_delete=CASCADE, related_name='category_menu_items')

class Option(Model):
    """
    Model representing an option for menu items.
    Fields:
    - name: The name of the option.
    """
    menu_item_id = ForeignKey(MenuItem, on_delete=CASCADE, related_name='options')
    name = CharField(max_length=255)

class ItemOption(Model):
    """"
    Model representing an option for menu items.
    Fields:
    - menu_item_id: ForeignKey linking to the MenuItem model.
    - option_id: ForeignKey linking to the Option model.
    - is_default: Boolean indicating if the option is the default choice.
    
    """
    menu_item_id = ManyToManyField(to=MenuItem, related_name='item_options')
    option_id = ManyToManyField(to=Option, blank=True, related_name="item_options")
    is_default = BooleanField(default=False)

