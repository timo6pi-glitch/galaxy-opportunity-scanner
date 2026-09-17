# galaxy_opportunity_scanner.py
# Un seul fichier, exécutable localement ou sur GitHub Actions

import json
import os
from datetime import datetime
from typing import List, Dict

# === CONFIGURATION ===
SOURCES = [
    {"name": "Twitter", "query": "freelance invoice late OR client hasn't paid", "weight": 1.0},
    {"name": "Reddit", "query": "r/freelance invoice OR r/smallbusiness problem", "weight": 1.0},
    {"name": "Product Hunt", "query": "new launch SaaS", "weight": 0.8},
    {"name": "Indie Hackers", "query": "revenue OR MRR OR launched", "weight": 0.9},
    {"name": "Google Trends", "query": "rising queries business tools", "weight": 0.7},
]

OUTPUT_DIR = "output"
OUTPUT_FILE = "{}/galaxy_opportunities_{}.json".format(OUTPUT_DIR, datetime.now().strftime("%Y%m%d"))

# === CORE AGENT LOGIC ===
class OpportunityScanner:
    def __init__(self):
        self.opportunities: List[Dict] = []
    
    def scan_source(self, source: Dict) -> List[Dict]:
        """
        Simule un scan de source (à remplacer par de vraies API)
        Retourne une liste de posts/signaux avec : source, texte, date, auteur
        """
        # Données mockées variées pour tester
        mock_data = {
            "Twitter": [
                {"text": "I'm losing 20% of my revenue to late invoices. Need a better system.", "author": "@freelance_dev"},
                {"text": "Spent 5 hours this week chasing unpaid invoices. This is not what I signed up for.", "author": "@designer_pro"},
                {"text": "My SaaS churn is 40% because of failed payments. Stripe dunning is not enough.", "author": "@saas_founder"},
                {"text": "Looking for a tool to track employee certifications. Excel is a nightmare.", "author": "@hr_manager"},
                {"text": "Google Reviews saved my plumbing business. Went from 10 to 100+ reviews in 3 months.", "author": "@plumber_bob"},
            ],
            "Reddit": [
                {"text": "How do you handle certification renewals for your team? Excel is a nightmare.", "author": "u/hr_manager"},
                {"text": "Anyone else losing sleep over failed subscription payments?", "author": "u/saas_builder"},
                {"text": "Best way to get more Google Reviews for my local business?", "author": "u/small_biz_owner"},
                {"text": "Freelancers: what % of your invoices are paid late?", "author": "u/freelance_dev"},
            ],
            "Product Hunt": [
                {"text": "Just launched: AI tool for automating customer support", "author": "@ph_maker"},
                {"text": "New SaaS: Invoice tracking for freelancers", "author": "@indie_founder"},
            ],
            "Indie Hackers": [
                {"text": "Hit $5k MRR with my certification tracking tool", "author": "@builder_mike"},
                {"text": "How I recovered 30% of lost revenue with better dunning", "author": "@saas_jane"},
            ],
            "Google Trends": [
                {"text": "Rising: invoice automation software", "author": "trends_bot"},
                {"text": "Rising: employee certification management", "author": "trends_bot"},
                {"text": "Rising: Google Reviews for local business", "author": "trends_bot"},
            ],
        }
        
        return [
            {
                "source": source["name"],
                "text": item["text"],
                "date": datetime.now().isoformat(),
                "author": item["author"],
                "query_matched": source["query"]
            }
            for item in mock_data.get(source["name"], [])
        ]
    
    def extract_problem(self, signal: Dict) -> Dict:
        """
        Extrait le problème mentionné dans un signal
        Utilise un LLM (Claude, GPT-4) pour l'extraction
        """
        # TODO: Appeler Claude API ou GPT-4 API ici
        # Prompt: "Extract the business problem from this text. Return JSON: {problem, who_has_it, how_often, current_solution}"
        
        problem = {
            "problem": "Late invoice payments",
            "who_has_it": "Freelance developers and designers",
            "how_often": "20% of revenue lost",
            "current_solution": "Manual tracking in Excel, sending reminder emails",
            "source_signal": signal,
            "pain_level": "high"
        }
        return problem
    
    def score_opportunity(self, problem: Dict) -> float:
        """
        Score une opportunité selon :
        - Fréquence du problème (combien de fois mentionné)
        - Douleur (mots comme "losing", "hate", "frustrated")
        - Capacité à payer (mention de revenus, budget)
        """
        score = 0.0
        
        # Fréquence (à calculer sur tous les signaux agrégés)
        score += 0.3
        
        # Douleur (détection de mots-clés)
        pain_words = ["losing", "hate", "frustrated", "annoying", "waste time", "not what I signed up for"]
        if any(word in problem["problem"].lower() or word in problem["who_has_it"].lower() for word in pain_words):
            score += 0.4
        
        # Capacité à payer (détection de revenus/budget)
        if any(word in problem["who_has_it"].lower() for word in ["revenue", "budget", "paying", "$", "€"]):
            score += 0.3
        
        return round(score, 2)
    
    def generate_business_idea(self, problem: Dict) -> Dict:
        """
        Génère une idée de business basée sur le problème
        Utilise un LLM pour la génération
        """
        # TODO: Appeler Claude API ou GPT-4 API ici
        # Prompt: "Given this problem, suggest a simple SaaS or service to solve it. Return JSON: {idea, target_customer, price_point, mvp_features}"
        
        idea = {
            "idea": "Automated invoice reminder SaaS for freelancers",
            "target_customer": "Freelance developers and designers earning 3k-10k€/month",
            "price_point": "19€/month or 5% of recovered revenue",
            "mvp_features": [
                "CSV upload of invoices",
                "Automatic email reminders at J+1, J+7, J+14",
                "Weekly report of late payments",
                "Integration with Stripe/PayPal"
            ],
            "estimated_market_size": "500k+ freelancers in EU/US",
            "problem_reference": problem
        }
        return idea
    
    def run_daily_scan(self) -> List[Dict]:
        """
        Exécute le scan quotidien et retourne les opportunités triées par score
        """
        all_signals = []
        
        # 1. Scanner toutes les sources
        for source in SOURCES:
            signals = self.scan_source(source)
            all_signals.extend(signals)
        
        # 2. Extraire les problèmes
        problems = [self.extract_problem(signal) for signal in all_signals]
        
        # 3. Agréger les problèmes similaires (regrouper par thème)
        aggregated = {}
        for problem in problems:
            key = problem["problem"].lower()
            if key not in aggregated:
                aggregated[key] = problem
            else:
                # Incrémenter un compteur de fréquence
                aggregated[key]["frequency"] = aggregated[key].get("frequency", 1) + 1
        
        # 4. Scorer et générer les idées
        opportunities = []
        for problem in aggregated.values():
            score = self.score_opportunity(problem)
            idea = self.generate_business_idea(problem)
            
            opportunities.append({
                "score": score,
                "problem": problem,
                "business_idea": idea,
                "timestamp": datetime.now().isoformat()
            })
        
        # 5. Trier par score décroissant
        opportunities.sort(key=lambda x: x["score"], reverse=True)
        
        return opportunities[:10]  # Top 10 opportunités

# === EXECUTION ===
if __name__ == "__main__":
    # Créer le dossier output s'il n'existe pas
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    scanner = OpportunityScanner()
    opportunities = scanner.run_daily_scan()
    
    # Sauvegarder dans un fichier JSON
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump({
            "scan_date": datetime.now().isoformat(),
            "total_opportunities": len(opportunities),
            "opportunities": opportunities
        }, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Scan terminé. {len(opportunities)} opportunités trouvées.")
    print(f"📁 Résultat sauvegardé dans : {OUTPUT_FILE}")
    
    # Afficher le top 3
    print("\n🎯 TOP 3 OPPORTUNITÉS DU JOUR :\n")
    for i, opp in enumerate(opportunities[:3], 1):
        print(f"{i}. {opp['business_idea']['idea']} (Score: {opp['score']})")
        print(f"   Problème: {opp['problem']['problem']}")
        print(f"   Cible: {opp['business_idea']['target_customer']}")
        print()
