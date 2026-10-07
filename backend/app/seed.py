import os
from typing import Any

from openai import OpenAI


def generate_business_intelligence(message: str, context: dict[str, Any]) -> dict[str, Any]:
    if not message or len(message.strip()) < 3:
        message = "Fournissez un résumé de la performance commerciale actuelle."

    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        try:
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "Tu es un conseiller commercial expert pour une entreprise commerciale. Donne des recommandations concrètes et courtes.",
                    },
                    {
                        "role": "user",
                        "content": f"Question: {message}\nContexte: {context}",
                    },
                ],
                temperature=0.6,
            )
            answer = response.choices[0].message.content.strip()
            return {
                "summary": answer,
                "action_points": [
                    "Suivre les KPI du mois",
                    "Renforcer les ventes les plus rentables",
                    "Réduire les ruptures de stock",
                ],
                "confidence": 0.95,
                "model": "openai",
            }
        except Exception as exc:  # pragma: no cover
            print(f"OpenAI request failed: {exc}")

    low_stock = context.get("low_stock", 0)
    monthly_revenue = context.get("monthly_revenue", 0)
    total_clients = context.get("total_clients", 0)
    sales_count = context.get("sales_count", 0)

    summary_lines = [
        f"Le tableau de bord actuel montre {total_clients} clients actifs et {sales_count} ventes enregistrées.",
        f"Le chiffre d'affaires du mois est estimé à {monthly_revenue:,.0f} FCFA.",
    ]
    if low_stock > 0:
        summary_lines.append(f"{low_stock} produits sont en stock critique et nécessitent une commande rapide.")
    else:
        summary_lines.append("Le niveau de stock est globalement stable et rassurant.")

    summary = " ".join(summary_lines)
    action_points = [
        "Prioriser les clients à forte valeur avec des relances ciblées.",
        "Renforcer les promotions sur les produits à forte rotation.",
        "Contrôler les niveaux de stock avant la prochaine commande.",
    ]

    return {
        "summary": summary,
        "action_points": action_points,
        "confidence": 0.87,
        "model": "local-heuristic",
    }
