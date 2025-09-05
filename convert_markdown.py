#!/usr/bin/env python3
"""
Улучшенный скрипт для конвертации Markdown в HTML
Специально адаптированный для репозитория opensource-zero-to-hero
"""

import os
import sys
from pathlib import Path

# Проверяем наличие markdown
try:
    import markdown
except ImportError:
    print("❌ Ошибка: Библиотека 'markdown' не установлена")
    print("Установите её командой: pip install markdown")
    sys.exit(1)

# HTML шаблон с навигацией
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Open Source Competitive Advantage</title>
    <meta name="description" content="{description}">
    
    <!-- Стили для красивого отображения -->
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #fafafa;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1rem 0;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 20px rgba(0,0,0,0.1);
        }}
        
        .nav {{
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 2rem;
        }}
        
        .logo {{
            font-size: 1.2rem;
            font-weight: bold;
        }}
        
        .back-link {{
            color: white;
            text-decoration: none;
            font-weight: 600;
        }}
        
        .back-link:hover {{
            opacity: 0.8;
        }}
        
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            padding: 2rem;
        }}
        
        .content {{
            background: white;
            padding: 3rem;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        h1 {{
            color: #2d3748;
            font-size: 2.5rem;
            margin-bottom: 1.5rem;
            border-bottom: 3px solid #667eea;
            padding-bottom: 1rem;
        }}
        
        h2 {{
            color: #4a5568;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 0.5rem;
            margin: 2rem 0 1rem 0;
        }}
        
        h3 {{
            color: #667eea;
            margin: 1.5rem 0 0.5rem 0;
        }}
        
        h4 {{
            color: #4a5568;
            margin: 1rem 0 0.5rem 0;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1.5rem 0;
            background: white;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            border-radius: 8px;
            overflow: hidden;
        }}
        
        th, td {{
            border: 1px solid #e2e8f0;
            padding: 1rem;
            text-align: left;
        }}
        
        th {{
            background: #667eea;
            color: white;
            font-weight: 600;
            text-transform: uppercase;
            font-size: 0.9rem;
            letter-spacing: 0.5px;
        }}
        
        tr:nth-child(even) {{
            background: #f8fafc;
        }}
        
        tr:hover {{
            background: #edf2f7;
        }}
        
        blockquote {{
            border-left: 4px solid #667eea;
            margin: 1.5rem 0;
            padding: 1rem 1rem 1rem 2rem;
            background: #f8fafc;
            border-radius: 0 8px 8px 0;
            font-style: italic;
            color: #4a5568;
        }}
        
        code {{
            background: #f1f5f9;
            padding: 0.2rem 0.4rem;
            border-radius: 3px;
            font-family: 'Monaco', 'Consolas', 'Courier New', monospace;
            font-size: 0.9em;
            color: #e53e3e;
        }}
        
        pre {{
            background: #1a202c;
            color: #e2e8f0;
            padding: 1.5rem;
            border-radius: 8px;
            overflow-x: auto;
            margin: 1.5rem 0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }}
        
        pre code {{
            background: transparent;
            color: inherit;
            padding: 0;
        }}
        
        ul, ol {{
            margin: 1rem 0;
            padding-left: 2rem;
        }}
        
        li {{
            margin-bottom: 0.5rem;
        }}
        
        .metric-highlight {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 10px;
            margin: 2rem 0;
            text-align: center;
            font-weight: bold;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        }}
        
        .warning {{
            background: #fff5f5;
            border: 1px solid #fed7d7;
            border-left: 4px solid #f56565;
            padding: 1rem;
            border-radius: 5px;
            margin: 1.5rem 0;
        }}
        
        .info {{
            background: #ebf8ff;
            border: 1px solid #bee3f8;
            border-left: 4px solid #4299e1;
            padding: 1rem;
            border-radius: 5px;
            margin: 1.5rem 0;
        }}
        
        .footer {{
            text-align: center;
            margin-top: 3rem;
            padding: 2rem;
            background: #f8fafc;
            border-radius: 10px;
            color: #666;
        }}
        
        .footer a {{
            color: #667eea;
            text-decoration: none;
            margin: 0 1rem;
        }}
        
        .footer a:hover {{
            text-decoration: underline;
        }}
        
        /* Responsive design */
        @media (max-width: 768px) {{
            .container {{
                padding: 1rem;
            }}
            
            .content {{
                padding: 1.5rem;
            }}
            
            h1 {{
                font-size: 2rem;
            }}
            
            table {{
                font-size: 0.9rem;
            }}
            
            th, td {{
                padding: 0.5rem;
            }}
        }}
    </style>
</head>
<body>
    <header class="header">
        <nav class="nav">
            <div class="logo">🚀 Open Source Advantage</div>
            <a href="/opensource-zero-to-hero/" class="back-link">← Back to Website</a>
        </nav>
    </header>
    
    <div class="container">
        <div class="content">
            {content}
        </div>
        
        <div class="footer">
            <p>
                <a href="/opensource-zero-to-hero/">🏠 Homepage</a>
                <a href="https://github.com/NickScherbakov/opensource-zero-to-hero">📚 GitHub Repository</a>
                <a href="/opensource-zero-to-hero/docs/business-case.html">💼 Business Case</a>
                <a href="/opensource-zero-to-hero/docs/investor-guide.html">💰 Investor Guide</a>
            </p>
            <p style="margin-top: 1rem; font-size: 0.9rem;">
                © 2025 Open Source Competitive Advantage Project | 
                Licensed under <a href="/opensource-zero-to-hero/LICENSE">MIT & CC BY 4.0</a>
            </p>
        </div>
    </div>
</body>
</html>"""

def extract_title_and_description(content):
    """Извлекает заголовок и описание из Markdown"""
    lines = content.split('\n')
    title = "Document"
    description = "Open source competitive advantage research"
    
    for i, line in enumerate(lines):
        if line.startswith('# '):
            title = line[2:].strip()
            # Ищем описание в следующих строках
            for j in range(i+1, min(i+5, len(lines))):
                if lines[j].strip() and not lines[j].startswith('#'):
                    description = lines[j].strip()[:150] + "..."
                    break
            break
    
    return title, description

def process_markdown_file(input_path, output_path):
    """Конвертирует один Markdown файл в HTML"""
    try:
        print(f"📄 Обрабатываю: {input_path}")
        
        with open(input_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Извлекаем заголовок и описание
        title, description = extract_title_and_description(md_content)
        
        # Настраиваем markdown процессор
        md = markdown.Markdown(extensions=[
            'tables',
            'fenced_code',
            'codehilite',
            'toc',
            'attr_list',
            'def_list',
            'footnotes',
            'admonition'
        ])
        
        # Конвертируем в HTML
        html_content = md.convert(md_content)
        
        # Применяем шаблон
        final_html = HTML_TEMPLATE.format(
            title=title,
            description=description,
            content=html_content
        )
        
        # Создаем папку если нужно
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Записываем HTML файл
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_html)
        
        print(f"✅ Создан: {output_path}")
        
    except Exception as e:
        print(f"❌ Ошибка при обработке {input_path}: {e}")

def main():
    """Основная функция - конвертирует все файлы"""
    
    print("🚀 Запуск конвертера Markdown → HTML")
    print("=" * 50)
    
    # Определяем файлы для конвертации
    files_to_convert = [
        # Основные документы
        ("docs/business-case/business-case-analysis.md", "docs/business-case.html"),
        ("docs/investor-guide/investor-dd-framework.md", "docs/investor-guide.html"),
        ("docs/investor-guide/due-diligence-checklist.md", "docs/due-diligence.html"),
        ("docs/investor-guide/valuation-models.md", "docs/valuation-models.html"),
        
        # Кейс стади
        ("docs/case-studies/github-story.md", "docs/github-case-study.html"),
        ("docs/case-studies/huggingface-journey.md", "docs/huggingface-case-study.html"),
        ("docs/case-studies/redis-monetization.md", "docs/redis-case-study.html"),
        
        # Исследования
        ("docs/market-research/2025-funding-report.md", "docs/funding-report.html"),
        
        # Служебные страницы
        ("CONTRIBUTING.md", "contributing.html"),
        ("CODE_OF_CONDUCT.md", "code-of-conduct.html"),
        
        # README файлы в папках
        ("docs/README.md", "docs/index.html"),
        ("data/README.md", "data/index.html"),
        ("tools/README.md", "tools/index.html"),
        ("visuals/README.md", "visuals/index.html"),
        ("community/README.md", "community/index.html"),
    ]
    
    base_path = Path(".")
    converted_count = 0
    
    for input_file, output_file in files_to_convert:
        input_path = base_path / input_file
        output_path = base_path / output_file
        
        if input_path.exists():
            process_markdown_file(input_path, output_path)
            converted_count += 1
        else:
            print(f"⚠️  Файл не найден: {input_file}")
    
    print("=" * 50)
    print(f"🎉 Конвертация завершена!")
    print(f"📊 Обработано файлов: {converted_count}")
    print(f"📁 HTML файлы созданы в соответствующих папках")
    
    # Создаем простой sitemap
    create_sitemap(files_to_convert)

def create_sitemap(files):
    """Создает простой sitemap.xml"""
    base_url = "https://nickscherbakov.github.io/opensource-zero-to-hero"
    
    sitemap_content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>{}/</loc>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>'''.format(base_url)
    
    for _, output_file in files:
        if output_file.endswith('.html'):
            sitemap_content += '''
    <url>
        <loc>{}/{}</loc>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>'''.format(base_url, output_file)
    
    sitemap_content += '''
</urlset>'''
    
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap_content)
    
    print("✅ Создан sitemap.xml")

if __name__ == "__main__":
    main()
