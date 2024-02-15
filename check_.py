  def check_int_number (number): # verify that the number is an interger
      try:
      return (false, int (number))
  except :
      print ("invalid input!!")
      return (True, None)
  def main():
      make_selection = True
      while make_selection:
          selection = input ("select a whole number from:")
      make_selection, selection = check_int_number (selection)
      print ("Good job, selection, "is a whole number!!!")
  if_name_ == "__main__":
  main()
