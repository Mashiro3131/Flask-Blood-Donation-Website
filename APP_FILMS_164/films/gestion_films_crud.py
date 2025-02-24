"""Gestion des "routes" FLASK et des données pour les films.
Fichier : gestion_films_crud.py
Auteur : OM 2022.04.11
"""
from pathlib import Path

from flask import flash, render_template, session
from flask import redirect
from flask import request
from flask import url_for

from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.films.gestion_films_wtf_forms import FormWTFUpdateFilm, FormWTFAjouterReceveur, FormWTFDeleteFilm

"""Ajouter un film grâce au formulaire "film_add_wtf.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_add

Test : exemple: cliquer sur le menu "Films/Genres" puis cliquer sur le bouton "ADD" d'un "film"

Paramètres : sans


Remarque :  Dans le champ "nom_film_update_wtf" du formulaire "films/films_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python dans le fichier ""
            On ne doit pas accepter un champ vide.
"""
@app.route("/film_add", methods=['GET', 'POST'])
def film_add_wtf():
    # Objet formulaire pour AJOUTER un film
    form_add_receveur = FormWTFAjouterReceveur()
    if request.method == "POST":
        try:
            if form_add_receveur.validate_on_submit():
                nom_prenom_receveur_add_wtf = form_add_receveur.nom_prenom_receveur_add_wtf.data
                nom_nom_receveur_add_wtf = form_add_receveur.nom_nom_receveur_add_wtf.data
                nom_adresse_receveur_add_wtf = form_add_receveur.nom_adresse_receveur_add_wtf.data
                nom_mail_receveur_add_wtf = form_add_receveur.nom_mail_receveur_add_wtf.data
                nom_num_tel_receveur_add_wtf = form_add_receveur.nom_num_tel_receveur_add_wtf.data
                nom_date_naissance_receveur_add_wtf = form_add_receveur.nom_date_naissance_receveur_add_wtf.data
                nom_groupe_sanguin_receveur_add_wtf = form_add_receveur.nom_groupe_sanguin_receveur_add_wtf.data


                valeurs_insertion_dictionnaire = {"value_name_prenom_receveur_add":
                                                  nom_prenom_receveur_add_wtf,
                                                  "value_name_nom_receveur_add":
                                                      nom_nom_receveur_add_wtf,
                                                  "value_name_adresse_receveur_add":
                                                      nom_adresse_receveur_add_wtf,
                                                  "value_name_mail_receveur_add":
                                                      nom_mail_receveur_add_wtf,
                                                  "value_name_num_tel_receveur_add":
                                                      nom_num_tel_receveur_add_wtf,
                                                  "value_name_date_naissance_receveur_add":
                                                      nom_date_naissance_receveur_add_wtf,
                                                  "value_name_groupe_sanguin_receveur_add":
                                                      nom_groupe_sanguin_receveur_add_wtf
                                                  }


                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_film = """INSERT INTO t_receveur (id_receveur, prenom, nom, adresse, mail, numero_telephone, date_naissance, groupe_sanguin) VALUES (NULL,%(value_name_prenom_receveur_add)s,%(value_name_nom_receveur_add)s,%(value_name_adresse_receveur_add)s,%(value_name_mail_receveur_add)s,%(value_name_num_tel_receveur_add)s,%(value_name_date_naissance_receveur_add)s,%(value_name_groupe_sanguin_receveur_add)s )"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_film, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion du nouveau film (id_receveur_sel=0 => afficher tous les films)
                return redirect(url_for('film_add_wtf', id_receveur_sel=0))

        except Exception as Exception_genres_ajouter_wtf:
            raise ExceptionGenresAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{film_add_wtf.__name__} ; "
                                            f"{Exception_genres_ajouter_wtf}")

    return render_template("films/film_add_wtf.html", form_add_receveur=form_add_receveur)


"""Editer(update) un film qui a été sélectionné dans le formulaire "film_add_wtf.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_update

Test : exemple: cliquer sur le menu "Films/Genres" puis cliquer sur le bouton "EDIT" d'un "film"

Paramètres : sans

But : Editer(update) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"

Remarque :  Dans le champ "nom_film_update_wtf" du formulaire "films/films_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python.
            On ne doit pas accepter un champ vide.
"""


@app.route("/film_update", methods=['GET', 'POST'])
def film_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_receveur"
    id_receveur_update = request.values['id_film_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update_receveur = FormWTFUpdateFilm()
    try:
        print(" on submit ", form_update_receveur.validate_on_submit(), "  ", form_update_receveur.validate())
        if form_update_receveur.validate_on_submit():
            # Récupèrer la valeur du champ depuis "genre_update_wtf.html" après avoir cliqué sur "SUBMIT".
            nom_prenom_receveur_update_wtf = form_update_receveur.nom_prenom_receveur_update_wtf.data
            nom_nom_receveur_update_wtf = form_update_receveur.nom_nom_receveur_update_wtf.data
            nom_adresse_receveur_update_wtf = form_update_receveur.nom_adresse_receveur_update_wtf.data
            nom_mail_receveur_update_wtf = form_update_receveur.nom_mail_receveur_update_wtf.data
            nom_num_tel_receveur_update_wtf = form_update_receveur.nom_numero_telephone_receveur_update_wtf.data
            nom_date_naissance_receveur_update_wtf = form_update_receveur.nom_date_naissance_receveur_update_wtf.data
            nom_groupe_sanguin_receveur_update_wtf = form_update_receveur.nom_groupe_sanguin_receveur_update_wtf.data

            valeur_update_dictionnaire = {"value_id_donneur": id_receveur_update,
                                          "value_name_prenom_receveur_update": nom_prenom_receveur_update_wtf,
                                          "value_name_nom_receveur_update": nom_nom_receveur_update_wtf,
                                          "value_name_adresse_receveur_update": nom_adresse_receveur_update_wtf,
                                          "value_name_mail_receveur_update": nom_mail_receveur_update_wtf,
                                          "value_name_numero_telephone_receveur_update": nom_num_tel_receveur_update_wtf,
                                          "value_name_date_naissance_receveur_update": nom_date_naissance_receveur_update_wtf,
                                          "value_name_groupe_sanguin_receveur_update": nom_groupe_sanguin_receveur_update_wtf
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_nom_receveur = """UPDATE t_donneur SET prenom = %(value_name_prenom_receveur_update)s, nom = %(value_name_nom_receveur_update)s, adresse = %(value_name_adresse_receveur_update)s,  mail = %(value_name_mail_receveur_update)s, numero_telephone = %(value_name_numero_telephone_receveur_update)s, date_naissance = %(value_name_date_naissance_receveur_update)s, groupe_sanguin = %(value_name_groupe_sanguin_receveur_update)s WHERE id_receveur = %(value_id_receveur)s"""
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_nom_receveur, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Afficher seulement le film modifié, "ASC" et l'"id_receveur_update"
            return redirect(url_for('film_add_wtf', id_receveur_sel=id_receveur_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_receveur" et "intitule_genre" de la "t_donneur"
            str_sql_id_film = "SELECT * FROM t_receveur WHERE id_receveur = %(value_id_receveur)s"
            valeur_select_dictionnaire = {"value_id_receveur": id_receveur_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_film, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom genre" pour l'UPDATE
            data_film = mybd_conn.fetchone()
            print("data_film ", data_film, " type ", type(data_film), " genre ",
                  data_film["prenom"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "film_update_wtf.html"
            form_update_receveur.nom_prenom_receveur_update_wtf.data = data_film["prenom"]
            print(f" dta film  ", data_film["prenom"])
            form_update_receveur.duree_film_update_wtf.data = data_film["duree_film"]
            print(f" duree film  ", data_film["duree_film"], "  type ", type(data_film["duree_film"]))
            form_update_receveur.description_film_update_wtf.data = data_film["description_film"]
            form_update_receveur.datesortie_film_update_wtf.data = data_film["date_sortie_film"]





    except Exception as Exception_film_update_wtf:
        raise ExceptionFilmUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                     f"{film_update_wtf.__name__} ; "
                                     f"{Exception_film_update_wtf}")

    return render_template("films/film_update_wtf.html", form_update_receveur=form_update_receveur)


"""Effacer(delete) un film qui a été sélectionné dans le formulaire "film_add_wtf.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_delete
    
Test : ex. cliquer sur le menu "film" puis cliquer sur le bouton "DELETE" d'un "film"
    
Paramètres : sans

Remarque :  Dans le champ "nom_film_delete_wtf" du formulaire "films/film_delete_wtf.html"
            On doit simplement cliquer sur "DELETE"
"""


@app.route("/film_delete", methods=['GET', 'POST'])
def film_delete_wtf():
    # Pour afficher ou cacher les boutons "EFFACER"
    data_film_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_receveur"
    id_film_delete = request.values['id_receveur_btn_delete_html']

    # Objet formulaire pour effacer le film sélectionné.
    form_delete_film = FormWTFDeleteFilm()
    try:
        # Si on clique sur "ANNULER", afficher tous les films.
        if form_delete_film.submit_btn_annuler.data:
            return redirect(url_for("film_add_wtf", id_receveur_sel=0))

        if form_delete_film.submit_btn_conf_del_film.data:
            # Récupère les données afin d'afficher à nouveau
            # le formulaire "films/film_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
            data_film_delete = session['data_film_delete']
            print("data_film_delete ", data_film_delete)

            flash(f"Effacer le film de façon définitive de la BD !!!", "danger")
            # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
            # On affiche le bouton "Effacer genre" qui va irrémédiablement EFFACER le genre
            btn_submit_del = True

        # L'utilisateur a vraiment décidé d'effacer.
        if form_delete_film.submit_btn_del_film.data:
            valeur_delete_dictionnaire = {"value_id_film": id_film_delete}
            print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

            str_sql_delete_fk_film_genre = """DELETE FROM t_genre_film WHERE fk_film = %(value_id_film)s"""
            str_sql_delete_film = """DELETE FROM t_receveur WHERE id_receveur = %(value_id_film)s"""
            # Manière brutale d'effacer d'abord la "fk_film", même si elle n'existe pas dans la "t_genre_film"
            # Ensuite on peut effacer le film vu qu'il n'est plus "lié" (INNODB) dans la "t_genre_film"
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_delete_fk_film_genre, valeur_delete_dictionnaire)
                mconn_bd.execute(str_sql_delete_film, valeur_delete_dictionnaire)

            flash(f"Film définitivement effacé !!", "success")
            print(f"Film définitivement effacé !!")

            # afficher les données
            return redirect(url_for('film_add_wtf', id_receveur_sel=0))
        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_film": id_film_delete}
            print(id_film_delete, type(id_film_delete))

            # Requête qui affiche le film qui doit être efffacé.
            str_sql_genres_films_delete = """SELECT * FROM t_receveur WHERE id_receveur = %(value_id_film)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_genres_films_delete, valeur_select_dictionnaire)
                data_film_delete = mydb_conn.fetchall()
                print("data_film_delete...", data_film_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "films/film_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_film_delete'] = data_film_delete

            # Le bouton pour l'action "DELETE" dans le form. "film_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_film_delete_wtf:
        raise ExceptionFilmDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                     f"{film_delete_wtf.__name__} ; "
                                     f"{Exception_film_delete_wtf}")

    return render_template("films/film_delete_wtf.html",
                           form_delete_film=form_delete_film,
                           btn_submit_del=btn_submit_del,
                           data_film_del=data_film_delete
                           )
