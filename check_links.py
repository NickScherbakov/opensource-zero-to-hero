#!/usr/bin/env python3
"""
Script to check all links in Markdown files for broken references
"""

import re
import os
import requests
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse
import sys

class LinkChecker:
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir)
        self.broken_links = []
        self.checked_urls = {}  # Cache for external URLs
        
    def find_md_files(self):
        """Find all Markdown files in the directory"""
        return list(self.root_dir.glob("**/*.md"))
    
    def extract_links(self, content):
        """Extract all links from Markdown content"""
        # Patterns for different link types
        patterns = [
            r'\[([^\]]*)\]\(([^)]+)\)',  # [text](url)
            r'!\[([^\]]*)\]\(([^)]+)\)',  # ![alt](image)
        ]
        
        links = []
        for pattern in patterns:
            matches = re.findall(pattern, content)
            for match in matches:
                text, url = match
                links.append({
                    'text': text,
                    'url': url,
                    'type': 'image' if pattern.startswith('!') else 'link'
                })
        
        return links
    
    def is_external_url(self, url):
        """Check if URL is external (http/https)"""
        return url.startswith(('http://', 'https://'))
    
    def is_anchor_link(self, url):
        """Check if URL is an anchor link (#...)"""
        return url.startswith('#')
    
    def check_internal_link(self, url, current_file):
        """Check if internal file/directory exists"""
        if self.is_anchor_link(url):
            return True  # Skip anchor links for now
            
        # Handle relative paths
        if url.startswith('/'):
            # Absolute path from root
            target_path = self.root_dir / url.lstrip('/')
        else:
            # Relative path from current file
            target_path = current_file.parent / url
        
        # Normalize path
        try:
            target_path = target_path.resolve()
        except (OSError, RuntimeError):
            return False
            
        return target_path.exists()
    
    def check_external_url(self, url):
        """Check if external URL is accessible"""
        if url in self.checked_urls:
            return self.checked_urls[url]
        
        try:
            # Add delay to be respectful
            time.sleep(0.5)
            
            response = requests.head(url, timeout=10, allow_redirects=True)
            is_valid = response.status_code < 400
            
            self.checked_urls[url] = is_valid
            return is_valid
            
        except requests.RequestException:
            try:
                # Try GET if HEAD fails
                response = requests.get(url, timeout=10, allow_redirects=True)
                is_valid = response.status_code < 400
                self.checked_urls[url] = is_valid
                return is_valid
            except requests.RequestException:
                self.checked_urls[url] = False
                return False
    
    def check_links_in_file(self, file_path):
        """Check all links in a single file"""
        print(f"Проверяем файл: {file_path.relative_to(self.root_dir)}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Ошибка чтения файла {file_path}: {e}")
            return
        
        links = self.extract_links(content)
        file_broken_links = []
        
        for link in links:
            url = link['url']
            
            if self.is_external_url(url):
                print(f"  Проверяем внешнюю ссылку: {url}")
                if not self.check_external_url(url):
                    file_broken_links.append({
                        'file': file_path,
                        'text': link['text'],
                        'url': url,
                        'type': 'external',
                        'error': 'URL недоступен'
                    })
            else:
                print(f"  Проверяем внутреннюю ссылку: {url}")
                if not self.check_internal_link(url, file_path):
                    file_broken_links.append({
                        'file': file_path,
                        'text': link['text'],
                        'url': url,
                        'type': 'internal',
                        'error': 'Файл или папка не найдена'
                    })
        
        self.broken_links.extend(file_broken_links)
        
        if file_broken_links:
            print(f"  ❌ Найдено {len(file_broken_links)} битых ссылок")
        else:
            print(f"  ✅ Все ссылки корректны")
    
    def run_check(self):
        """Run link check on all Markdown files"""
        md_files = self.find_md_files()
        
        print(f"Найдено {len(md_files)} Markdown файлов для проверки\n")
        
        for file_path in md_files:
            self.check_links_in_file(file_path)
            print()
        
        return self.broken_links
    
    def print_report(self):
        """Print final report of broken links"""
        if not self.broken_links:
            print("🎉 Битых ссылок не найдено!")
            return
        
        print(f"❌ Найдено {len(self.broken_links)} битых ссылок:\n")
        
        # Group by file
        by_file = {}
        for link in self.broken_links:
            file_path = link['file']
            if file_path not in by_file:
                by_file[file_path] = []
            by_file[file_path].append(link)
        
        for file_path, links in by_file.items():
            print(f"📄 {file_path.relative_to(self.root_dir)}:")
            for link in links:
                print(f"  • {link['type']}: [{link['text']}]({link['url']})")
                print(f"    Ошибка: {link['error']}")
            print()

def main():
    if len(sys.argv) > 1:
        root_dir = sys.argv[1]
    else:
        root_dir = "."
    
    checker = LinkChecker(root_dir)
    checker.run_check()
    checker.print_report()
    
    # Return exit code based on results
    sys.exit(1 if checker.broken_links else 0)

if __name__ == "__main__":
    main()