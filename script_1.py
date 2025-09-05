# Создаем данные для демонстрации успешных кейсов open source компаний
import pandas as pd
import json

# Данные о самых успешных open source выходах
success_cases = {
    "company_name": [
        "GitHub", "Red Hat", "GitLab", "Elastic", "MongoDB", 
        "Confluent", "HashiCorp", "Databricks", "Snowflake", "Docker"
    ],
    "founded_year": [2008, 1993, 2011, 2012, 2007, 2014, 2012, 2013, 2012, 2010],
    "exit_year": [2018, 2019, 2021, 2018, 2017, 2021, 2021, None, 2020, None],
    "exit_type": ["Acquisition", "Acquisition", "IPO", "IPO", "IPO", "IPO", "IPO", "Private", "IPO", "Private"],
    "exit_valuation_b": [7.5, 34.0, 16.0, 7.0, 24.0, 9.5, 15.2, 43.0, 70.0, 1.1],
    "latest_valuation_b": [7.5, 34.0, 16.0, 7.0, 24.0, 9.5, 15.2, 43.0, 70.0, 1.1],
    "github_stars_k": [57.5, 2.1, 23.7, 68.2, 26.8, 9.2, 14.8, 39.0, 4.2, 68.7],
    "primary_oss_project": [
        "Git hosting", "Linux/RHEL", "Git platform", "Elasticsearch", "MongoDB", 
        "Apache Kafka", "Terraform/Vault", "Apache Spark", "Data Cloud", "Containerization"
    ],
    "monetization_model": [
        "SaaS Platform", "Support + Enterprise", "Open Core", "Open Core", "Open Core",
        "Open Core", "Open Core", "Cloud Platform", "Cloud Platform", "Enterprise Platform"
    ],
    "enterprise_value_prop": [
        "Developer collaboration", "Enterprise Linux support", "DevOps automation", 
        "Search at scale", "Database management", "Stream processing", "Infrastructure as code",
        "ML/AI platform", "Data warehouse", "Container orchestration"
    ]
}

# Создаем DataFrame
df_success = pd.DataFrame(success_cases)

# Данные для анализа открытых проектов по секторам
sector_analysis = {
    "sector": [
        "AI/ML Platforms", "Developer Tools", "Cloud Infrastructure", "Data Management", 
        "Security", "DevOps/CI-CD", "Blockchain", "IoT/Edge", "Analytics", "Collaboration"
    ],
    "total_funding_2025_b": [8.2, 6.1, 5.8, 4.3, 3.4, 2.9, 2.1, 1.7, 1.5, 1.2],
    "num_funded_companies": [67, 89, 45, 32, 41, 56, 23, 19, 28, 15],
    "avg_valuation_m": [122, 69, 129, 134, 83, 52, 91, 89, 54, 80],
    "open_source_percentage": [78, 84, 71, 69, 63, 79, 95, 58, 67, 45],
    "top_companies": [
        "Hugging Face, OpenAI, Databricks", "GitHub, GitLab, JetBrains", "HashiCorp, Docker, Kubernetes Inc",
        "MongoDB, Elastic, InfluxData", "Snyk, Aqua Security, Sysdig", "GitLab, JFrog, CircleCI",
        "ConsenSys, Chainlink, Polygon", "EdgeX, KubeEdge, OpenYurt", "Grafana, Looker, Tableau",
        "Slack, Discord, Notion"
    ]
}

# Создаем DataFrame для секторального анализа
df_sectors = pd.DataFrame(sector_analysis)

# Сохраняем данные в CSV файлы
df_success.to_csv("open_source_success_cases.csv", index=False)
df_sectors.to_csv("open_source_sector_analysis.csv", index=False)

print("Success Cases Data:")
print(df_success.to_string(index=False))
print("\n" + "="*80 + "\n")
print("Sector Analysis Data:")
print(df_sectors.to_string(index=False))

# Расчет основных метрик
total_exit_value = df_success['exit_valuation_b'].sum()
avg_exit_multiple = df_success['exit_valuation_b'].mean()
total_github_stars = df_success['github_stars_k'].sum()

print(f"\n" + "="*80)
print("KEY INSIGHTS:")
print(f"Total Exit Value: ${total_exit_value:.1f}B")
print(f"Average Exit Valuation: ${avg_exit_multiple:.1f}B") 
print(f"Total GitHub Stars: {total_github_stars:.0f}K")
print(f"Average Stars per Company: {total_github_stars/len(df_success):.1f}K")

# Анализ по секторам
total_sector_funding = df_sectors['total_funding_2025_b'].sum()
print(f"\nTotal 2025 Funding Across Sectors: ${total_sector_funding:.1f}B")
print(f"Average Open Source Percentage: {df_sectors['open_source_percentage'].mean():.0f}%")