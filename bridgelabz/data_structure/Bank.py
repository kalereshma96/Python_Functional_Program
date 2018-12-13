"""
purpose   :creates Banking Cash Counter where people come in to
           deposit Cash and withdraw Cash. Have an input panel to
           add people to Queue to either deposit or withdraw money
           and dequeue the people.

@Author   : Reshma Y. Kale

"""
from com.bridgelabz.utility.Data_structure_utility import *

q = Queue()
balance = 1000
q.bankCounter()
q.deposit()
q.withdraw()
q.current_balance(balance)
q.persons_in_queue()