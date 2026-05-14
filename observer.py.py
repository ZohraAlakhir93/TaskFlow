#  Utilisateur (Observer) 
class Utilisateur:
    def __init__(self, id, nom, email):
        self.id = id
        self.nom = nom
        self.email = email

    def update(self, message):
        print(f"[{self.nom}] reçoit notification: {message}")


#  Tache (Subject) 
class Tache:
    def __init__(self):
        self.observers = []
        self.status = ""

    def attach(self, o):
        self.observers.append(o)

    def notify(self):
        for obs in self.observers:
            obs.update(self.status)

    def setStatus(self, status):
        print("Changement de statut:", status)
        self.status = status
        self.notify()


# TEST 
u1 = Utilisateur("1", "Ali", "ali@mail.com")
u2 = Utilisateur("2", "Sara", "sara@mail.com")

tache = Tache()
tache.attach(u1)
tache.attach(u2)

tache.setStatus("En cours")
tache.setStatus("Terminée")# ===== Utilisateur (Observer) =====
class Utilisateur:
    def __init__(self, id, nom, email):
        self.id = id
        self.nom = nom
        self.email = email

    def update(self, message):
        print(f"[{self.nom}] reçoit notification: {message}")


#  Tache (Subject) 
class Tache:
    def __init__(self):
        self.observers = []
        self.status = ""

    def attach(self, o):
        self.observers.append(o)

    def notify(self):
        for obs in self.observers:
            obs.update(self.status)

    def setStatus(self, status):
        print("Changement de statut:", status)
        self.status = status
        self.notify()


# A TEST 
u1 = Utilisateur(1, "Ali", "ali@mail.com")
u2 = Utilisateur(2, "Sara", "sara@mail.com")

tache = Tache()
tache.attach(u1)
tache.attach(u2)

tache.setStatus("En cours")
tache.setStatus("Terminée")
