class PersonalAssistant:

  def __init__(self):
    self.contacts = {
        'Jess': 'PM', 'Hemlata': 'SSE', 'Alpa': 'TL'
    }
    self.todos = []


  def get_contact(self, name):
    if name in self.contacts:
        return self.contacts[name]
    else:
        return "No contact with that name!"


# Code to test the class
assistant = PersonalAssistant()
print(assistant.get_contact("Hemlata"))
