class PersonalAssistant:

    def __init__(self):
        self.contacts = {
            'Jess': {'title': 'PM', 'dob': '20/09/1993'}, 'Hemlata': {'title': 'SSE', 'dob': '25/12/199'},
            'Alpa': {'title': 'TL', 'dob': '20/09/1987'}
        }
        self.todos = []

    def add_todo(self, new_item):
        self.todos.append(new_item)

    def remove_todo(self, todo_item):
        if todo_item in self.todos:
            # Get the todo_item index in list
            index = self.todos.index(todo_item)
            # pop the index for todo_item in todos list
            self.todos.pop(index)
        else:
            print("Todo is not in list!")

    def get_todos(self):
        return self.todos

    def get_birthday(self, name):
        return self.get_contact(name).get("dob") if "dob" in self.get_contact(name) else self.get_contact(name)

    def get_contact(self, name):
        if name in self.contacts:
            return self.contacts[name]
        else:
            return f"No contact with the name! {name}"


# Code to test the class
assistant = PersonalAssistant()
assistant.add_todo("Pick up groceries")
assistant.add_todo("Schedule meeting for next week")
print(assistant.get_todos())
assistant.remove_todo("Pick up groceries")
print(assistant.get_todos())
# Change names to use your own data
print(assistant.get_contact("Hemlata"))
print(assistant.get_birthday("Jess"))
