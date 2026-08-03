"""
A small, deterministic, rule-based FAQ bot for the Accutech site.

No LLM/API key is used: incoming text is normalised and matched against a
set of keyword-triggered intents, ordered by specificity. This keeps the
bot fast, free to run, and easy to extend by editing INTENTS below.
"""
import re

from core.content import BRANDS, COMPANY, SOLUTIONS

GREETINGS = ("hi", "hello", "hey", "salam", "good morning", "good afternoon", "good evening")

QUICK_REPLIES_DEFAULT = [
    "Our solutions",
    "Calibration lab",
    "Brands we represent",
    "Contact details",
]


def _solution_by_keywords():
    """Build a keyword -> solution lookup from the shared content module."""
    lookup = []
    keyword_map = {
        "pressure": ["pressure", "gauge", "transmitter", "psi"],
        "temperature": ["temperature", "thermocouple", "rtd", "thermometer"],
        "force-level": ["force", "level", "load cell", "tank", "hopper"],
        "flow": ["flow", "flowmeter", "flow meter"],
        "calibration": ["calibration", "calibrate", "iso 17025", "accredited", "lab"],
        "sf6-gas": ["sf6", "gas", "switchgear"],
    }
    for solution in SOLUTIONS:
        keywords = keyword_map.get(solution["slug"], [solution["title"].lower()])
        lookup.append((solution, keywords))
    return lookup


SOLUTION_LOOKUP = _solution_by_keywords()


def _normalise(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return re.sub(r"\s+", " ", text)


def _contains_any(text: str, keywords) -> bool:
    words = set(text.split())
    for kw in keywords:
        if " " in kw:
            if kw in text:
                return True
        elif kw in words:
            return True
    return False


def get_reply(message: str) -> dict:
    """
    Return {"reply": str, "quick_replies": list[str]} for a user message.
    """
    text = _normalise(message)

    if not text:
        return {
            "reply": "Ask me about our solutions, calibration services, "
                      "brand partnerships, or how to reach the Accutech team.",
            "quick_replies": QUICK_REPLIES_DEFAULT,
        }

    if _contains_any(text, GREETINGS):
        return {
            "reply": f"Hello! I'm the {COMPANY['name']} assistant. I can help with "
                      "product solutions, calibration services, our brand "
                      "partners, or contact details. What do you need?",
            "quick_replies": QUICK_REPLIES_DEFAULT,
        }

    if _contains_any(text, ["thank", "thanks", "cheers"]):
        return {
            "reply": "You're welcome! Anything else about our instrumentation "
                      "or calibration services I can help with?",
            "quick_replies": QUICK_REPLIES_DEFAULT,
        }

    if _contains_any(text, ["bye", "goodbye", "see you"]):
        return {
            "reply": "Thanks for stopping by Accutech — reach out any time "
                      f"at {COMPANY['email']}.",
            "quick_replies": [],
        }

    # Specific solution matches
    for solution, keywords in SOLUTION_LOOKUP:
        if _contains_any(text, keywords):
            return {
                "reply": f"{solution['title']}: {solution['summary']} "
                         f"{solution['detail']}",
                "quick_replies": ["See all solutions", "Talk to an engineer", "Contact us"],
            }

    if _contains_any(text, ["solution", "product", "instrument", "measure", "measurement"]):
        titles = ", ".join(s["title"] for s in SOLUTIONS)
        return {
            "reply": f"We cover: {titles}. Ask me about any one of these for more detail.",
            "quick_replies": [s["title"] for s in SOLUTIONS[:4]],
        }

    if _contains_any(text, ["brand", "abb", "wika", "trafag", "partner", "represent"]):
        lines = "; ".join(f"{b['name']} ({b['role']})" for b in BRANDS)
        return {
            "reply": f"We represent {lines}. We're the only Trafag partner "
                     "in the Middle East and an approved ABB Value Provider.",
            "quick_replies": ["Contact us", "Our solutions"],
        }

    if _contains_any(text, ["iso", "accredit", "certified", "certificate", "quality"]):
        return {
            "reply": "Our calibration lab is ISO/IEC 17025:2005 (DAC) accredited "
                      "and ISO 9001:2015 (BAS) certified, and is approved by WIKA.",
            "quick_replies": ["Calibration services", "Contact us"],
        }

    if _contains_any(text, ["about", "history", "founded", "company", "who are you"]):
        return {
            "reply": f"{COMPANY['legal_name']} launched in the UAE in 1996 as "
                      "pressure and temperature specialists, and has grown "
                      "into a multi-divisional instrumentation and "
                      "calibration provider across the Middle East.",
            "quick_replies": ["Our solutions", "Brands we represent"],
        }

    if _contains_any(text, ["contact", "phone", "email", "address", "location", "located",
                             "reach", "call", "where"]):
        return {
            "reply": f"You can reach Accutech at {COMPANY['phone']} or "
                      f"{COMPANY['email']}. We're based at {COMPANY['address']}.",
            "quick_replies": ["Open contact form"],
        }

    if _contains_any(text, ["job", "career", "vacancy", "hiring"]):
        return {
            "reply": "For career opportunities, please send your CV to "
                      f"{COMPANY['email']} and our team will follow up.",
            "quick_replies": ["Contact us"],
        }

    return {
        "reply": "I'm not sure about that one yet — I can help with our "
                  "solutions, calibration services, brand partners, or "
                  "contact details. You can also reach our team directly "
                  f"at {COMPANY['email']}.",
        "quick_replies": QUICK_REPLIES_DEFAULT,
    }
