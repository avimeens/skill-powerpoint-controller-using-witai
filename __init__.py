from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class PowerpointControllerUsingWitaiSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder().require('PowerpointControllerUsingWitai'))
    def handle_powerpoint_controller_using_witai(self, message):
        self.speak_dialog('powerpoint.controller.using.witai')


def create_skill():
    return PowerpointControllerUsingWitaiSkill()

