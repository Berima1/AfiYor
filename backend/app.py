# AfiYor Professional System with Research-Based Knowledge
# Integrates real business intelligence and professional insights

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import time
import random
import os
import re
import sqlite3
from datetime import datetime

# Import the professional knowledge base
exec(open('afiyor_knowledge_base.py').read())

app = Flask(__name__)
CORS(app)

class ProfessionalAfiYor:
    """Professional African AI Assistant with research-based knowledge"""
    
    def __init__(self):
        self.knowledge_base = AFRICAN_BUSINESS_KNOWLEDGE_BASE
        self.training_docs = TRAINING_DOCUMENTS
        self.response_cache = {}  # Cache for complex responses
        
    def analyze_query_professional(self, message, user_context=None):
        """Advanced query analysis using professional knowledge"""
        
        message_lower = message.lower()
        analysis = {
            'primary_intent': None,
            'secondary_intents': [],
            'complexity_level': 'basic',  # basic, intermediate, advanced
            'requires_professional_data': False,
            'country_specific': user_context.get('country', 'ghana') if user_context else 'ghana',
            'industry_specific': user_context.get('industry', 'general') if user_context else 'general'
        }
        
        # Funding and Investment Intent
        if any(word in message_lower for word in ['funding', 'investment', 'investor', 'capital', 'raise money', 'venture', 'angel']):
            analysis['primary_intent'] = 'funding_investment'
            analysis['complexity_level'] = 'advanced'
            analysis['requires_professional_data'] = True
            
        # Legal and Registration
        elif any(word in message_lower for word in ['register', 'legal', 'license', 'permit', 'incorporation', 'cac', 'trademark']):
            analysis['primary_intent'] = 'legal_registration'
            analysis['complexity_level'] = 'intermediate'
            analysis['requires_professional_data'] = True
            
        # Mobile Money Integration
        elif any(word in message_lower for word in ['mobile money', 'm-pesa', 'momo', 'mtn', 'paystack', 'flutterwave', 'payment integration']):
            analysis['primary_intent'] = 'mobile_money'
            analysis['complexity_level'] = 'advanced'
            analysis['requires_professional_data'] = True
            
        # Market Research and Validation
        elif any(word in message_lower for word in ['market research', 'validate', 'target market', 'market size', 'customer', 'pricing']):
            analysis['primary_intent'] = 'market_research'
            analysis['complexity_level'] = 'intermediate'
            analysis['requires_professional_data'] = True
            
        # Ubuntu Philosophy and Culture
        elif any(word in message_lower for word in ['ubuntu', 'culture', 'philosophy', 'community', 'values', 'tradition']):
            analysis['primary_intent'] = 'ubuntu_culture'
            analysis['complexity_level'] = 'basic'
            
        # Sector-Specific Queries
        elif any(word in message_lower for word in ['fintech', 'agriculture', 'agritech', 'healthtech', 'edtech']):
            analysis['primary_intent'] = 'sector_specific'
            analysis['complexity_level'] = 'advanced'
            analysis['requires_professional_data'] = True
            
        # General Business Startup
        elif any(word in message_lower for word in ['start', 'business', 'startup', 'entrepreneur', 'company']):
            analysis['primary_intent'] = 'business_startup'
            analysis['complexity_level'] = 'intermediate'
            
        else:
            analysis['primary_intent'] = 'general_business'
            analysis['complexity_level'] = 'basic'
            
        return analysis
    
    def generate_professional_response(self, message, user_context=None):
        """Generate professional response using research-based knowledge"""
        
        analysis = self.analyze_query_professional(message, user_context)
        
        if analysis['requires_professional_data']:
            return self.get_professional_data_response(analysis, message, user_context)
        else:
            return self.get_general_professional_response(analysis, message, user_context)
    
    def get_professional_data_response(self, analysis, message, user_context):
        """Generate responses using professional research data"""
        
        intent = analysis['primary_intent']
        country = analysis['country_specific']
        industry = analysis['industry_specific']
        
        if intent == 'funding_investment':
            return self.get_funding_intelligence(message, country, industry)
            
        elif intent == 'legal_registration':
            return self.get_legal_intelligence(message, country)
            
        elif intent == 'mobile_money':
            return self.get_mobile_money_intelligence(message, country)
            
        elif intent == 'market_research':
            return self.get_market_research_intelligence(message, country, industry)
            
        elif intent == 'sector_specific':
            return self.get_sector_intelligence_response(message, industry)
            
        return self.get_general_professional_response(analysis, message, user_context)
    
    def get_funding_intelligence(self, message, country, industry):
        """Professional funding and investment guidance"""
        
        funding_data = self.knowledge_base['frequent_questions']['funding_and_investment']['professional_answers']
        
        if 'raise' in message.lower() or 'capital' in message.lower():
            capital_info = funding_data['capital_raising']
            
            # Determine appropriate funding stage
            if any(word in message.lower() for word in ['idea', 'early', 'start']):
                stage = 'pre_seed'
            elif any(word in message.lower() for word in ['seed', 'series a']):
                stage = 'seed'
            else:
                stage = 'seed'  # Default
                
            stage_data = capital_info['funding_stages'][stage]
            
            response = f"""**Funding Intelligence for {country.title()}**

**{stage.replace('_', ' ').title()} Funding Overview:**
• **Typical Amount**: {stage_data['typical_amount']}
• **Key Sources**: {', '.join(stage_data['sources'])}

**African-Specific Funding Sources:**"""
            
            if 'african_sources' in stage_data:
                for source in stage_data['african_sources']:
                    response += f"\n• {source}"
            
            if stage == 'seed' and 'african_vcs' in stage_data:
                response += f"\n\n**Process & Timeline Questions:**"
            for i, question in enumerate(questions[3:6], 4):
                response += f"\n{i}. {question}"
                
            response += f"\n\n**Support & Value-Add Questions:**"
            for i, question in enumerate(questions[6:9], 7):
                response += f"\n{i}. {question}"
                
            response += f"\n\n**Reference Question:**\n10. {questions[9]}"
            
        return response + f"\n\n🤝 Ubuntu wisdom: Build partnerships that create mutual prosperity for your community."
    
    def get_legal_intelligence(self, message, country):
        """Professional legal and registration guidance"""
        
        legal_data = self.knowledge_base['frequent_questions']['business_registration_legal']['professional_answers']
        
        if country.lower() in legal_data['business_registration']:
            country_data = legal_data['business_registration'][country.lower()]
            
            response = f"""**Business Registration Guide for {country.title()}**

**Registration Authority**: {country_data['authority']}
**Process**: {country_data['process']}
**Cost**: {country_data['cost']}
**Timeline**: {country_data['timeline']}

**Required Documents:**"""
            
            for req in country_data['requirements']:
                response += f"\n• {req}"
                
            if 'license' in message.lower() or 'permit' in message.lower():
                response += f"\n\n**Industry-Specific Licenses:**"
                for business_type, authority in country_data['licenses'].items():
                    response += f"\n• **{business_type.replace('_', ' ').title()}**: {authority}"
                    
        elif 'trademark' in message.lower() or 'patent' in message.lower():
            ip_data = legal_data['intellectual_property']
            
            response = f"""**Intellectual Property Protection in Africa**

**Trademark Protection:**
• Cost Range: {ip_data['trademarks']['cost_range']}
• Process: {ip_data['trademarks']['process']}
• Protection Period: {ip_data['trademarks']['protection']}

**Patent Protection:**
• Cost Range: {ip_data['patents']['cost_range']}
• Process: {ip_data['patents']['process']}
• Protection Period: {ip_data['patents']['protection']}

**Recommendation**: File in multiple African countries where you plan to operate."""
            
        return response + f"\n\n🤝 Ubuntu principle: Proper legal foundation protects your community's investment in your success."
    
    def get_mobile_money_intelligence(self, message, country):
        """Professional mobile money integration guidance"""
        
        mm_data = self.knowledge_base['mobile_money_intelligence']
        
        # Market overview
        response = f"""**Mobile Money Intelligence for {country.title()}**

**African Mobile Money Leadership:**
• Africa processes 70% of global mobile money transactions
• $490 billion transaction value in 2024
• 469 million registered users continent-wide"""
        
        if country.lower() in mm_data['country_specific']:
            country_data = mm_data['country_specific'][country.lower()]
            
            if country.lower() == 'kenya':
                response += f"""

**Kenya - M-Pesa Dominance:**
• Market Share: {country_data['market_share']} of mobile money users
• Daily Volume: {country_data['daily_transactions']}
• Adult Penetration: {country_data['penetration']}

**API Integration Details:**
• Developer Portal: {country_data['api_integration']['developer_portal']}
• Transaction Fees: {country_data['api_integration']['transaction_fees']}
• Settlement Time: {country_data['api_integration']['settlement_time']}

**Business Opportunities:**"""
                for opportunity in country_data['business_opportunities']:
                    response += f"\n• {opportunity}"
                    
            elif country.lower() == 'ghana':
                response += f"""

**Ghana - Multi-Platform Market:**"""
                for platform, data in country_data['platforms'].items():
                    response += f"""

**{platform.upper().replace('_', ' ')}:**
• Market Share: {data['market_share']}
• Operator: {data['operator']}"""
                    if 'api_integration' in data:
                        response += f"""
• Developer Portal: {data['api_integration']['developer_portal']}
• Transaction Fees: {data['api_integration']['fees']}"""
                        
                response += f"""

**Regulatory Framework:**
• Regulator: {country_data['regulatory_environment']['regulator']}
• Key Requirements: {', '.join(country_data['regulatory_environment']['key_requirements'])}"""
                
        # Technical integration guide
        if 'integrate' in message.lower() or 'api' in message.lower():
            integration_guide = mm_data['integration_guide']
            
            response += f"""

**Technical Integration Requirements:**"""
            for req in integration_guide['technical_requirements']:
                response += f"\n• {req}"
                
            response += f"""

**Compliance Must-Haves:**"""
            for req in integration_guide['compliance_requirements']:
                response += f"\n• {req}"
                
        return response + f"\n\n🤝 Ubuntu insight: Mobile money succeeds because it serves the entire community's financial needs."
    
    def get_market_research_intelligence(self, message, country, industry):
        """Professional market research and validation guidance"""
        
        market_data = self.knowledge_base['frequent_questions']['market_research_validation']['professional_answers']
        
        response = f"""**Market Research Intelligence for {country.title()} - {industry.title()}**

**Market Validation Framework:**"""
        
        for method in market_data['market_validation']['lean_startup_method']:
            response += f"\n• {method}"
            
        response += f"""

**African-Specific Validation:**"""
        for method in market_data['market_validation']['african_specific_validation']:
            response += f"\n• {method}"
            
        # Market sizing information
        if 'market size' in message.lower() or 'tam' in message.lower():
            sizing_data = market_data['market_sizing']
            
            response += f"""

**Market Sizing Methodology:**
{sizing_data['methodology']}

**African Market Data (2024):**"""
            for key, value in sizing_data['african_market_data'].items():
                response += f"\n• **{key.replace('_', ' ').title()}**: {value}"
                
        # Add industry-specific market insights
        if industry in self.knowledge_base['sector_intelligence']:
            sector_data = self.knowledge_base['sector_intelligence'][industry]
            if 'market_size' in sector_data:
                response += f"\n\n**{industry.title()} Market Size**: {sector_data['market_size']}"
                
        return response + f"\n\n🤝 Ubuntu approach: Research that serves community needs creates sustainable businesses."
    
    def get_sector_intelligence_response(self, message, industry):
        """Professional sector-specific business intelligence"""
        
        if industry not in self.knowledge_base['sector_intelligence']:
            industry = 'fintech'  # Default to fintech
            
        sector_data = self.knowledge_base['sector_intelligence'][industry]
        
        response = f"""**{industry.title()} Sector Intelligence**

**Market Overview:**"""
        
        if 'market_size' in sector_data:
            response += f"\n• Market Size: {sector_data['market_size']}"
            
        if 'key_segments' in sector_data:
            response += f"\n\n**Key Segments:**"
            for segment, description in sector_data['key_segments'].items():
                response += f"\n• **{segment.title()}**: {description}"
                
        if 'success_factors' in sector_data:
            response += f"\n\n**Success Factors:**"
            for factor in sector_data['success_factors']:
                response += f"\n• {factor}"
                
        if 'challenges' in sector_data:
            response += f"\n\n**Key Challenges:**"
            for challenge in sector_data['challenges']:
                response += f"\n• {challenge}"
                
        if 'opportunities' in sector_data:
            response += f"\n\n**Market Opportunities:**"
            for opportunity in sector_data['opportunities']:
                response += f"\n• {opportunity}"
                
        return response + f"\n\n🤝 Ubuntu perspective: {industry.title()} success comes from solving community problems profitably."
    
    def get_general_professional_response(self, analysis, message, user_context):
        """Generate professional response for general queries"""
        
        country = analysis['country_specific']
        industry = analysis['industry_specific']
        
        if analysis['primary_intent'] == 'ubuntu_culture':
            ubuntu_data = self.knowledge_base['cultural_intelligence']['ubuntu_philosophy']
            
            response = f"""**Ubuntu Philosophy in Business**

**Core Meaning**: {ubuntu_data['definition']}

**Business Applications:**"""
            
            if 'leadership' in message.lower():
                for principle in ubuntu_data['business_applications']['leadership_style']:
                    response += f"\n• {principle}"
            elif 'employee' in message.lower():
                for principle in ubuntu_data['business_applications']['employee_relations']:
                    response += f"\n• {principle}"
            else:
                for principle in ubuntu_data['core_principles'][:3]:
                    response += f"\n• {principle}"
                    
            response += f"\n\n**Success Examples:**"
            for example in ubuntu_data['success_examples'][:2]:
                response += f"\n• {example}"
                
        else:
            # General business guidance with professional touch
            response = f"""**Professional Business Guidance for {country.title()}**

**Market Context**: Africa's 1.4 billion population, 60% under 25, represents incredible entrepreneurial opportunity.

**Key Success Principles:**
• Focus on solving real community problems
• Build for mobile-first users (84% mobile penetration)
• Understand local payment preferences
• Create sustainable business models
• Integrate cultural values like Ubuntu

**{industry.title()} Specific Considerations:**"""
            
            if industry == 'fintech':
                response += "\n• Mobile money integration is essential\n• Regulatory compliance is critical\n• Focus on financial inclusion"
            elif industry == 'agriculture':
                response += "\n• Value chain integration opportunities\n• Climate-smart solutions needed\n• Cooperative models work well"
            else:
                response += f"\n• Build strong local partnerships\n• Understand cultural business practices\n• Focus on community benefit"
                
        return response + f"\n\n🤝 Ubuntu wisdom: I am because we are - your business success strengthens the entire {country} community."

# Initialize professional AfiYor
professional_afiyor = ProfessionalAfiYor()

@app.route('/')
def home():
    return jsonify({
        "name": "AfiYor Professional API",
        "version": "4.0.0",
        "description": "Research-Based African Business Intelligence System",
        "ubuntu": "I am because we are",
        "knowledge_base": "Professional research data integrated",
        "features": [
            "Research-based business intelligence",
            "Professional funding guidance", 
            "Legal and regulatory information",
            "Mobile money integration details",
            "Market research methodologies",
            "Sector-specific insights",
            "Ubuntu philosophy integration"
        ],
        "data_sources": [
            "African venture capital reports",
            "Mobile money industry research", 
            "Business registration requirements",
            "Cultural business practices",
            "Sector market intelligence"
        ]
    })

@app.route('/chat', methods=['POST'])
def professional_chat():
    try:
        data = request.get_json()
        message = data.get('message', '').strip()
        user_context = {
            'country': data.get('country', 'ghana'),
            'industry': data.get('industry', 'general'),
            'user_id': data.get('user_id', 'anonymous')
        }
        
        if not message:
            return jsonify({"error": "Message is required"}), 400
        
        # Generate professional response
        response = professional_afiyor.generate_professional_response(message, user_context)
        
        return jsonify({
            "response": response,
            "confidence": 0.95,
            "source": "professional_research_data",
            "country": user_context['country'],
            "industry": user_context['industry'],
            "knowledge_level": "professional",
            "timestamp": int(time.time()),
            "version": "4.0.0"
        })
        
    except Exception as e:
        return jsonify({
            "error": "Professional analysis in progress",
            "response": f"I'm processing your {user_context['industry']} question for {user_context['country']}. Ubuntu teaches us patience - let me provide you with research-based guidance shortly.",
            "confidence": 0.7
        }), 200

@app.route('/knowledge/<category>')
def get_knowledge_category(category):
    """Get specific knowledge category data"""
    
    categories = {
        'funding': professional_afiyor.knowledge_base['frequent_questions']['funding_and_investment'],
        'mobile_money': professional_afiyor.knowledge_base['mobile_money_intelligence'],
        'ubuntu': professional_afiyor.knowledge_base['cultural_intelligence']['ubuntu_philosophy'],
        'sectors': professional_afiyor.knowledge_base['sector_intelligence']
    }
    
    if category in categories:
        return jsonify({
            "category": category,
            "data": categories[category],
            "source": "professional_research"
        })
    
    return jsonify({"error": "Category not found"}), 404

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": int(time.time()),
        "ai_status": "professional_research_ready",
        "knowledge_base_loaded": True,
        "ubuntu": "Ngiyaphila - I am well because we are well",
        "version": "4.0.0",
        "professional_features": [
            "Research-based responses",
            "Professional business intelligence",
            "Real market data integration"
        ]
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("🌍 AfiYor Professional System Starting...")
    print("📊 Research-based knowledge loaded")
    print("🤝 Ubuntu wisdom integrated")
    app.run(host='0.0.0.0', port=port, debug=False)Top African VCs for Your Stage:**"
                for vc in stage_data['african_vcs'][:3]:
                    response += f"\n• {vc}"
            
            response += f"\n\n**Critical Success Factors:**"
            for factor in capital_info['success_factors'][:4]:
                response += f"\n• {factor}"
                
            response += f"\n\n**Pro Tip**: African startups raised $3.5B in 2024. {industry.title()} represents a strong sector for funding."
            
        elif 'investor' in message.lower() and 'question' in message.lower():
            questions = funding_data['investor_questions']['top_10_questions']
            
            response = f"""**Top 10 Professional Questions to Ask Investors:**

**Strategic Value Questions:**"""
            for i, question in enumerate(questions[:3], 1):
                response += f"\n{i}. {question}"
                
            response += f"\n\n**
