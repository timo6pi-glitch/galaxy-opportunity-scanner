def generate_business_idea(self, problem: Dict) -> Dict:
    """
    Génère une idée de business basée sur le problème
    Version améliorée - idée personnalisée selon le problème
    """
    problem_name = problem["problem"].lower()
    
    if "invoice" in problem_name or "payment" in problem_name:
        idea = {
            "idea": "Automated invoice reminder SaaS for freelancers",
            "target_customer": "Freelance developers and designers earning 3k-10k€/month",
            "price_point": "19€/month or 5% of recovered revenue",
            "mvp_features": [
                "CSV upload of invoices",
                "Automatic email reminders at J+1, J+7, J+14",
                "Weekly report of late payments"
            ],
            "estimated_market_size": "500k+ freelancers in EU/US"
        }
    
    elif "certification" in problem_name or "tracking" in problem_name:
        idea = {
            "idea": "Employee certification tracking platform",
            "target_customer": "HR managers and compliance officers in companies 50-500 employees",
            "price_point": "99€/month for unlimited certifications",
            "mvp_features": [
                "Google Sheets import",
                "Automated email reminders (J-30, J-7, J-1)",
                "Compliance dashboard for managers",
                "Auto-renewal workflow"
            ],
            "estimated_market_size": "100k+ companies in EU/US"
        }
    
    elif "google reviews" in problem_name or "reviews" in problem_name:
        idea = {
            "idea": "Automated Google Reviews request system for local businesses",
            "target_customer": "Plumbers, electricians, restaurants, salons (local services)",
            "price_point": "49€/month or 2€ per new review",
            "mvp_features": [
                "SMS/email automation after service",
                "Direct link to Google Reviews",
                "Review tracking dashboard",
                "Follow-up for non-responders"
            ],
            "estimated_market_size": "1M+ local businesses in EU/US"
        }
    
    elif "launching" in problem_name or "saas" in problem_name:
        idea = {
            "idea": "Launch accelerator for indie hackers",
            "target_customer": "Solo founders launching their first SaaS",
            "price_point": "199€ one-time or 29€/month",
            "mvp_features": [
                "Product Hunt launch checklist",
                "Pre-launch email sequence templates",
                "Early adopter finder tool",
                "Launch day analytics dashboard"
            ],
            "estimated_market_size": "50k+ indie hackers launching per year"
        }
    
    else:
        idea = {
            "idea": "Business automation audit + implementation",
            "target_customer": "Small business owners drowning in manual work",
            "price_point": "499€ audit + 99€/month implementation",
            "mvp_features": [
                "Process mapping workshop",
                "Automation roadmap (Zapier/Make)",
                "Implementation of top 3 automations",
                "Monthly optimization calls"
            ],
            "estimated_market_size": "10M+ small businesses in EU/US"
        }
    
    # Ajoute la référence au problème
    idea["problem_reference"] = problem
    
    return idea
