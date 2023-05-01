from mongoengine import DynamicDocument
import mongoengine as me


class Resultats(DynamicDocument):
    meta = {"strict": False}
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