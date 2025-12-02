
import requests
import requests


class SciNovaLogicCore:

    def _init_(self, GOOGLE_API_KEY: str, GOOGLE_CX: str):

        self.GOOGLE_API_KEY = AIzaSyAa884RsgXulHvV66xqbVi4K250Tfe4Q
        self.GOOGLE_CX = 36 d4846c1e2fb47de 

        # --------------------------
        # LOCAL SCIENCE KNOWLEDGE
        # --------------------------
        self.knowledge = {
            "physics": {
                "gravity": "Gravity is a natural force that pulls two masses toward each other. On Earth it causes objects to fall at 9.8 m/s².",
                "newton's first law": "Newton’s First Law: An object stays at rest or in uniform motion unless an external force acts on it.",
                "newton's second law": "Newton’s Second Law: Force = mass × acceleration (F = m × a).",
                "newton's third law": "Newton’s Third Law: Every action has an equal and opposite reaction.",
                "ohm's law": "Ohm’s Law: Voltage = Current × Resistance (V = I × R).",
                "work": "Work = Force × Distance, and measured in Joules.",
                "energy": "Energy is the ability to do work. Total energy is conserved in a closed system."
            },

            "chemistry": {
                "atom": "An atom is the basic unit of matter made of protons, neutrons, and electrons.",
                "chemical reaction": "A chemical reaction is a process where substances (reactants) change into new substances (products).",
                "acid": "Acids release H⁺ ions in water and turn blue litmus red.",
                "base": "Bases release OH⁻ ions in water and turn red litmus blue.",
                "valency": "Valency is the combining capacity of an element, depending on the number of electrons in the outer shell."
            },

            "maths": {
                "pythagoras": "Pythagoras Theorem: a² + b² = c² for right-angled triangles.",
                "derivative": "A derivative measures the rate of change of a function with respect to a variable.",
                "integral": "An integral calculates the area under a curve or the accumulation of quantities.",
                "quadratic formula": "Quadratic Formula: x = (-b ± √(b² - 4ac)) / (2a)."
            }
        }

    # --------------------------
    # NORMALIZER
    # --------------------------
    def normalize(self, text: str):
        text = text.lower().strip()
        text = re.sub(r"[^a-z0-9\s']", " ", text)
        return text

    # --------------------------
    # LOCAL KNOWLEDGE LOOKUP
    # --------------------------
    def local_lookup(self, query: str):
        q = self.normalize(query)

        for domain, topics in self.knowledge.items():
            for concept, explanation in topics.items():
                if concept.replace("'", "") in q:
                    return domain, concept, explanation

        return None

    # --------------------------
    # GOOGLE SEARCH
    # --------------------------
    def google_search(self, query: str):

        url = "https://www.googleapis.com/customsearch/v1"

        params = {
            "key": self.GOOGLE_API_KEY,
            "cx": self.GOOGLE_CX,
            "q": query,
            "num": 3
        }

        try:
            response = requests.get(url, params=params)
            data = response.json()

            if "items" not in data:
                return "No Google results found."

            result_text = ""
            for item in data["items"]:
                title = item.get("title", "No Title")
                snippet = item.get("snippet", "")
                link = item.get("link", "")

                result_text += f"\n• {title}\n  {snippet}\n  {link}\n"

            return result_text

        except Exception as e:
            return f"Google Search Error: {str(e)}"

    # --------------------------
    # MAIN EXPLAIN FUNCTION
    # --------------------------
    def explain(self, question: str):

        result = f"\n=============================\nSciNova Logic Core Response\n=============================\n"
        result += f"Your Question: {question}\n\n"

        # TRY LOCAL KNOWLEDGE
        lookup = self.local_lookup(question)

        if lookup:
            domain, concept, explanation = lookup
            result += f"Domain: {domain.title()}\nConcept: {concept.title()}\n\n"
            result += f"Explanation:\n{explanation}\n"
            result += "\nGoogle Real-World Examples:\n"
            result += self.google_search(concept)
            return result

        # OTHERWISE GO TO GOOGLE
        result += "Local concept not found.\nSearching Google...\n"
        result += self.google_search(question)
        return result


# ----------------------------------------------------
# MAIN PROGRAM LOOP
# ----------------------------------------------------
def main():

    print("=====================================")
    print("        SciNova Logic Core AI        ")
    print("=====================================\n")
    print("Type 'exit' to stop the agent.\n")

    GOOGLE_API_KEY = "AIzaSyAa884RsgXulHvV66xqbVi4K250Tfe4Q"      # ← Replace with your API Key
    GOOGLE_CX = "36d4846c1e2fb47de"             # ← Replace with your CSE ID

    agent = SciNovaLogicCore(AIzaSyAa884RsgXulHvV66xqbVi4K250Tfe4Q)

    while True:
        question = input("Ask SciNova: ")

        if question.lower() == "exit":
            print("\nExiting SciNova Logic Core…")
            break

        print(agent.explain(question))


if _name_ == "_main_":
    main()