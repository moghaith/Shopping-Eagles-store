from ._anvil_designer import baseTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
import random
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Cart import Cart
from ..home import home
from ..home.ads_component import ads_component
from ..Admin import Admin
class base(baseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.welcome_text()
    self.cart_items = []
    self.stock={'Tshirt':25,'Shirt':20,'Hoodie':30,'Dress':1000,'Kid_shirt':300,'dog_clothes1':10,'dog_clothes2':300,'Cat_costume':250}
    n = random.randint(0,3)
    n2= random.randint(0,3)
    self.drop_down_1.items = [(r['drop'],r) for r in app_tables.dropdown.search() ]
    s=self.drop_down_1.selected_value['drop']
    self.content_panel.add_component(home(n,n2,s))
  #apply stock changes
  def stock_edit(self,quantity,name,boolian):
    if boolian==True:
      self.stock[name]=self.stock[name]+quantity
      alert(self.stock[name])
    z=self.stock[name]
    x=z-quantity
    self.stock[name]=x
    if boolian==False:
      if self.stock[name]<0:
        alert("Item out of stock please contact manager")
        self.stock[name]=z
        return False
      else:
        return True
  def add_to_cart(self, product, Amount):
    #if item is already in cart, just update the Amount
    for i in self.cart_items:
      if i['product'] == product:
        i['Amount'] += Amount
        break
    else:
      self.cart_items.append({'product': product, 'Amount': Amount})
  def homep(self):
    n = random.randint(0,3)
    n2= random.randint(0,3)
    self.drop_down_1.items = [(r['drop'],r) for r in app_tables.dropdown.search() ]
    s=self.drop_down_1.selected_value['drop']
    self.content_panel.clear()
    self.content_panel.add_component(home(n,n2,s))
  #add user name instead of sign in button and add cart after signing in 
  def welcome_text(self):
    user = anvil.users.get_user()
    self.Admin_Page.visible = anvil.users.get_user() != None
    if user: 
      email = user["email"]
      Admincon = user['Admin']
      self.sign_in.text = email
      # Admin button doesn't appear except when the user is an assigned admin
      if int(Admincon) == True: 
        self.Admin_Page.visible = anvil.users.get_user() != None
    else:
      self.sign_in.text = "Sign In"
    self.personal_cart()
  #hide cart when signed out
  def personal_cart(self):
    self.Cart.visible = anvil.users.get_user() != None
  #Cart button 
  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Cart(items=self.cart_items))
  #Home button
  def Home_page_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    n = random.randint(0,3)
    n2= random.randint(0,3)
    s=self.drop_down_1.selected_value['drop']
    self.content_panel.add_component(home(n,n2,s))
    pass
  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    user = anvil.users.get_user()
    if user:
      logout = confirm("Do you want to logout?")
      if logout:
        anvil.users.logout()
        self.homep()
    else:
      anvil.users.login_with_form()
    self.welcome_text()
  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    self.content_panel.clear()
    n = random.randint(0,3)
    n2= random.randint(0,3)
    s=self.drop_down_1.selected_value['drop']
    self.content_panel.add_component(home(n,n2,s))
    pass
  def Admin_Page_hide(self, **event_args):
    """This method is called when the Link is removed from the screen"""
    if (anvil.users.get_user())["Admin"]== False:
      self.Admin_Page.visible == True
    else:
      self.Admin_Page.visible == False
  def Admin_Page_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Admin())


    








