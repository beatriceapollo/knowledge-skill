from mycroft import MycroftSkill, intent_file_handler
from nltk.tokenize import word_tokenize


class Knowledge(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('knowledge.intent')
    def handle_knowledge(self, message):
        self.speak_dialog('knowledge')

#    def converse(self, utterances, lang):
 #       if utterances:
  #          text = utterances[0]
   #         tokenized_text = word_tokenize(text)
    #        tagged_text = nltk.pos_tag(tokenized_text)
     #       self.speak(tagged_text)
     #       return True
     #   else:
     #       return False

def create_skill():
    return Knowledge()

