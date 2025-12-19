def analyser_commandes(commandes):
    #total des commandes livréées
    livrees = [c for c in commandes if c["statut"] == "livree"]
    total_livrees = sum(c["montant"] for c in livrees)
    
    clients_totaux = {}
    for c in commandes:
        clients_totaux[c["client"]] = clients_totaux.get(c["client"], 0) + c["montant"]
    meilleur_client = max(clients_totaux, key=lambda x: clients_totaux[x])
    
    # commandes par jour avec le montant moyen 
    commandes_par_jour = {}
    for c in commandes:
        commandes_par_jour[c["date"]] = commandes_par_jour.get(c["date"], 0) + 1
    moyenne_par_commande = total_livrees / len(livrees) if livrees else 0
    
    return {
        "total_livrees": total_livrees,
        "meilleur_client": meilleur_client,
        "commandes_par_jour": commandes_par_jour,
        "moyenne_par_commande": moyenne_par_commande
    }


def trier_commandes_complexe(commandes):
    statut_ordre = {"livree": 0, "en_cours": 1, "annulee": 2}
    return sorted( #en utilisant sorted comme demandé dans l'énoncée
        commandes,
        key=lambda c: (statut_ordre[c["statut"]], -c["montant"])
    )
