import string
import random
from datetime import date

print("Test")


def get_case_nr():
  the_number=random.randint(10121, 89999)
  letters = string.ascii_uppercase
  the_letter = ''.join(random.choice(letters) for i in range(1))
  today = date.today()
  the_day = today.strftime("%d%m%y-")
  case_nr = str(the_day) + str(the_letter) + str(the_number)
  print("case_nr:", case_nr)
  
get_case_nr()