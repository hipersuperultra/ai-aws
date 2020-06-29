#   Code a SalesPerson class with the following attributes
#   - first_name (string), the first name of the salesperson
#   - last_name (string), the last name of the salesperson
#   - employee_id (int), the employee ID number like 5681923
#   - salary (float), the monthly salary of the employee
#   - pants_sold (list of Pants objects),
#            pants that the salesperson has sold
#   - total_sales (float), sum of sales of pants sold
class SalesPerson:

###    Input Args for the __init__ function:
#        first_name (str)
#        last_name (str)
#        employee_id (int)
#        salary (float)
#
# You can initialize pants_sold as an empty list
# You can initialize total_sales to zero.
#
###
    def __init__(self, first_name, last_name, employee_id, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = []
        self.total_sales = 0

#
#    This method receives a Pants object and appends
#    the object to the pants_sold attribute list
#
#    Args:
#        pants (Pants object): a pants object
#    Returns:
#        None
    def sell_pants(self, pant):
        self.pants_sold.append(pant)

#
#    This method has no input or outputs. When this method
#    is called, the code iterates through the pants_sold list
#    and prints out the characteristics of each pair of pants
#    line by line. The print out should look something like this
#
#   color: blue, waist_size: 34, length: 34, price: 10
#   color: red, waist_size: 36, length: 30, price: 14.15
#
#
#
###
    def display_sales(self):
        for pant in self.pants_sold:
            print(f'color: {pant.color}, waist_size: {pant.waist_size}, length: {pant.length}, price: {pant.price}')

#      This method calculates the total sales for the sales person.
#      The method should iterate through the pants_sold attribute list
#      and sum the prices of the pants sold. The sum should be stored
#      in the total_sales attribute and then return the total.
#
#      Args:
#        None
#      Returns:
#        float: total sales
#
###
    def calculate_sales(self):
        self.total_sales = sum(p.price for p in self.pants_sold)
        return self.total_sales

#
#   The salesperson receives a commission based on the total
#   sales of pants. The method receives a percentage, and then
#   calculate the total sales of pants based on the price,
#   and then returns the commission as (percentage * total sales)
#
#    Args:
#        percentage (float): comission percentage as a decimal
#
#    Returns:
#        float: total commission
#
#
###
    def calculate_commission(self, percentage):
        return self.calculate_sales() * percentage
