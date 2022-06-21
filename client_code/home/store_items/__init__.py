from ._anvil_designer import store_itemsTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...Form1 import Form1
from ...Cart import Cart
class store_items(store_itemsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.item_description.text = self.item['name']
    self.iprice.text = self.item['price']
    self.photo.source= self.item['image']
  def add_cart_click(self, **event_args):
    """This method is called when the button is clicked"""
    save_clicked = alert(content=Form1(item=self.item),
                         large=True)

