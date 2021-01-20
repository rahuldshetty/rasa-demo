# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted

from actions.backend import *

class ActionListOptions(Action):

    def name(self) -> Text:
        return "action_list_options"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        res = fetch_actions()

        dispatcher.utter_message(text=res['text'], buttons=res['list'])

        return [UserUtteranceReverted()]


class ActionRandomNumber(Action):
    
    def name(self) -> Text:
        return "action_random_number"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        number = fetch_random_number()

        dispatcher.utter_message(text="Your random number is {}".format(number))

        return [UserUtteranceReverted()]



class ActionArticleResult(Action):
    
    def name(self) -> Text:
        return "action_article_result"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        articles = fetch_article(tracker.get_slot("article")) 

        dispatcher.utter_message(text="There are some of the aricles:")
        dispatcher.utter_custom_json(json_message={"articles": articles})

        return [UserUtteranceReverted()]