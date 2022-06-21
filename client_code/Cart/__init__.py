from ._anvil_designer import CartTemplate
from anvil import *
import stripe.checkout
#import stripe
import anvil.stripe
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import stripe.checkout
user = anvil.users.get_user()
class Cart(CartTemplate):
  def __init__(self,items, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.order = []
    self.items = items
    self.repeating_panel_1.items = self.items
    self.subtotal = sum(item['product']['price'] * item['Amount'] for item in self.items)
    self.subtotal_label.text = f"EGP {self.subtotal:.02f}"
    if self.subtotal >= 1500: #free shipping for orders over $35
      self.shipping_label.text = 'FREE'     
    else: #add $5 shipping
      if self.subtotal==0:
        self.shipping_label.text = "EGP 0.00"
      else:
        self.shipping_label.text = "EGP 60.00"
        self.subtotal = self.subtotal + 60
      
    self.total_label.text = f"EGP{self.subtotal:.02f}"
    # Any code you write here will run when the form opens.

  def checkout_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    token, info = stripe.checkout.get_token(amount=self.subtotal*100, currency="EGP", title='Go for it', description='These are your final steps.')
    try:
      alert("Success")
    except Exception as e:
      alert(str(e))
    
    
    
#     for i in self.items:
#       self.order.append({'name':i['product']['name'], 'Amount':i['Amount']})
#     try:
#       charge = stripe.checkout.charge(amount=self.subtotal*100,
#                                       currency="EGP",
#                                       shipping_address=True,
#                                       title="نسور الكود",
#                                       icon_url="_/theme/cupcake_logo.png")
#     except:
#       return
    
#     anvil.server.call('add_order', charge['charge_id'], self.order)

#     get_open_form().cart_items = []
#     get_open_form().cart_link_click()
#     Notification("Your order has been received!").show()

