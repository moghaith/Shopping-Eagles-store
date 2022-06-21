from ._anvil_designer import FormmTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from ...Form1 import Form1
from anvil.tables import app_tables
from .. import Cart
from ...base import base
class Formm(FormmTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
#     self.load_cart_items()
    self.label_1.text = self.item['product']['description']
    self.image_1.source= self.item['product']['image']
    self.label_2.text=self.item['product']['price']
    self.label_3.text=self.item['Amount']
#     get_open_form().stock_edit(self.item['Amount'],self.item['product']['name'])
#     if x==True:
#       self.update_form()
#   def update_form(self):
#     # Any code you write here will run when the form opens.
#     items=anvil.server.call('get_items_cart').search()
#     panel= GridPanel()
#     for i,item in enumerate(items):
#       z=Form1(desc=item['description'],cost=(f"${item['price']}"),icart=item['image'])
# #       self.image_cart.source=item['image']
#       panel.add_component(z,width_xs=12)
#       self.clear()
#       self.add_component(panel)
#     pass
#   def load_cart_items(self):
#     items = anvil.server.call("get_items").search()
#     items_panel= GridPanel()
#     for i,item in enumerate(items):
# #       print(item['Item'])
#       c = product(name=item['name'], price=f"${item['price']}" ,button_text="Add to Cart",imagecontent=item['image'])
#       items_panel.add_component(c,row=str(i//2),width_xs=6)
#     self.add_component(items_panel)
#     # Any code you write here will run when the form opens.
#   def drop_down_3_change(self, **event_args):
#     """This method is called when an item is selected"""
#     pass
#   def repeating_panel_1_hide(self, **event_args):
#     """This method is called when the RepeatingPanel is removed from the screen"""
#     pass
#   def delete_button_click(self, **event_args):
#     """This method is called when the button is clicked"""
#     get_open_form().cart_items.remove(self.item)
#     get_open_form().link_2_click()
  def delete_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().cart_items.remove(self.item)
    get_open_form().stock_edit(self.item['Amount'],self.item['product']['name'],True)
    get_open_form().link_2_click()
    


