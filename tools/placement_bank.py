"""Banque de questions du test de niveau (indépendante des leçons).

Chaque question :
  skill    : write (réponse à écrire), grammar, vocab, reading, listening
  prompt   : consigne ou phrase à compléter (« ___ » = trou)
  text     : texte à lire (reading) ; audio : texte entendu (listening)
  question : question posée sur le texte ou l'audio
  options  : QCM, la première est la bonne réponse (mélangées dans l'app)
  accept   : réponses acceptées pour « write » (accents tolérés)
"""

def W(prompt, accept, hint=None):
    return {"skill": "write", "prompt": prompt, "accept": accept, "hint": hint}


def G(prompt, options, skill="grammar"):
    return {"skill": skill, "prompt": prompt, "options": options}


def R(text, question, options):
    return {"skill": "reading", "text": text, "question": question, "options": options}


def L(audio, question, options):
    return {"skill": "listening", "audio": audio, "question": question, "options": options}


BANK = {
    "A1": [
        W("Écris en espagnol : « merci beaucoup »", ["muchas gracias"]),
        W("Yo ___ de Francia. (ser)", ["soy"]),
        W("¿Cuántos años ___ tú? (tener)", ["tienes"]),
        W("Écris en espagnol : « la maison »", ["la casa", "casa"]),
        G("Mi hermana ___ muy simpática.", ["es", "está", "son", "hay", "tiene"]),
        G("En mi casa ___ dos baños.", ["hay", "están", "es", "tiene", "son"]),
        G("Nosotros ___ en Guadalajara. (vivir)", ["vivimos", "viven", "vivo", "vivís", "viviendo"]),
        G("¿A qué hora ___ la tienda?", ["abre", "abro", "abres", "abrimos", "abrir"]),
        G("« La semana que viene » signifie…", ["la semaine prochaine", "la semaine dernière", "cette semaine", "le week-end", "le mois prochain"], "vocab"),
        R("Hola, me llamo Daniela. Tengo veinticuatro años y vivo en Puebla con mis papás y mi hermano. "
          "Trabajo en un café y los domingos voy al mercado con mi abuela.",
          "Avec qui Daniela va-t-elle au marché ?",
          ["Avec sa grand-mère", "Avec son frère", "Avec ses parents", "Seule", "Avec une amie"]),
        R("MUSEO DE ARTE POPULAR — Cerrado los lunes. De martes a domingo, de 10:00 a 18:00.",
          "Quand peut-on visiter le musée ?",
          ["Le mardi à 11 h", "Le lundi à 10 h", "Le dimanche à 19 h", "Tous les jours", "Le lundi après-midi"]),
        L("Buenos días. Quiero dos tacos de pollo y un agua de jamaica, por favor.",
          "Que commande la personne ?",
          ["Deux tacos au poulet et une eau de jamaica", "Deux tacos au porc et un soda", "Un taco au poulet et un café",
           "Trois tacos et une bière", "Deux quesadillas et un jus"]),
        L("Mi cumpleaños es el doce de marzo.", "Quand est son anniversaire ?",
          ["Le 12 mars", "Le 2 mars", "Le 12 mai", "Le 20 mars", "Le 10 mars"]),
        L("La farmacia está a la derecha del banco, enfrente del parque.", "Où est la pharmacie ?",
          ["À droite de la banque, en face du parc", "À gauche de la banque", "Derrière le parc", "Dans le parc", "À côté de l'église"]),
    ],
    "A2": [
        W("Ayer nosotros ___ al cine. (ir)", ["fuimos"]),
        W("El año pasado ellos ___ en Cancún. (estar)", ["estuvieron"]),
        W("¿Qué ___ tú anoche? (hacer)", ["hiciste"]),
        W("Mañana ___ a llover. (ir)", ["va"]),
        G("Me ___ mucho los tacos al pastor.", ["gustan", "gusta", "gusto", "gustas", "gustamos"]),
        G("Cuando era niño, ___ al parque todos los domingos.", ["iba", "fui", "voy", "iré", "he ido"]),
        G("Este regalo es ___ ti.", ["para", "por", "a", "de", "en"]),
        G("Mi hermano es ___ alto ___ mi papá.", ["más… que", "tan… que", "más… como", "mucho… que", "muy… de"]),
        G("« Me duele la garganta » signifie…", ["J'ai mal à la gorge", "J'ai mal à la tête", "J'ai mal au ventre", "J'ai soif", "J'ai froid"], "vocab"),
        R("El sábado pasado fui a Teotihuacán con mis primos. Salimos muy temprano porque queríamos subir a la "
          "Pirámide del Sol antes del calor. Al final no subimos: había demasiada gente y mi prima se sentía mal.",
          "Pourquoi ne sont-ils pas montés sur la pyramide ?",
          ["Il y avait trop de monde et sa cousine se sentait mal", "Il faisait trop chaud", "Ils sont arrivés trop tard",
           "La pyramide était fermée", "Ils n'avaient pas de billets"]),
        R("Se renta cuarto amueblado en la colonia Narvarte. Incluye internet y agua. No se aceptan mascotas. "
          "A cinco minutos del metro Etiopía.",
          "Quelle affirmation est vraie ?",
          ["Internet est inclus", "Les animaux sont acceptés", "Le logement est loin du métro",
           "La chambre n'est pas meublée", "L'eau n'est pas incluse"]),
        L("Perdón por llegar tarde. Es que el metro se detuvo veinte minutos entre dos estaciones.",
          "Pourquoi la personne est-elle en retard ?",
          ["Le métro s'est arrêté vingt minutes", "Elle s'est réveillée tard", "Il y avait des bouchons",
           "Elle a raté le bus", "Elle s'est perdue"]),
        L("Si quieres, nos vemos el jueves en la tarde, porque el miércoles tengo que trabajar hasta las nueve.",
          "Quand se voient-ils ?",
          ["Jeudi après-midi", "Mercredi soir", "Mercredi à 9 h", "Jeudi matin", "Vendredi après-midi"]),
        L("Hace dos años que vivo aquí, pero todavía me pierdo en el centro.",
          "Que dit la personne ?",
          ["Elle vit ici depuis deux ans et se perd encore dans le centre", "Elle est arrivée il y a deux jours",
           "Elle ne se perd jamais", "Elle va déménager dans deux ans", "Elle travaille dans le centre depuis deux ans"]),
    ],
    "B1": [
        W("Espero que ___ buen viaje. (tener, tú)", ["tengas"]),
        W("Cuando ___ a la casa, te llamo. (llegar, yo)", ["llegue"]),
        W("Si tuviera tiempo, ___ más. (leer, yo)", ["leería"]),
        W("Ya ___ visto esa película tres veces. (haber, yo)", ["he"]),
        G("Busco un departamento que ___ cerca del trabajo.", ["esté", "está", "estará", "estaba", "estar"]),
        G("Cuando llegué a la fiesta, mis amigos ya ___.", ["se habían ido", "se fueron", "se van", "se iban a ir", "se han ido"]),
        G("No es caro, ___ barato.", ["sino", "pero", "si no", "sin", "aunque"]),
        G("Te lo explico ___ que no te preocupes.", ["para", "por", "porque", "aunque", "sino"]),
        G("« Echarle ganas » signifie…", ["Faire des efforts", "Avoir faim", "Abandonner", "Se mettre en colère", "Avoir sommeil"], "vocab"),
        R("Querida Ana: perdona que no te haya escrito antes. Desde que empecé en la nueva chamba casi no tengo "
          "tiempo libre. Mi jefa es buena onda, pero las juntas duran horas. Ojalá que el mes que entra pueda "
          "tomarme unos días para ir a verte a Mérida.",
          "Que souhaite l'autrice de la lettre ?",
          ["Prendre quelques jours le mois prochain pour aller voir Ana", "Changer de travail",
           "Que sa cheffe soit plus sympathique", "Qu'Ana vienne la voir", "Avoir moins de réunions"]),
        R("AVISO: Por obras de mantenimiento, la Línea 1 del Metro permanecerá cerrada hasta nuevo aviso. "
          "Se recomienda usar el Metrobús o las rutas alternas de autobús.",
          "Que dit l'avis ?",
          ["La ligne 1 est fermée pour une durée indéterminée", "La ligne 1 rouvre demain", "Le Metrobús est fermé",
           "Les bus ne circulent pas", "Les travaux sont terminés"]),
        L("Me hubiera gustado ir a la boda, pero justo ese fin de semana tenía un examen y no me dio tiempo de nada.",
          "Que s'est-il passé ?",
          ["Elle n'est pas allée au mariage à cause d'un examen", "Elle est allée au mariage après son examen",
           "Le mariage a été annulé", "Elle a oublié le mariage", "Elle n'était pas invitée"]),
        L("Ahorita no puedo, estoy en una junta. Te marco en cuanto salga.",
          "Que va faire la personne ?",
          ["Rappeler dès la fin de sa réunion", "Rappeler demain", "Venir tout de suite",
           "Envoyer un message pendant la réunion", "Annuler la réunion"]),
        L("Aunque llueva, vamos a ir a la feria; ya compramos los boletos.",
          "Que vont-ils faire ?",
          ["Aller à la foire même s'il pleut", "Ne pas y aller s'il pleut", "Acheter les billets",
           "Rester chez eux car la foire est annulée", "Décider plus tard"]),
    ],
    "B2": [
        W("Si me lo ___ dicho antes, habría venido. (haber, tú)", ["hubieras", "hubieses"]),
        W("Me pidió que no le ___ nada a nadie. (decir, yo)", ["dijera", "dijese"]),
        W("No creo que ellos ___ a tiempo. (llegar)", ["lleguen"]),
        W("Ojalá ___ más tiempo el año pasado. (tener, yo — plus-que-parfait)", ["hubiera tenido", "hubiese tenido"]),
        G("De ___ sabido que llovería, me habría quedado en casa.", ["haber", "había", "hubiera", "habría", "he"]),
        G("Le prometí que ___ por ella a las ocho.", ["pasaría", "pasaré", "pase", "pasara", "pasaba"]),
        G("Con tal de que me ___, te presto el coche.", ["lo devuelvas mañana", "lo devuelves mañana", "lo devolverás mañana",
                                                       "lo devolviste mañana", "devolverlo mañana"]),
        G("___ sea difícil, lo vamos a lograr.", ["Aunque", "A pesar de", "Sin embargo", "Por lo tanto", "Ya que"]),
        G("« Dar el avión » signifie…", ["Faire semblant d'écouter", "Prendre l'avion", "Donner un coup de main",
                                         "Se tromper", "Partir sans prévenir"], "vocab"),
        R("Si bien el gobierno capitalino presume la ampliación de la red de ciclovías, colectivos ciudadanos advierten "
          "que muchas de ellas no conectan entre sí y que, en la práctica, siguen siendo más simbólicas que funcionales.",
          "Quelle est la critique des collectifs citoyens ?",
          ["Les pistes ne sont pas reliées entre elles et servent peu en pratique", "Il n'y a aucune piste cyclable",
           "Les pistes coûtent trop cher", "Le gouvernement a supprimé des pistes", "Les cyclistes refusent de les utiliser"]),
        R("No es que no me guste mi trabajo; es que llevo tres años haciendo lo mismo y siento que ya no aprendo nada. "
          "Por eso, aunque me ofrecieran un aumento, me iría.",
          "Que pense la personne ?",
          ["Elle partirait même avec une augmentation, car elle n'apprend plus rien", "Elle déteste son travail",
           "Elle resterait pour une augmentation", "Elle travaille là depuis trois mois", "Elle veut surtout gagner plus"]),
        L("La neta, si hubiera sabido que el examen estaba tan pesado, me habría puesto las pilas desde antes.",
          "Que ressent la personne ?",
          ["Elle regrette de ne pas avoir travaillé plus tôt", "Elle a réussi l'examen facilement",
           "Elle savait que l'examen serait difficile", "Elle passe l'examen demain", "L'examen a été annulé"]),
        L("No te creas todo lo que circula en redes; esa nota la sacaron de contexto para generar polémica.",
          "Que dit la personne de cette information ?",
          ["Elle a été sortie de son contexte pour créer la polémique", "Elle est vraie", "Elle vient d'un journal sérieux",
           "Il faut la partager", "Elle parle des réseaux sociaux"]),
        L("Me late que nos están haciendo de chivo los tamales con ese contrato.",
          "Que pense la personne ?",
          ["Qu'on est en train de les arnaquer avec ce contrat", "Que le contrat est très avantageux",
           "Qu'elle veut manger des tamales", "Qu'il faut signer vite", "Que le contrat parle de nourriture"]),
    ],
}

# Composition d'une série de 10 questions par niveau.
PLAN = {"write": 3, "grammar": 2, "vocab": 1, "reading": 2, "listening": 2}
