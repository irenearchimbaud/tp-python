import argparse
import time
import json
from syswatch.model import SystemCollector
from syswatch.database import MetricsDatabase


def afficher_stats(db, hostname):
    stats = db.get_statistics(hostname)
    if not stats or stats["count"] == 0:
        print("Aucune donnée disponible.")
        return

    print("\n=== Statistiques (24h) ===")
    print(f"CPU Moy: {stats['cpu_avg']:.2f}% | Min: {stats['cpu_min']:.2f}% | Max: {stats['cpu_max']:.2f}%")
    print(f"RAM Moy: {stats['mem_avg']:.2f}% | Min: {stats['mem_min']:.2f}% | Max: {stats['mem_max']:.2f}%")

def couleur_pourcentage(valeur):
    if valeur >= 80:
        return "\033[91m"  # rouge
    elif valeur >= 60:
        return "\033[93m"  # jaune
    else:
        return "\033[92m"  # vert


def reset_couleur():
    return "\033[0m"


def barre_ascii(pourcentage, longueur=10):
    remplissage = int((pourcentage / 100) * longueur)
    return "█" * remplissage + "░" * (longueur - remplissage)

def main():
    parser = argparse.ArgumentParser(description="SysWatch - Monitoring système")
    parser.add_argument("--collect", action="store_true", help="Collecte continue")
    parser.add_argument("--interval", type=int, default=60, help="Intervalle en secondes")
    parser.add_argument("--stats", action="store_true", help="Afficher statistiques")
    parser.add_argument("--export", help="Exporter dernière mesure en JSON")
    parser.add_argument("--cleanup", type=int, help="Supprimer données > N jours")

    args = parser.parse_args()

    collector = SystemCollector()
    db = MetricsDatabase()

    if args.cleanup:
        deleted = db.cleanup_old(args.cleanup)
        print(f"{deleted} entrées supprimées.")
        return

    if args.stats:
        afficher_stats(db, collector.hostname)
        return

    if args.collect:
        print("Collecte continue (Ctrl+C pour arrêter)")
        try:
            while True:
                metrics = collector.collect()
                print(metrics)
                db.save(metrics)
                time.sleep(args.interval)
                cpu_color = couleur_pourcentage(metrics.cpu_percent)
                ram_color = couleur_pourcentage(metrics.memory_percent)
                print("\n=== SysWatch ===")
                print(
                    f"CPU  {cpu_color}[{barre_ascii(metrics.cpu_percent)}] "
                    f"{metrics.cpu_percent:.1f}%{reset_couleur()}"
                )
                print(
                    f"RAM  {ram_color}[{barre_ascii(metrics.memory_percent)}] "
                    f"{metrics.memory_percent:.1f}%{reset_couleur()}"
                )
        except KeyboardInterrupt:
            print("\nArrêt demandé.")
        return

    metrics = collector.collect()
    print(metrics)
    db.save(metrics)

    if args.export:
        with open(args.export, "w") as f:
            json.dump(metrics.to_dict(), f, indent=2)
        print(f"Export JSON : {args.export}")


if __name__ == "__main__":
    main()