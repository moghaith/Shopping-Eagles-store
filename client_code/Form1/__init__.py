from ._anvil_designer import Form1Template
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.
    self.description_label.text= self.item['description']
    self.price_label.text= self.item['price']
    self.image_cart.source=self.item['image']
    pass
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    Flag=get_open_form().stock_edit(self.Amount_box.text,self.item['name'],False)
    if Flag == True:
      if self.Amount_box.text:
        get_open_form().add_to_cart(self.item, self.Amount_box.text)
  #       x=app_tables.store_items.get(stock=self.item['stock'])
  #       x=x-int(self.Amount_box.text)
  #       app_tables.store_items(stock=x)
        self.Amount_box.text = ""
        self.button_1.visible = False
        self.button_2.visible = True
        self.timer.interval = 1
      else:
        self.Amount_box.text = ""
        alert("Please specify an amount over 0").show()
  def timer_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    self.button_1.visible = True
    self.button_2.visible = False
    self.timer.interval = 0
