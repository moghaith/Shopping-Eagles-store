from ._anvil_designer import AdminTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
c=0
class Admin(AdminTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties) 
  def button_1_click(self, **event_args):
    #This method is called when the button is clicked it checks that all the fields are filled and appends the database
    if self.name.text=="":
      self.name.text=""
      self.Id.text=""
      self.price.text=""
      self.description.text=""
      self.stock.text=""
      c=1
    elif self.Id.text=="":
      self.name.text=""
      self.Id.text=""
      self.price.text=""
      self.description.text=""
      self.stock.text=""
      c=1
    elif self.price.text=="":
      self.name.text=""
      self.Id.text=""
      self.price.text=""
      self.description.text=""
      self.stock.text=""
      c=1
    elif self.description.text=="":
      self.name.text=""
      self.Id.text=""
      self.price.text=""
      self.description.text=""
      self.stock.text=""
      c=1
      return 
    elif self.stock.text=="":
      self.name.text=""
      self.Id.text=""
      self.price.text=""
      self.description.text=""
      self.stock.text=""
      c=1
         #This is validation for the entries added to the databse
    else:
      c=0
    if c==0:
      alert("Please upload an image of your new product to the database")
      row = app_tables.store_items.add_row(name=self.name.text,price=(self.price.text),
            id_name=self.Id_Name.text, stock=self.stock.text,Type=self.Type_drop.selected_value,
                                          description=self.description.text)
      return
    else:
      alert("Please fill all the fields")
      return
    


