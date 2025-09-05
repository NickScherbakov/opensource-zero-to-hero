# Создаем структуру данных для репозитория "Open Source Competitive Advantage"
import json

# Основная структура репозитория
repo_structure = {
    "repository_name": "open-source-competitive-advantage",
    "tagline": "🚀 Open Source as Competitive Advantage: A Data-Driven Guide for Startups & Investors",
    "description": "Comprehensive research repository demonstrating why open source is the ultimate competitive advantage for modern businesses. From market data to investor perspectives.",
    
    "folder_structure": {
        "/": ["README.md", "LICENSE", ".gitignore", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md"],
        "/docs/": [
            "business-case/",
            "market-research/", 
            "investor-guide/",
            "case-studies/",
            "methodology/"
        ],
        "/data/": [
            "market-analysis/",
            "funding-rounds/",
            "performance-metrics/",
            "surveys/"
        ],
        "/visuals/": [
            "infographics/",
            "charts/", 
            "presentations/",
            "logos/"
        ],
        "/tools/": [
            "calculators/",
            "templates/",
            "scripts/"
        ],
        "/community/": [
            "contributors/",
            "discussions/",
            "events/"
        ]
    },
    
    "key_sections": [
        {
            "name": "The Business Case",
            "description": "Quantitative evidence why open source drives competitive advantage",
            "files": ["roi-analysis.md", "cost-savings.md", "speed-to-market.md"]
        },
        {
            "name": "Market Intelligence", 
            "description": "Latest data on open source market trends and investment flows",
            "files": ["2025-funding-report.md", "unicorn-analysis.md", "exit-strategies.md"]
        },
        {
            "name": "Investor Playbook",
            "description": "Guide for VCs evaluating open source startups",
            "files": ["due-diligence-checklist.md", "valuation-models.md", "portfolio-analysis.md"]
        },
        {
            "name": "Success Stories",
            "description": "Real case studies of open source companies that achieved massive success",
            "files": ["github-story.md", "huggingface-journey.md", "redis-monetization.md"]
        }
    ],
    
    "target_audience": [
        "🎯 Startup founders considering open source strategy",
        "💰 Venture capitalists evaluating OS investments", 
        "👩‍💻 Developers building community-driven projects",
        "📊 Business analysts researching market trends",
        "🏢 Enterprise decision makers"
    ],
    
    "value_propositions": [
        "📈 7x higher IPO valuations for open source companies",
        "⚡ 50% faster time-to-market through community contributions", 
        "💸 80% reduction in customer acquisition costs",
        "🔒 Enhanced security through peer review",
        "🌍 Global talent pool access",
        "🚀 Built-in marketing through developer adoption"
    ]
}

print("Repository Structure Created:")
print(json.dumps(repo_structure, indent=2, ensure_ascii=False))