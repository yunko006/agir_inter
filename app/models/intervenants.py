import mongoengine as me


class Intervenants(me.Document):
    meta = {"collection": "intervenants", "strict": False}
    # mapping from db
    email = me.StringField()
    nom = me.StringField()
    prenom = me.StringField()
    volontaire = me.StringField()
    hesitations = me.StringField()
    contact = me.StringField()
    aider = me.StringField()
    voyager = me.StringField()
    travailler_en_equipe = me.StringField()
    soutenir = me.StringField()
    connaitre_personnes_cultures = me.StringField()
    mettre_a_dispotion = me.StringField()
    responsabilites = me.StringField()
    actif = me.StringField()
    autres_facteurs = me.StringField()
    domaines = me.StringField()
    fonctions = me.StringField()
    competences = me.StringField()
    complements = me.StringField()
    dispo = me.StringField()
    duree = me.StringField()
    deplacements_par_an = me.StringField()
    langue_maternelle = me.StringField()
    notions = me.StringField()
    lu_parle_ecrit = me.StringField()
    autonomes = me.StringField()
    roles = me.StringField()
    exp_inter_oui_non = me.StringField()
    exp_pro = me.StringField()
    exp_benevole = me.StringField()
    structures = me.StringField()
    suggestions = me.StringField()
    connaissances = me.StringField()
    connaissances_structure = me.StringField()
    delegation = me.StringField()
    idees = me.StringField()
    linkedin = me.StringField()
    autres_langues = me.StringField()

    def to_dict(self):
        return {
            "id": str(self.id),
            "nom": self.nom,
            "prenom": self.prenom,
            "email": self.email,
            "volontaire": self.volontaire,
            "hesitations": self.hesitations,
            "contact": self.contact,
            "aider": self.aider,
            "voyager": self.voyager,
            "travailler_en_equipe": self.travailler_en_equipe,
            "soutenir": self.soutenir,
            "connaitre_personnes_cultures": self.connaitre_personnes_cultures,
            "mettre_a_dispotion": self.mettre_a_dispotion,
            "responsabilites": self.responsabilites,
            "actif": self.actif,
            "autres_facteurs": self.autres_facteurs,
            "domaines": self.domaines,
            "fonctions": self.fonctions,
            "competences": self.competences,
            "complements": self.complements,
            "dispo": self.dispo,
            "duree": self.duree,
            "deplacements_par_an": self.deplacements_par_an,
            "langue_maternelle": self.langue_maternelle,
            "notions": self.notions,
            "lu_parle_ecrit": self.lu_parle_ecrit,
            "autonomes": self.autonomes,
            "roles": self.roles,
            "exp_inter_oui_non": self.exp_inter_oui_non,
            "exp_pro": self.exp_pro,
            "exp_benevole": self.exp_benevole,
            "structures": self.structures,
            "suggestions": self.suggestions,
            "connaissances": self.connaissances,
            "connaissances_structure": self.connaissances_structure,
            "delegation": self.delegation,
            "idees": self.idees,
            "linkedin": self.linkedin,
            "autres_langues": self.autres_langues,
        }
