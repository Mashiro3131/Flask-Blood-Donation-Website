"""
    Fichier : gestion_genres_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class FormWTFAjouterGenres(FlaskForm):
    """
        Dans le formulaire "genres_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    # nom_prenom_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_prenom_regexp = ""
    nom_prenom_wtf = StringField("Prénom ", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                                                   Regexp(nom_prenom_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])

    submit = SubmitField("Enregistrer")


class FormWTFUpdateGenre(FlaskForm):
    """
        Dans le formulaire "genre_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_prenom_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_prenom_update_wtf = StringField("Prénom ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                          Regexp(nom_prenom_update_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])
    nom_nom_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_nom_update_wtf = StringField("Nom", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                 Regexp(nom_nom_update_regexp,
                                                        message="Pas de chiffres, de caractères "
                                                                "spéciaux, "
                                                                "d'espace à double, de double "
                                                                "apostrophe, de double trait union")
                                                 ])
    nom_adresse_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_adresse_update_wtf = StringField("Adresse", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                 Regexp(nom_adresse_update_regexp,
                                                        message="Pas de chiffres, de caractères "
                                                                "spéciaux, "
                                                                "d'espace à double, de double "
                                                                "apostrophe, de double trait union")
                                                 ])
    nom_mail_update_regexp = "([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+]+$"
    nom_mail_update_wtf = StringField("Mail", validators=[Length(min=2, max=50, message="min 2 max 20"),
                                                 Regexp(nom_mail_update_regexp,
                                                        message="Pas de chiffres, de caractères "
                                                                "spéciaux, "
                                                                "d'espace à double, de double "
                                                                "apostrophe, de double trait union")
                                                 ])
    nom_num_tel_update_regexp = "/(\b(0041|0)|\B\+41)(\s?\(0\))?(\s)?[1-9]{2}(\s)?[0-9]{3}(\s)?[0-9]{2}(\s)?[0-9]{2}\b/"
    nom_num_tel_update_wtf = StringField("Numero de telephone (a changer pour etre compatible avec chiffre dans gestion_genres_wtf_forms.py", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                 Regexp(nom_num_tel_update_regexp,
                                                        message="Pas de chiffres, de caractères "
                                                                "spéciaux, "
                                                                "d'espace à double, de double "
                                                                "apostrophe, de double trait union")
                                                 ])
    nom_date_naissance_update_regexp = "([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    nom_date_naissance_update_wtf = StringField("Date de naissance", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                 Regexp(nom_date_naissance_update_regexp,
                                                        message="Pas de chiffres, de caractères "
                                                                "spéciaux, "
                                                                "d'espace à double, de double "
                                                                "apostrophe, de double trait union")
                                                 ])
    nom_groupe_sanguin_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_groupe_sanguin_update_wtf = StringField("Groupe sanguin", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                 Regexp(nom_groupe_sanguin_update_regexp,
                                                        message="Pas de chiffres, de caractères "
                                                                "spéciaux, "
                                                                "d'espace à double, de double "
                                                                "apostrophe, de double trait union")
                                                 ])

    submit = SubmitField("Update genre")



class FormWTFDeleteGenre(FlaskForm):

    nom_prenom_delete_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_prenom_delete_wtf = StringField("Prénom ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                          Regexp(nom_prenom_delete_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])
    nom_nom_delete_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_nom_delete_wtf = StringField("Nom", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                 Regexp(nom_nom_delete_regexp,
                                                        message="Pas de chiffres, de caractères "
                                                                "spéciaux, "
                                                                "d'espace à double, de double "
                                                                "apostrophe, de double trait union")
                                                 ])
    nom_adresse_delete_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_adresse_delete_wtf = StringField("Adresse", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                 Regexp(nom_adresse_delete_regexp,
                                                        message="Pas de chiffres, de caractères "
                                                                "spéciaux, "
                                                                "d'espace à double, de double "
                                                                "apostrophe, de double trait union")
                                                 ])
    nom_mail_delete_regexp = "([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    nom_mail_delete_wtf = StringField("Mail", validators=[Length(min=2, max=50, message="min 2 max 20"),
                                                 Regexp(nom_mail_delete_regexp,
                                                        message="Pas de chiffres, de caractères "
                                                                "spéciaux, "
                                                                "d'espace à double, de double "
                                                                "apostrophe, de double trait union")
                                                 ])
    nom_num_tel_delete_regexp = "/(\b(0041|0)|\B\+41)(\s?\(0\))?(\s)?[1-9]{2}(\s)?[0-9]{3}(\s)?[0-9]{2}(\s)?[0-9]{2}\b/"
    nom_num_tel_delete_wtf = StringField("Numero de telephone (a changer pour etre compatible avec chiffre dans gestion_genres_wtf_forms.py", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                 Regexp(nom_num_tel_delete_regexp,
                                                        message="Pas de chiffres, de caractères "
                                                                "spéciaux, "
                                                                "d'espace à double, de double "
                                                                "apostrophe, de double trait union")
                                                 ])
    nom_date_naissance_delete_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_date_naissance_delete_wtf = StringField("Date de naissance", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                 Regexp(nom_date_naissance_delete_regexp,
                                                        message="Pas de chiffres, de caractères "
                                                                "spéciaux, "
                                                                "d'espace à double, de double "
                                                                "apostrophe, de double trait union")
                                                 ])
    nom_groupe_sanguin_delete_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_groupe_sanguin_delete_wtf = StringField("Groupe sanguin", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                 Regexp(nom_groupe_sanguin_delete_regexp,
                                                        message="Pas de chiffres, de caractères "
                                                                "spéciaux, "
                                                                "d'espace à double, de double "
                                                                "apostrophe, de double trait union")
                                                 ])

    submit = SubmitField
    """
        Dans le formulaire "genre_delete_wtf.html"

        nom_genre_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_genre".
    """
    nom_genre_delete_wtf = StringField("Effacer ce genre")
    submit_btn_del = SubmitField("Effacer genre")
    submit_btn_conf_del = SubmitField("Etes-vous sûr d'effacer ????")
    submit_btn_annuler = SubmitField("Annuler!!")
