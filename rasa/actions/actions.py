from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# ---- SYMPTOM REPORTING (ENGLISH) ----
class ActionReportSymptom(Action):
    def name(self) -> Text:
        return "action_report_symptom"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        symptom = next(tracker.get_latest_entity_values("symptom"), None)
        duration = next(tracker.get_latest_entity_values("duration"), None)
        activity = next(tracker.get_latest_entity_values("activity"), None)
        emotion = next(tracker.get_latest_entity_values("emotion"), None)
        relation = next(tracker.get_latest_entity_values("relation"), None)
        msg = f"I see you're experiencing {symptom or '[not specified]'}."
        if duration: msg += f" Duration: {duration}."
        if activity: msg += f" Activity: {activity}."
        if emotion: msg += f" Emotion: {emotion}."
        if relation: msg += f" Relation: {relation}."
        dispatcher.utter_message(text=msg)
        return []

class ActionReportSymptomHindi(Action):
    def name(self) -> Text:
        return "action_report_symptom_hindi"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        symptom = next(tracker.get_latest_entity_values("symptom"), None)
        duration = next(tracker.get_latest_entity_values("duration"), None)
        activity = next(tracker.get_latest_entity_values("activity"), None)
        emotion = next(tracker.get_latest_entity_values("emotion"), None)
        relation = next(tracker.get_latest_entity_values("relation"), None)
        msg = f"मैं देख रहा हूँ कि आपको {symptom or '[निर्दिष्ट नहीं]'} हो रहा है।"
        if duration: msg += f" अवधि: {duration}."
        if activity: msg += f" गतिविधि: {activity}."
        if emotion: msg += f" भावना: {emotion}."
        if relation: msg += f" संबंध: {relation}."
        dispatcher.utter_message(text=msg)
        return []

class ActionReportSymptomGujarati(Action):
    def name(self) -> Text:
        return "action_report_symptom_gujarati"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        symptom = next(tracker.get_latest_entity_values("symptom"), None)
        duration = next(tracker.get_latest_entity_values("duration"), None)
        activity = next(tracker.get_latest_entity_values("activity"), None)
        emotion = next(tracker.get_latest_entity_values("emotion"), None)
        relation = next(tracker.get_latest_entity_values("relation"), None)
        msg = f"હું જોઈ રહ્યો છું કે તમને {symptom or '[અજ્ઞાત]'} થઈ રહ્યું છે."
        if duration: msg += f" સમયગાળો: {duration}."
        if activity: msg += f" પ્રવૃત્તિ: {activity}."
        if emotion: msg += f" ભાવના: {emotion}."
        if relation: msg += f" સંબંધ: {relation}."
        dispatcher.utter_message(text=msg)
        return []

class ActionFindClinic(Action):
    def name(self) -> Text:
        return "action_find_clinic"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        fields = ["clinic_type", "location", "clinic_name", "specialty", "when", "service", "opening_time", "closing_time", "phone_number", "parking_details", "amenities_list", "department_hours"]
        labels = {"clinic_type":"Type", "location":"Location", "clinic_name":"Name", "specialty":"Specialty", "when":"When", "service":"Service", "opening_time":"Opens", "closing_time":"Closes", "phone_number":"Phone", "parking_details":"Parking", "amenities_list":"Amenities", "department_hours":"Department hours"}
        parts = [f"{labels[field]}: {value}." for field in fields if (value := next(tracker.get_latest_entity_values(field), None))]
        dispatcher.utter_message(text="Clinic info: " + " ".join(parts) if parts else "Please provide more clinic details.")
        return []

class ActionFindClinicHindi(Action):
    def name(self) -> Text:
        return "action_find_clinic_hindi"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        location = next(tracker.get_latest_entity_values("location"), None)
        clinic_type = next(tracker.get_latest_entity_values("clinic_type"), None)
        dispatcher.utter_message(text=f"क्या आप {location or '[स्थान]'} में {clinic_type or '[क्लिनिक प्रकार]'} क्लिनिक खोज रहे हैं? मैं जांचता हूँ।")
        return []

class ActionFindClinicGujarati(Action):
    def name(self) -> Text:
        return "action_find_clinic_gujarati"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        location = next(tracker.get_latest_entity_values("location"), None)
        clinic_type = next(tracker.get_latest_entity_values("clinic_type"), None)
        dispatcher.utter_message(text=f"શું તમે {location or '[સ્થાન]'} માં {clinic_type or '[ક્લિનિક પ્રકાર]'} ક્લિનિક શોધી રહ્યા છો? હું તપાસું છું.")
        return []

class ActionMedicineInfo(Action):
    def name(self) -> Text:
        return "action_medicine_info"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        medicine = next(tracker.get_latest_entity_values("medicine"), None)
        dispatcher.utter_message(text=f"Medicine information requested for {medicine or '[not specified]'}. Please consult a qualified healthcare professional for medical advice.")
        return []

class ActionMedicineInfoHindi(Action):
    def name(self) -> Text:
        return "action_medicine_info_hindi"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        medicine = next(tracker.get_latest_entity_values("medicine"), None)
        dispatcher.utter_message(text=f"{medicine or '[दवा]'} के बारे में जानकारी मांगी गई है। चिकित्सकीय सलाह के लिए योग्य स्वास्थ्य विशेषज्ञ से परामर्श करें।")
        return []

class ActionMedicineInfoGujarati(Action):
    def name(self) -> Text:
        return "action_medicine_info_gujarati"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        medicine = next(tracker.get_latest_entity_values("medicine"), None)
        dispatcher.utter_message(text=f"{medicine or '[દવા]'} વિશે માહિતી માંગવામાં આવી છે. તબીબી સલાહ માટે યોગ્ય આરોગ્ય નિષ્ણાતની સલાહ લો.")
        return []
