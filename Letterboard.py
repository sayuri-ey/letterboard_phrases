'''
Code to verify the possibility of writing phrases with available characters set in a letterboard.
It asks the user for a phrase (input) and it checks whether it is possible to write the phrase, 
or if there are insufficient characters in the set to write the determined phrase
or if the user is using invalid charaters, which do not exist in the characters set.
'''

while True:
  #Listing all the characters available on the letterboard set. Should be edit accordlingly to the letters available in the user's letter set 
  letter_set=("aabbccddeeffgghhijjkkllmmnnooppqqrssttuuvvwwxxyyz122334455667788990*!?%$/=-÷+@#&") 
  available_ch=list(letter_set)
  phrase=(input("Type your phrase: ")).lower()
  ch_needed=list(phrase)

  if phrase == "":
    print("Bye :) Come back when you need to check another phrase")
    break

  i=[]
  ok=1
  #Checking for invalid characters (Characters not available in the letter set)
  for i in ch_needed:
    if i not in available_ch: 
      ok=0
      print("Error: Invalid character (%s) used in \"" %i, phrase,"\"",sep="")
    
  #Checking if the character is available for use
  ok=1
  for i in ch_needed:  
    if i not in available_ch:
      ok=0
      print("Unavailable character (%s)" %i)
    #Removing used characters from the set
    else:
      available_ch.remove(i)

  if ok:
      print("It is possible to write \"", phrase,"\" in your letterboard :)",sep="")