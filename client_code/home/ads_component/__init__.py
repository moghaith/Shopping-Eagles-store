from ._anvil_designer import ads_componentTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
class ads_component(ads_componentTemplate):
  def __init__(self,adscontent,adscontent2, **properties):
    # Set Form properties and Data Bindings that relate to the ads and their presentation.
    self.init_components(**properties)
    self.ad_photo.source= adscontent
    self.ad_photo2.source= adscontent2
  