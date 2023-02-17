from mycroft import MycroftSkill, intent_file_handler


class Knowledge(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('knowledge.intent')
    def handle_knowledge(self, message):
        self.speak_dialog('knowledge')


def create_skill():
    return Knowledge()

