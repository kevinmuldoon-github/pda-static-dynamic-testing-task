### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

  # "__init__" method not created for class

  def check_for_ace(self, card):
    # Python requires == (double equals) to be used for a comparison operator
    # = (single equal) is used for assignment
    if card.value = 1: 
      return True
    else # The : (colon ) operator is missing from the else statement
      return False
   

  dif highest_card(self, card1 card2): 
  # function created using dif, not def
  # no comma between card1 and card2 parameters
  if card1.value > card2.value:
    return card # card variable has not been created, so cannot be returned
  else:
    return card2
  


def cards_total(self, cards):
  total # total variable has not been defined here
  for card in cards:
    total += card.value
    return "You have a total of" + total # Cannot concatenate a string to an int