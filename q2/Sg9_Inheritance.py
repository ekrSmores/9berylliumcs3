class Publication:

  def __init__(self, title: str, author: str): #Initiaized the funtions
    self.__title = title
    self.__author = author

  def get_title(self): #Gets title
    return self.__title

  def get_author(self): #gets author
    return self.__author

  def set_title(self, title: str): #Sets  title
    self.__title = title

  def set_author(self, author: str):# Sets author
    self.__author = author

  def Display_info(self):
    return f"Author: {self.__author} \nTitle: {self.__title}" #Gets both title and author

#BookClASS
class Book(Publication):

  def __init__(self, title: str, author: str, number_of_pages: int):
    super().__init__(title, author) #access parent methods and attributes
    self.__number_of_pages = number_of_pages #New unique attribute

  def get_number_of_pages(self): #gets
    return self.__number_of_pages

  def set_number_of_pages(self, number_of_pages: int): #sets
    if number_of_pages < 0:
      raise ValueError("Number of Pages Can NOT be negative.") # Raises an error if it does not follow the condition
    self.__number_of_pages = number_of_pages

  def Display_info(self): 
    return (
        f"{super().Display_info()} \nPages: {self.__number_of_pages}" #gets info from parent and attribute from self
    )

#MagazinecLASS
class Magazine(Publication):

  def __init__(self, title: str, author: str, issue_number: int):
    super().__init__(title, author) #access parent methods and attributes
    self.__issue_number = issue_number #New unique attribute


  def get_issue_number(self): #gets
    return self.__issue_number

  def set_issue_number(self, issue_number: int): #sets
    if issue_number < 0:
      raise ValueError("Issue Number Can NOT be negative.") # Raises an error if it does not follow the condition
    self.__issue_number = issue_number

  def Display_info(self):
    return (
        f"{super().Display_info()} \nIssue Number: {self.__issue_number}" #gets info from parent and attribute from self
    )


# Testing the code
publication = Publication("Maze Runner", "James Dashner")
book = Book("Maze Runner", "James Dashner", 6767)
magazine = Magazine("The New Yorker", "Aura Men", 167)

print("Publication")
print(publication.Display_info())
print("____________________________")

print("Book")
book.set_number_of_pages(350)  # Valid update
print(book.Display_info())
print("____________________________")

print("Magazine")
print(magazine.Display_info())
