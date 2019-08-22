# Create a class Shopping cart with the methods, add_item, remove_item and checkout 
# then create a class Shop that inherits from shooping cart and overrides the ,ethod remove_item

class ShoppingCart(object):
  quantity = 0
  # initiliaze
  def __init__(self):
    self.total = 0
    self.items = {}
    
  def add_item(self, item_name, quantity, price):
    self.items[item_name] = quantity
    self.total = self.total + price * quantity
  
  def remove_item(self, item_name, quantity, price):
    if self.items[item_name] <= quantity:
      self.total = self.total - price * self.items[item_name]
      del self.items[item_name]
      return self.total
    
    else:
      left_quantity = self.items[item_name] - quantity
      self.items[item_name] = left_quantity
      self.total = self.total - price * quantity
      
      return self.total
  
  def checkout(self, cash_paid):
    if cash_paid >= self.total:
      balance = cash_paid - self.total
      return balance
    
    else:
      err_msg = "Cash paid not enough" 
      return err_msg
    
  
class Shop(ShoppingCart):
  def __init__(self, quantity=100):
    self.quantity = quantity
    
  def remove_item(self):
    self.quantity -= 1
  
  