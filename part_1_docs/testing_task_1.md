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

#A column (:) is missing after the else statement
#the equality check should be == instead of =
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False

  #dif is mispelled so the method highest_card is not actually created - it should have been "def"
  #indentention for the function body is wrong
  #There's a comma (,) missing after card1 before card2 arguments
  #return statement for card1 is mising the number, it should be card1
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2


#the function is indented outside the class definition
#total variable wasn't properly defined
#Return statement is indentend inside the wrong block, it should be indented into the function block
#The return statement need to be inside the f''
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total

```
