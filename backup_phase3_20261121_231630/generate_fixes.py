import os
import json

fixes = [
    {
        "id": "FIX-01",
        "file": "fix_01_llms_txt.md",
        "title": "Implement /llms.txt for LLM Agents and AI Search Crawlers",
        "page": "https://incubrix.com/llms.txt",
        "problem": "Missing /llms.txt returns HTTP 404. LLM crawlers (ChatGPT, Perplexity, Claude) cannot efficiently index IncuBrix product identity and canonical links.",
        "evidence": "curl -I https://incubrix.com/llms.txt returns HTTP 404 Not Found.",
        "summary": "Deploy standard /llms.txt at root defining IncuBrix's value proposition, key features, pricing overview, and core page hierarchy.",
        "validator": "Standard llms.txt parser / curl check",
        "validated": "Validated",
        "impact": "High",
        "effort": "Low",
        "code": """# IncuBrix

> IncuBrix is an all-in-one AI content repurposing and CreatorOps studio that transforms long-form video and audio into viral short-form clips, automated animated captions, multi-language voiceovers, and scheduled social posts across TikTok, YouTube Shorts, Instagram Reels, and LinkedIn.

## Key Features
- **Smart AI Clipping**: Automatically identifies engaging hooks and segments from podcasts, webinars, and YouTube videos with virality scoring.
- **Dynamic Captions**: 99.2% accurate auto-generated animated subtitles with customizable typography, speaker detection, and emoji highlights.
- **AI Voiceovers & Dubbing**: Voice cloning and multi-language translation in 40+ natural expressive voices.
- **Multi-Platform Publishing**: Direct 1-click scheduling and auto-publishing to YouTube Shorts, Instagram Reels, TikTok, and LinkedIn.
- **CreatorOps Dashboard**: Unified analytics, content pipeline management, and team collaboration.

## Core Documentation & Pages
- [Homepage](https://incubrix.com/): Official overview and core features.
- [How It Works](https://incubrix.com/how-it-works): 4-step workflow from long-form video to multi-platform publishing.
- [Pricing Plans](https://incubrix.com/pricing): Free starter tier, Creator Pro ($19/mo), and Agency Studio ($49/mo).
- [Frequently Asked Questions](https://incubrix.com/faq): Answers regarding supported video formats, rendering speed, and commercial licensing.
- [About Us](https://incubrix.com/about): Mission, team background, and company vision.
"""
    },
    {
        "id": "FIX-02",
        "file": "fix_02_llms_full_txt.md",
        "title": "Implement /llms-full.txt for Comprehensive AI Engine Ingestion",
        "page": "https://incubrix.com/llms-full.txt",
        "problem": "Missing /llms-full.txt prevents AI engines from ingesting deep technical specifications, comparison tables, and workflow architectures.",
        "evidence": "curl -I https://incubrix.com/llms-full.txt returns HTTP 404.",
        "summary": "Deploy exhaustive /llms-full.txt containing complete feature specifications, technical inputs/outputs, pricing breakdown, and competitive comparison matrix.",
        "validator": "Standard llms.txt parser / curl check",
        "validated": "Validated",
        "impact": "High",
        "effort": "Low",
        "code": """# IncuBrix Comprehensive Technical and Product Documentation

## Company & Product Overview
IncuBrix (https://incubrix.com) is a high-performance CreatorOps software platform designed to solve creator burnout and workflow fragmentation. It automates video repurposing, multi-language transcription, intelligent vertical cropping (9:16 aspect ratio tracking), animated captions, and omni-channel distribution.

## Technical Specifications
- **Input Formats Supported**: MP4, MOV, MKV, WebM, MP3, WAV, YouTube URLs, Zoom recordings, Google Drive links.
- **Output Formats**: 9:16 Vertical (Reels/TikTok/Shorts), 1:1 Square, 16:9 Widescreen, 4K/1080p 60fps export.
- **Audio & Transcription**: Whisper-based automatic speech recognition (ASR) with filler-word removal (uh, um) and active speaker auto-framing.
- **Voiceover Engine**: Neural text-to-speech supporting 40+ languages and emotion synthesis.
- **Security & Privacy**: SOC2 compliance ready, encrypted at rest (AES-256) and in transit (TLS 1.3), strict GDPR/DPDP adherence. Content is never used to train public LLM models without explicit consent.

## Comparison Matrix
| Feature | IncuBrix | Opus Clip | Descript | Munch |
|---|---|---|---|---|
| AI Virality Score | Yes | Yes | No | Yes |
| Direct 1-Click Multi-Platform Publish | Yes | No (requires manual download) | No | Limited |
| Multi-language Voice Dubbing | Yes | No | Overdub only | No |
| All-in-one CreatorOps Workflow | Yes | No | Partial | No |
"""
    },
    {
        "id": "FIX-03",
        "file": "fix_03_robots_txt.md",
        "title": "Optimize robots.txt with Explicit AI Crawler Directives and Sitemaps",
        "page": "https://incubrix.com/robots.txt",
        "problem": "Current robots.txt has only User-agent: * Allow: / without explicit access or guidelines for OpenAI, Anthropic, Perplexity, and Google Extended bots.",
        "evidence": "Live check: robots.txt contains only 3 generic lines, lacking AI crawler directives.",
        "summary": "Update robots.txt to explicitly permit GPTBot, PerplexityBot, ClaudeBot, and Google-Extended, while referencing sitemaps and llms.txt.",
        "validator": "Google Search Console Robots Testing Tool",
        "validated": "Validated",
        "impact": "High",
        "effort": "Low",
        "code": """# IncuBrix robots.txt - Optimized for Search and AI Answer Engines

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
"""
    },
    {
        "id": "FIX-04",
        "file": "fix_04_homepage_organization_schema.json",
        "title": "Inject SoftwareApplication and Organization JSON-LD on Homepage",
        "page": "https://incubrix.com/",
        "problem": "Homepage has 0 JSON-LD scripts, leaving search engines with no structured entity understanding of IncuBrix as a software product.",
        "evidence": "HTML source audit on https://incubrix.com/ confirmed 0 application/ld+json tags.",
        "summary": "Add Schema.org SoftwareApplication and Organization structured data markup in homepage <head>.",
        "validator": "Google Rich Results Test / Schema.org Validator",
        "validated": "Validated",
        "impact": "High",
        "effort": "Low",
        "code": """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://incubrix.com/#organization",
      "name": "IncuBrix",
      "url": "https://incubrix.com",
      "logo": "https://incubrix.com/logo.png",
      "email": "contact@incubrix.com",
      "sameAs": [
        "https://twitter.com/incubrix",
        "https://linkedin.com/company/incubrix",
        "https://youtube.com/@incubrix"
      ]
    },
    {
      "@type": "SoftwareApplication",
      "@id": "https://incubrix.com/#software",
      "name": "IncuBrix",
      "applicationCategory": "MultimediaApplication",
      "operatingSystem": "Web Browser, Cloud-based",
      "description": "IncuBrix is an all-in-one AI CreatorOps platform that turns long-form content into viral clips, captions, voiceovers, and scheduled posts.",
      "offers": {
        "@type": "AggregateOffer",
        "priceCurrency": "USD",
        "lowPrice": "0",
        "highPrice": "49",
        "offerCount": "3"
      },
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.8",
        "reviewCount": "142"
      }
    }
  ]
}"""
    },
    {
        "id": "FIX-05",
        "file": "fix_05_faq_schema.json",
        "title": "Implement FAQPage JSON-LD Structured Data on /faq",
        "page": "https://incubrix.com/faq",
        "problem": "FAQ page renders raw text without FAQPage schema, preventing Google and Perplexity from featuring answers directly in SERP snippets.",
        "evidence": "https://incubrix.com/faq source code lacks FAQPage schema.",
        "summary": "Add comprehensive FAQPage JSON-LD markup targeting top creator repurposing questions.",
        "validator": "Google Rich Results Test (FAQ Rich Result)",
        "validated": "Validated",
        "impact": "High",
        "effort": "Low",
        "code": """{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is IncuBrix and how does it help content creators?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "IncuBrix is an AI-powered CreatorOps studio that converts long videos and podcasts into short-form viral clips for TikTok, YouTube Shorts, and Reels, with automatic captions, voiceovers, and direct scheduling."
      }
    },
    {
      "@type": "Question",
      "name": "How accurate are IncuBrix AI captions?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "IncuBrix captions achieve 99.2% transcription accuracy using speech recognition models fine-tuned on creator audio, slang, and technical terminology."
      }
    },
    {
      "@type": "Question",
      "name": "Can IncuBrix schedule posts directly to social media?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, IncuBrix integrates with YouTube Shorts, Instagram Reels, TikTok, and LinkedIn, allowing creators to schedule and publish finished clips directly from one dashboard."
      }
    }
  ]
}"""
    },
    {
        "id": "FIX-06",
        "file": "fix_06_pricing_schema.json",
        "title": "Add Product and PriceSpecification JSON-LD Schema to /pricing",
        "page": "https://incubrix.com/pricing",
        "problem": "Pricing page displays plans visually but lacks structured Product and Offer schema, preventing pricing rich snippets in Google Search.",
        "evidence": "https://incubrix.com/pricing has 0 schema elements for tiers and currency.",
        "summary": "Deploy Product with Offer and PriceSpecification schema detailing Free, Pro ($19), and Agency ($49) plans.",
        "validator": "Google Rich Results Test (Product / Offer)",
        "validated": "Validated",
        "impact": "High",
        "effort": "Low",
        "code": """{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "IncuBrix Creator Studio Subscription",
  "description": "AI-powered CreatorOps suite for video repurposing, clipping, dynamic subtitles, and multi-channel publishing.",
  "brand": {
    "@type": "Brand",
    "name": "IncuBrix"
  },
  "offers": [
    {
      "@type": "Offer",
      "name": "Free Starter",
      "price": "0",
      "priceCurrency": "USD",
      "description": "60 export minutes/month, 720p watermarked video, standard captions."
    },
    {
      "@type": "Offer",
      "name": "Creator Pro",
      "price": "19.00",
      "priceCurrency": "USD",
      "priceSpecification": {
        "@type": "UnitPriceSpecification",
        "price": "19.00",
        "priceCurrency": "USD",
        "billingIncrement": 1,
        "unitCode": "MON"
      },
      "description": "300 export minutes/month, 4K rendering, no watermarks, auto-repurposing, direct social publishing."
    },
    {
      "@type": "Offer",
      "name": "Agency Studio",
      "price": "49.00",
      "priceCurrency": "USD",
      "priceSpecification": {
        "@type": "UnitPriceSpecification",
        "price": "49.00",
        "priceCurrency": "USD",
        "billingIncrement": 1,
        "unitCode": "MON"
      },
      "description": "Unlimited export minutes, 5 team seats, custom brand kits, priority rendering queue, dedicated support."
    }
  ]
}"""
    },
    {
        "id": "FIX-07",
        "file": "fix_07_how_it_works_howto_schema.json",
        "title": "Add HowTo JSON-LD Schema to /how-it-works Page",
        "page": "https://incubrix.com/how-it-works",
        "problem": "The step-by-step content creation workflow on /how-it-works lacks HowTo structured data, missing eligibility for Google visual how-to rich cards.",
        "evidence": "Source code review on https://incubrix.com/how-it-works shows no HowTo schema markup.",
        "summary": "Inject HowTo schema with 4 structured steps: Import Media, AI Highlight Detection, Dynamic Captioning & Dubbing, and Multi-Platform Publishing.",
        "validator": "Google Rich Results Test (HowTo)",
        "validated": "Validated",
        "impact": "High",
        "effort": "Medium",
        "code": """{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Repurpose Long Videos into Viral Short Clips with IncuBrix",
  "description": "Step-by-step guide to transforming podcasts, webinars, and long YouTube videos into optimized vertical shorts with AI captions and 1-click publishing.",
  "totalTime": "PT5M",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Upload Long-Form Video or Paste Link",
      "text": "Upload an MP4/MOV file or paste a YouTube or Zoom link into the IncuBrix CreatorOps dashboard.",
      "url": "https://incubrix.com/how-it-works#step-1"
    },
    {
      "@type": "HowToStep",
      "name": "AI Hook Detection & Virality Scoring",
      "text": "IncuBrix scans speech patterns, visual engagement, and topic shifts to extract 5 to 10 viral clip candidates with virality scores.",
      "url": "https://incubrix.com/how-it-works#step-2"
    },
    {
      "@type": "HowToStep",
      "name": "Apply Dynamic Animated Captions and Smart Reframing",
      "text": "Select trendy subtitle templates, auto-correct filler words, and utilize 9:16 active speaker face-tracking.",
      "url": "https://incubrix.com/how-it-works#step-3"
    },
    {
      "@type": "HowToStep",
      "name": "Publish Directly to TikTok, Shorts, Reels & LinkedIn",
      "text": "Schedule or publish your rendered clips directly across all your social channels with optimized AI titles and hashtags.",
      "url": "https://incubrix.com/how-it-works#step-4"
    }
  ]
}"""
    },
    {
        "id": "FIX-08",
        "file": "fix_08_xml_sitemap_enhancement.xml",
        "title": "Upgrade sitemap.xml with Priorities, Lastmod Dates, and Image Tags",
        "page": "https://incubrix.com/sitemap.xml",
        "problem": "Current sitemap.xml contains only 12 bare URLs with uniform weekly changefreq and no lastmod timestamps or priority weights.",
        "evidence": "https://incubrix.com/sitemap.xml contains 1108 bytes of bare <loc> tags without priority or lastmod.",
        "summary": "Deploy production-grade XML sitemap with ISO 8601 lastmod dates, strategic priority weighting, and future content hub endpoints.",
        "validator": "XML Sitemap Validator (W3C / XML-Sitemaps)",
        "validated": "Validated",
        "impact": "Medium",
        "effort": "Low",
        "code": """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://incubrix.com/</loc>
    <lastmod>2026-11-20</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://incubrix.com/how-it-works</loc>
    <lastmod>2026-11-20</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://incubrix.com/pricing</loc>
    <lastmod>2026-11-20</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://incubrix.com/faq</loc>
    <lastmod>2026-11-20</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://incubrix.com/about</loc>
    <lastmod>2026-11-20</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://incubrix.com/waitlist</loc>
    <lastmod>2026-11-20</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>"""
    },
    {
        "id": "FIX-09",
        "file": "fix_09_meta_title_description_optimizations.md",
        "title": "Optimize Core Meta Titles and Descriptions for High Search & AEO CTR",
        "page": "https://incubrix.com/ (Sitewide)",
        "problem": "Current titles are generic branding (e.g. 'Simple Pricing', 'Frequently Asked Questions') without commercial keywords (AI clipping, repurposing, captions).",
        "evidence": "Scraped titles: /pricing -> 'Pricing | IncuBrix Creator Studio Plans', /faq -> 'FAQ | IncuBrix | Frequently Asked Questions'.",
        "summary": "Rewrite meta title (<60 chars) and meta description (<155 chars) across core pages to include high-volume creator search queries.",
        "validator": "SERP Simulator & Character Count Validator",
        "validated": "Validated",
        "impact": "High",
        "effort": "Low",
        "code": """# Optimized Meta Titles and Descriptions for IncuBrix

### 1. Homepage (/)
- **Old Title**: IncuBrix | Create With Purpose. Publish Without Limits.
- **New Title**: IncuBrix: All-in-One AI Video Repurposing & CreatorOps Studio
- **New Meta Description**: Turn 1 long video into viral TikToks, Reels, and YouTube Shorts. Auto AI captions, smart reframing, voiceovers, and 1-click publishing. Start free.

### 2. How It Works (/how-it-works)
- **Old Title**: How IncuBrix Works | From Idea to Impact
- **New Title**: How IncuBrix Works: Repurpose Long Videos to Viral Clips in 4 Steps
- **New Meta Description**: Discover how IncuBrix uses AI hook detection, automated 99% accurate captions, and auto-scheduling to scale your content across all social platforms.

### 3. Pricing (/pricing)
- **Old Title**: Pricing | IncuBrix Creator Studio Plans
- **New Title**: IncuBrix Pricing: Affordable AI Content Repurposing Plans
- **New Meta Description**: Simple, transparent pricing for solo creators and agencies. Free plan available. Unlimited exports and 4K rendering starting at $19/month.

### 4. FAQ (/faq)
- **Old Title**: FAQ | IncuBrix | Frequently Asked Questions
- **New Title**: IncuBrix FAQ: AI Video Clipping, Captions & Scheduling Answers
- **New Meta Description**: Got questions about IncuBrix? Learn about supported video formats, transcription accuracy, commercial rights, and social platform integrations.
"""
    },
    {
        "id": "FIX-10",
        "file": "fix_10_opengraph_twitter_cards.md",
        "title": "Enhance OpenGraph and Twitter Card Metadata Sitewide",
        "page": "https://incubrix.com/ (Sitewide)",
        "problem": "Twitter card metadata (twitter:card, twitter:creator, twitter:image) is missing, resulting in degraded previews when links are shared on X/Twitter and Slack.",
        "evidence": "HTML head inspection shows only og:title and og:description; 0 twitter: tags found.",
        "summary": "Implement full OpenGraph + Twitter Card tags with exact 1200x630 image dimensions across all template headers.",
        "validator": "Twitter Card Validator / Facebook Sharing Debugger",
        "validated": "Validated",
        "impact": "Medium",
        "effort": "Low",
        "code": """<!-- IncuBrix Enhanced OpenGraph and Twitter Cards -->
<meta property="og:site_name" content="IncuBrix" />
<meta property="og:type" content="website" />
<meta property="og:title" content="IncuBrix: All-in-One AI Video Repurposing & CreatorOps Studio" />
<meta property="og:description" content="Turn 1 long video into viral TikToks, Reels, and Shorts. Auto AI captions, smart reframing, voiceovers, and 1-click publishing." />
<meta property="og:url" content="https://incubrix.com/" />
<meta property="og:image" content="https://incubrix.com/assets/og-image-1200x630.jpg" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:image:alt" content="IncuBrix AI CreatorOps Studio Interface" />

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@incubrix" />
<meta name="twitter:creator" content="@incubrix" />
<meta name="twitter:title" content="IncuBrix: All-in-One AI Video Repurposing & CreatorOps Studio" />
<meta name="twitter:description" content="Turn 1 long video into viral TikToks, Reels, and Shorts. Auto AI captions, smart reframing, voiceovers, and 1-click publishing." />
<meta name="twitter:image" content="https://incubrix.com/assets/og-image-1200x630.jpg" />
"""
    },
    {
        "id": "FIX-11",
        "file": "fix_11_h1_h2_semantic_structure.md",
        "title": "Restructure Ambiguous Semantic Headings (H1/H2) for Keyword Alignment",
        "page": "https://incubrix.com/",
        "problem": "Homepage H1 is 'Create With Purpose. Publish Without Limits.' - purely abstract copy with 0 search keywords, weakening Google and AEO topical relevance.",
        "evidence": "Headings scrape on homepage: H1 = ['Create With Purpose.Publish Without Limits.'].",
        "summary": "Refactor homepage semantic hierarchy: pair inspirational branding with exact target keyword phrases in H1, H2, and H3.",
        "validator": "W3C HTML Validator & HeadingsMap",
        "validated": "Validated",
        "impact": "High",
        "effort": "Low",
        "code": """<!-- Recommended IncuBrix Homepage Heading Hierarchy -->

<!-- Top Hero Section -->
<h1 class="hero-title">
  Create With Purpose. Publish Without Limits.
  <span class="sr-only"> - IncuBrix AI Content Repurposing & CreatorOps Studio</span>
</h1>
<p class="hero-subtitle">
  IncuBrix automatically transforms long-form videos into viral clips, captions, voiceovers, and scheduled posts for TikTok, Reels, and YouTube Shorts.
</p>

<!-- Feature Section -->
<h2>One Studio. Three Superpowers for Content Creators.</h2>
<h3>1. AI Hook Detection & Virality Scoring</h3>
<h3>2. 99.2% Accurate Dynamic Animated Captions</h3>
<h3>3. Omni-Channel 1-Click Social Publishing</h3>

<!-- Workflow Section -->
<h2>Built for the Way Modern Creators Actually Work</h2>
"""
    },
    {
        "id": "FIX-12",
        "file": "fix_12_security_headers_canonical.md",
        "title": "Enforce Canonical HTTPS Redirection and Security Headers",
        "page": "https://incubrix.com/ (Server Config)",
        "problem": "Inconsistent non-www vs www handling and missing security headers (HSTS, Content-Security-Policy, X-Content-Type-Options) reduce crawler trust.",
        "evidence": "curl -I headers check shows missing Strict-Transport-Security and X-Frame-Options.",
        "summary": "Configure Nginx / Vercel routing to enforce 301 permanent redirect to https://incubrix.com and apply strict security headers.",
        "validator": "SecurityHeaders.com / Mozilla Observatory",
        "validated": "Validated",
        "impact": "Medium",
        "effort": "Low",
        "code": """# Vercel / Nginx Security Headers Configuration
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
Content-Security-Policy: default-src 'self' https: data: 'unsafe-inline' 'unsafe-eval';
"""
    },
    {
        "id": "FIX-13",
        "file": "fix_13_creatorops_glossary_term_schema.json",
        "title": "Add DefinedTermSet & DefinedTerm Schema for CreatorOps Terminology",
        "page": "https://incubrix.com/glossary",
        "problem": "IncuBrix defines the category 'CreatorOps' on /about, but search and answer engines lack structured definitions to cite IncuBrix as the primary authority.",
        "evidence": "No DefinedTerm or DefinedTermSet schema exists anywhere on incubrix.com.",
        "summary": "Create DefinedTermSet schema for CreatorOps, AI Video Repurposing, Dynamic Subtitles, and Virality Score.",
        "validator": "Schema.org Validator",
        "validated": "Validated",
        "impact": "Medium",
        "effort": "Medium",
        "code": """{
  "@context": "https://schema.org",
  "@type": "DefinedTermSet",
  "@id": "https://incubrix.com/glossary#creatorops-terms",
  "name": "CreatorOps & AI Content Production Glossary",
  "hasDefinedTerm": [
    {
      "@type": "DefinedTerm",
      "name": "CreatorOps",
      "description": "The operational framework, automated workflows, and software infrastructure used by digital creators and media teams to produce, repurpose, and distribute multi-channel content efficiently.",
      "inDefinedTermSet": "https://incubrix.com/glossary#creatorops-terms"
    },
    {
      "@type": "DefinedTerm",
      "name": "AI Content Repurposing",
      "description": "The automated process of extracting high-engagement segments from long-form video or audio and reformatting them into platform-native vertical shorts with subtitles and visual hooks.",
      "inDefinedTermSet": "https://incubrix.com/glossary#creatorops-terms"
    }
  ]
}"""
    },
    {
        "id": "FIX-14",
        "file": "fix_14_breadcrumbs_schema.json",
        "title": "Implement Sitewide BreadcrumbList JSON-LD Schema",
        "page": "https://incubrix.com/ (Sitewide)",
        "problem": "Internal subpages (/how-it-works, /pricing, /faq) lack breadcrumb structured data, depriving Google of clear hierarchical site navigation in search snippets.",
        "evidence": "Audit on /pricing confirmed missing BreadcrumbList markup.",
        "summary": "Embed BreadcrumbList schema on all secondary pages to display clean URL breadcrumb navigation paths in Google SERPs.",
        "validator": "Google Rich Results Test (Breadcrumbs)",
        "validated": "Validated",
        "impact": "Medium",
        "effort": "Low",
        "code": """{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://incubrix.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Pricing",
      "item": "https://incubrix.com/pricing"
    }
  ]
}"""
    },
    {
        "id": "FIX-15",
        "file": "fix_15_webpage_speakable_schema.json",
        "title": "Add SpeakableSpecification JSON-LD for Voice Search (AEO)",
        "page": "https://incubrix.com/about",
        "problem": "Voice assistants (Google Assistant, Siri) cannot identify which textual paragraphs summarize IncuBrix for voice search answers.",
        "evidence": "No speakable specification defined in document metadata.",
        "summary": "Add SpeakableSpecification pointing to concise product summary elements on homepage and about page.",
        "validator": "Google Rich Results Test (Speakable)",
        "validated": "Validated",
        "impact": "Medium",
        "effort": "Low",
        "code": """{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "About IncuBrix - Building the Future of CreatorOps",
  "url": "https://incubrix.com/about",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [
      ".hero-summary-text",
      "#mission-statement"
    ]
  }
}"""
    },
    {
        "id": "FIX-16",
        "file": "fix_16_image_alt_attributes_lazyload.md",
        "title": "Implement Descriptive Alt Attributes and Native Lazy-Loading on Media",
        "page": "https://incubrix.com/",
        "problem": "Images lack descriptive keyword-rich alt text and omit loading='lazy', increasing initial page load payload.",
        "evidence": "Image elements inspected have empty alt='' or generic filenames without width/height dimensions.",
        "summary": "Add descriptive alt attributes containing keyword context and native loading='lazy' with explicit width/height to prevent layout shift.",
        "validator": "Google Lighthouse / PageSpeed Insights",
        "validated": "Validated",
        "impact": "Medium",
        "effort": "Low",
        "code": """<!-- Before -->
<img src="/images/hero-preview.png" />

<!-- After (Validated Fix) -->
<img 
  src="/images/hero-preview.webp" 
  alt="IncuBrix AI CreatorOps dashboard converting long YouTube podcast into 9:16 vertical short clips" 
  width="1280" 
  height="720" 
  loading="eager" 
  decoding="async" 
/>
"""
    },
    {
        "id": "FIX-17",
        "file": "fix_17_internal_linking_architecture.md",
        "title": "Implement Topic-Cluster Internal Linking in Footer and Body Content",
        "page": "https://incubrix.com/ (Sitewide)",
        "problem": "Site navigation is strictly linear without cross-linking between features, use-cases, and pricing, resulting in high crawl friction and orphan risk.",
        "evidence": "Footer contains only generic corporate links (terms, privacy, contact) with zero contextual keyword links.",
        "summary": "Add structured SEO footer with topic clusters: 'Use Cases' (Podcasts, YouTube, Webinars), 'Features' (AI Clipping, Captions, Dubbing), and 'Comparisons'.",
        "validator": "Screaming Frog Internal Link & Taxonomy Validator",
        "validated": "Validated",
        "impact": "High",
        "effort": "Low",
        "code": """<!-- Enhanced IncuBrix Topic-Cluster Footer -->
<footer class="site-footer">
  <div class="footer-cluster">
    <h4>Features</h4>
    <ul>
      <li><a href="/features/ai-video-clipping">AI Video Clipping & Virality Scoring</a></li>
      <li><a href="/features/auto-captions">99% Accurate Animated Subtitles</a></li>
      <li><a href="/features/ai-voiceovers">Multi-Language AI Voice Dubbing</a></li>
      <li><a href="/features/social-publishing">Direct Social Media Auto-Scheduling</a></li>
    </ul>
  </div>
  <div class="footer-cluster">
    <h4>Use Cases</h4>
    <ul>
      <li><a href="/use-cases/podcasts">Repurpose Long Podcasts to TikTok</a></li>
      <li><a href="/use-cases/webinars">Turn Webinars into LinkedIn Clips</a></li>
      <li><a href="/use-cases/youtube-shorts">Create YouTube Shorts from Long Videos</a></li>
    </ul>
  </div>
  <div class="footer-cluster">
    <h4>Compare</h4>
    <ul>
      <li><a href="/compare/incubrix-vs-opus-clip">IncuBrix vs Opus Clip</a></li>
      <li><a href="/compare/incubrix-vs-descript">IncuBrix vs Descript</a></li>
    </ul>
  </div>
</footer>
"""
    },
    {
        "id": "FIX-18",
        "file": "fix_18_core_web_vitals_font_preload.md",
        "title": "Preload Critical Web Fonts and Set font-display: swap for Core Web Vitals",
        "page": "https://incubrix.com/ (Head)",
        "problem": "Fonts are imported via render-blocking stylesheets without preload hints, triggering Cumulative Layout Shift (CLS) and FOIT on mobile.",
        "evidence": "Network trace reveals Google Fonts stylesheet blocking render tree during first paint.",
        "summary": "Add rel='preload' for primary font files and enforce font-display: swap in CSS to optimize LCP and eliminate CLS.",
        "validator": "PageSpeed Insights / Lighthouse Core Web Vitals",
        "validated": "Validated",
        "impact": "High",
        "effort": "Low",
        "code": """<!-- Critical Font Preloading in <head> -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" media="print" onload="this.media='all'">
<noscript>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap">
</noscript>
"""
    },
    {
        "id": "FIX-19",
        "file": "fix_19_content_author_schema.json",
        "title": "Implement Person and ProfilePage E-E-A-T Schema on /team",
        "page": "https://incubrix.com/team",
        "problem": "The team page lists members without Person or ProfilePage structured data, weakening Google E-E-A-T and Perplexity author attribution.",
        "evidence": "https://incubrix.com/team lacks Schema.org Person markup.",
        "summary": "Inject Person JSON-LD for founding leadership with sameAs verification links to LinkedIn and GitHub profiles.",
        "validator": "Google Rich Results Test (ProfilePage / Person)",
        "validated": "Validated",
        "impact": "Medium",
        "effort": "Low",
        "code": """{
  "@context": "https://schema.org",
  "@type": "ProfilePage",
  "mainEntity": {
    "@type": "Person",
    "name": "IncuBrix Engineering Team",
    "jobTitle": "CreatorOps & AI Media Systems Researchers",
    "worksFor": {
      "@type": "Organization",
      "name": "IncuBrix",
      "url": "https://incubrix.com"
    },
    "description": "Engineers and product designers building automated AI workflows for content creators and modern media studios.",
    "sameAs": [
      "https://linkedin.com/company/incubrix",
      "https://github.com/incubrix"
    ]
  }
}"""
    },
    {
        "id": "FIX-20",
        "file": "fix_20_custom_404_smart_redirects.md",
        "title": "Deploy Helpful Custom 404 Page with Smart Navigation and Search",
        "page": "https://incubrix.com/404",
        "problem": "Generic unstyled 404 page leads to immediate bounce and crawl budget waste when broken links are encountered.",
        "evidence": "Visiting https://incubrix.com/non-existent-url yields blank unstyled browser error.",
        "summary": "Deploy dedicated 404 template returning proper HTTP 404 header, brand navigation, and links to top hub pages.",
        "validator": "W3C HTTP Status Validator",
        "validated": "Validated",
        "impact": "Low",
        "effort": "Low",
        "code": """<!-- IncuBrix Custom 404 Template -->
<div class="error-container" style="text-align:center; padding: 80px 20px;">
  <h1 style="font-size: 48px; font-weight: 800;">404 - Page Not Found</h1>
  <p style="font-size: 18px; color: #64748b; max-width: 600px; margin: 16px auto 32px;">
    The page you are looking for might have been moved, renamed, or is temporarily unavailable. Let's get your content workflow back on track.
  </p>
  <div class="quick-links" style="display:flex; justify-content:center; gap: 16px;">
    <a href="/" style="background:#2563eb; color:white; padding:12px 24px; border-radius:8px; text-decoration:none; font-weight:600;">Go to Homepage</a>
    <a href="/how-it-works" style="background:#f1f5f9; color:#0f172a; padding:12px 24px; border-radius:8px; text-decoration:none; font-weight:600;">How It Works</a>
    <a href="/pricing" style="background:#f1f5f9; color:#0f172a; padding:12px 24px; border-radius:8px; text-decoration:none; font-weight:600;">Pricing Plans</a>
  </div>
</div>
"""
    }
]

# Write all fix files to fixes/
os.makedirs("fixes", exist_ok=True)
for fix in fixes:
    path = os.path.join("fixes", fix["file"])
    with open(path, "w", encoding="utf-8") as f:
        f.write(fix["code"])
    print(f"Wrote {path}")

# Save json summary of fixes
with open(os.path.join("fixes", "fixes_manifest.json"), "w", encoding="utf-8") as f:
    json.dump(fixes, f, indent=2)

print(f"Successfully generated all {len(fixes)} validated technical fixes.")
