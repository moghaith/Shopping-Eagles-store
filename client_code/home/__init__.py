from ._anvil_designer import homeTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .store_items import store_items
from .ads_component import ads_component

class home(homeTemplate):
  def __init__(self,n,n2,s, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    random=1
    self.ads_generator(n,n2)
    self.load_items(s)
#     self.ads_generator()
    # Any code you write here will run when the form opens.
#     self.load_items()
#     self.content.add_component(name="Tshirt")
  def load_items(self,s):
    c=0
    items = anvil.server.call("get_items").search()
    if s=='All':
      for i in items:
        c+=1
        self.flow_panel_1.add_component(store_items(item=i),row=str(c//2),width='30%')
    else:
      for i in items:
        c+=1
        if s == i["Type"]:
          self.flow_panel_1.add_component(store_items(item=i), row=str(c//2),width='30%')
    if s=='all':
      for i, item in enumerate(items):
        c = store_items(name=item['name'], price=f"${item['price']}" ,button_text="Add to Cart",imagecontent=item['image'])
        items_panel.add_component(c,row=str(i//2),width_xs=6)
  #     self.clear()
      self.add_component(items_panel)
    elif s=='medium':
      for i,item in enumerate(items):
  #       print(item['Item'])
        if s == item['Sizes']:
          c = store_items(name=item['name'], price=f"${item['price']}" ,button_text="Add to Cart",imagecontent=item['image'])
          items_panel.add_component(c,row=str(i//2),width_xs=6)
  #     self.clear()
      self.add_component(items_panel)
  def ads_generator(self,random,random2):
    pictures = anvil.server.call("get_ads").search()
    ads_panel= GridPanel()
#     for picture in pictures:
#       print(item['Item'])
    if random==random2 and random2==0:
      random2=2
    elif random==random2:
      random2=random2-1
    x = ads_component(adscontent=pictures[random]['ad'], adscontent2=pictures[random2]['ad'])
#     z = ads_component()
    self.flow_panel_2.add_component(x,row=0,width='100%')
#     global s
#     s=self.drop_down_1.selected_value['drop']
#     self.refresh_data_bindings()
#     self.clear()
#     self.load_items(s)
    #this function generates ads andomly on the shopping page 


