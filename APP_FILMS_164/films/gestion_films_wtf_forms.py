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


class FormWTFAjouterReceveur(FlaskForm):
    """
        Dans le formulaire "genres_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    # nom_prenom_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_prenom_receveur_add_regexp = ""
    nom_prenom_receveur_add_wtf = StringField("Prénom", validators=[Length(min=0, max=50, message="min 0 max 50"),
                                                                   Regexp(nom_prenom_receveur_add_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    # nom_nom_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_nom_receveur_add_regexp = ""
    nom_nom_receveur_add_wtf = StringField("Nom", validators=[Length(min=0, max=50, message="min 0 max 50"),
                                                                   Regexp(nom_nom_receveur_add_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    # nom_adresse_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ0-9]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ0-9-]+$"
    nom_adresse_receveur_add_regexp = ""
    nom_adresse_receveur_add_wtf = StringField("Adresse ", validators=[Length(min=0, max=50, message="min 0 max 50"),
                                                 Regexp(nom_adresse_receveur_add_regexp,
                                                        message="Veuillez inserer une adresse valide. EX:"
                                                                "1110 Morges"
                                                                "LE NPA puis le lieu"
                                                        )
                                                 ])
    # nom_mail_regexp = "([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    nom_mail_receveur_add_regexp = ""
    nom_mail_receveur_add_wtf = StringField("Mail", validators=[Length(min=0, max=50, message="min 0 max 50"),
                                                 Regexp(nom_mail_receveur_add_regexp,
                                                        message="Pas de chiffres, de caractères "
                                                                "spéciaux, "
                                                                "d'espace à double, de double "
                                                                "apostrophe, de double trait union")
                                                 ])
    # nom_num_tel_regexp = "/^\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$/"
    # nom_num_tel_regexp = "^[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}$"
    nom_num_tel_receveur_add_regexp = ""
    nom_num_tel_receveur_add_wtf = StringField("Numéro de Téléphone", validators=[Length(min=0, max=13, message="min 2 max 30"),
                                                 Regexp(nom_num_tel_receveur_add_regexp,
                                                        message="Pas de numéro de telephone dépassant 30 caractères "
                                                                "pas de lettres"
                                                                )
                                                 ])


    nom_date_naissance_receveur_add_wtf = DateField("Date de Naissance", validators=[InputRequired("Date obligatoire"),
                                                                        DataRequired("Date non valide")


                                                                        ])



    nom_groupe_sanguin_receveur_add_regexp = ""
    nom_groupe_sanguin_receveur_add_wtf = StringField("Groupe Sanguin", validators=[Length(min=0, max=50, message="min 0 max 50"),
                                                                   Regexp(nom_groupe_sanguin_receveur_add_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])

    submit = SubmitField("Enregistrer")


class FormWTFUpdateFilm(FlaskForm):
    """
        Dans le formulaire "film_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """

    nom_prenom_receveur_update_regexp = ""
    nom_prenom_receveur_update_wtf = StringField("Prénom", validators=[Length(min=0, max=50, message="min 0 max 50"),
                                                                       Regexp(nom_prenom_receveur_update_regexp,
                                                                              message="Pas de chiffres, de caractères "
                                                                                      "spéciaux, "
                                                                                      "d'espace à double, de double "
                                                                                      "apostrophe, de double trait union")
                                                                       ])
    # nom_nom_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_nom_receveur_update_regexp = ""
    nom_nom_receveur_update_wtf = StringField("Nom", validators=[Length(min=0, max=50, message="min 0 max 50"),
                                                                 Regexp(nom_nom_receveur_update_regexp,
                                                                        message="Pas de chiffres, de caractères "
                                                                                "spéciaux, "
                                                                                "d'espace à double, de double "
                                                                                "apostrophe, de double trait union")
                                                                 ])
    # nom_adresse_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ0-9]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ0-9-]+$"
    nom_adresse_receveur_update_regexp = ""
    nom_adresse_receveur_update_wtf = StringField("Adresse ", validators=[Length(min=0, max=50, message="min 0 max 50"),
                                                                          Regexp(nom_adresse_receveur_update_regexp,
                                                                                 message="Veuillez inserer une adresse valide. EX:"
                                                                                         "1110 Morges"
                                                                                         "LE NPA puis le lieu"
                                                                                 )
                                                                          ])
    # nom_mail_regexp = "([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    nom_mail_receveur_update_regexp = ""
    nom_mail_receveur_update_wtf = StringField("Mail", validators=[Length(min=0, max=50, message="min 0 max 50"),
                                                                   Regexp(nom_mail_receveur_update_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    # nom_num_tel_regexp = "/^\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$/"
    # nom_num_tel_regexp = "^[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}$"
    nom_numero_telephone_receveur_update_regexp = ""
    nom_numero_telephone_receveur_update_wtf = StringField("Numéro de Téléphone",
                                                  validators=[Length(min=0, max=13, message="min 2 max 30"),
                                                              Regexp(nom_numero_telephone_receveur_update_regexp,
                                                                     message="Pas de numéro de telephone dépassant 30 caractères "
                                                                             "pas de lettres"
                                                                     )
                                                              ])

    nom_date_naissance_receveur_update_wtf = DateField("Date de Naissance",
                                                       validators=[InputRequired("Date obligatoire"),
                                                                   DataRequired("Date non valide")

                                                                   ])

    nom_groupe_sanguin_receveur_update_regexp = ""
    nom_groupe_sanguin_receveur_update_wtf = StringField("Groupe Sanguin", validators=[Length(min=0, max=50, message="min 0 max 50"),
                                                                   Regexp(nom_groupe_sanguin_receveur_update_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])

class FormWTFDeleteFilm(FlaskForm):
    """
        Dans le formulaire "film_delete_wtf.html"

        nom_film_delete_wtf : Champ qui reçoit la valeur du film, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "film".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_receveur".
    """
    nom_film_delete_wtf = StringField("Effacer ce film")
    submit_btn_del_film = SubmitField("Effacer film")
    submit_btn_conf_del_film = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")





























