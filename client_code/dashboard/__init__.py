from ._anvil_designer import dashboardTemplate
from anvil import *
import anvil.server

class dashboard(dashboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('dashboard.hospital_booking_form_1')

  def primary_color_1_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('dashboard.oxy_wheels_booking_form_1')

  def primary_color_1_copy_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('dashboard.gym_booking_form_1')
