# skolens.py

class Skolens:
    id_counter = 1 
    
    def __init__(self, vards, uzvards, sekmes):
        self.name = vards
        self.surname = uzvards
        self.sekmes = sekmes
        self.id = Skolens.id_counter  
        Skolens.id_counter += 1 
    
    def pievienot_jauno_atzime(self, atzīme):
        """Pievieno jaunu atzīmi skolēnam."""
        self.sekmes.append(atzīme)
    
    def videja_atzime(self):
        """Izrēķina un atgriež skolēna vidējo atzīmi."""
        return sum(self.sekmes) / len(self.sekmes) if self.sekmes else 0
    
    def __str__(self):
        """Atgriež skolēna informāciju formātā: ID - Vārds Uzvārds - sekmes"""
        return f"{self.id} - {self.name} {self.surname} - {', '.join(map(str, self.sekmes))}"



# PD03/skola.py

from skolens import Skolens

class Skola:
    def __init__(self, nosaukums):
        self.nosaukums = nosaukums
        self.skoleni = []

    def pievienot_skolenu(self, skolens):
        self.skoleni.append(skolens)

    def paradit_visus_skolenus(self):
        for skolens in self.skoleni:
            print(skolens)

    def labakais(self):
        if not self.skoleni:
            return None
        return max(self.skoleni, key=lambda s: s.videja_atzime())



# PD03/main.py

from skolens import Skolens
from skola import Skola


mana_skola = Skola("Rīgas Vidusskola")


sk1 = Skolens("Anna", "Kalniņa", [9, 8, 10])
sk2 = Skolens("Jānis", "Ozols", [7, 6, 8])
sk3 = Skolens("Līga", "Bērziņa", [10, 10, 9])

mana_skola.pievienot_skolenu(sk1)
mana_skola.pievienot_skolenu(sk2)
mana_skola.pievienot_skolenu(sk3)


print("Visi skolēni:")
mana_skola.paradit_visus_skolenus()


sk1.pievienot_jauno_atzime(10)
print(f"\n{sk1.name} vidējā atzīme: {sk1.videja_atzime():.2f}")


labakais = mana_skola.labakais()
print(f"\nLabākais skolēns: {labakais.name} {labakais.surname} ar vidējo atzīmi {labakais.videja_atzime():.2f}")




