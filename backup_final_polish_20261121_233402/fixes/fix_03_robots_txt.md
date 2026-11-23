# IncuBrix robots.txt - Optimized for Search and AI Answer Engines

User-agent: *
Allow: /
Disallow: /api/
Disallow: /admin/
Disallow: /dashboard/
Disallow: /checkout/

# Explicit permissions for generative AI crawlers (AEO / GEO)
User-agent: GPTBot
Allow: /
Allow: /llms.txt
Allow: /llms-full.txt

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Google-Extended
Allow: /

# Sitemap Declarations
Sitemap: https://incubrix.com/sitemap.xml
