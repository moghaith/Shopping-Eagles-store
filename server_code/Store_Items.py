import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


@anvil.server.callable
def get_items_cart():
  return app_tables.store_items.client_readable()
@anvil.server.callable
def get_items():
  return app_tables.store_items.client_readable()
@anvil.server.callable
def get_ads():
  return app_tables.ads.client_readable()
def ping():
  return "pong"