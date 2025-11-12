import os
import shutil
import yaml
import re
import json
from pathlib import Path
from datetime import datetime

# --- SATBIR SINGH'S DATA ---
# This dictionary holds all the content for the website.
SATBIR_DATA = {
    "name": "Satbir Singh",
    "email": "satbir.taya84@gmail.com",
    "phone": "+1 510-402-1230",
    "location": "Castro Valley, CA",
    "avatar": "profile.jpeg",
    "profiles": {
        "linkedin_user": "satbirprofile",
        "github_user": "geekysatbir",
        "facebook_user": "satbir.singh.58726",
        "instagram_user": "satbir7262",
    },
    "summary": "Distinguished technology leader with 19+ years across AIOps, Observability, SaaS Reliability, and Identity & Access Management. Credited with original contributions of major significance adopted by Fortune 500 enterprises and U.S. agencies; automation frameworks reduced MTTR by up to 45% and hardened mission-critical platforms. Performed leading and critical roles in high-impact escalations safeguarding service continuity. Recognized by others in the field as an IEEE Senior Member, IETE Fellow, and SCRS Fellow with peer-reviewed publications, judging roles, and advisory work—evidence of sustained national and international acclaim placing me among the small percentage at the very top of the field. My proposed continued work in the United States will prospectively benefit the United States by scaling identity-aware observability and AI-driven auto-remediation across essential public- and private-sector systems.",
    "competencies": [
        "AIOps & Intelligent Automation (AI-driven auto-remediation)",
        "Full‑Stack Observability (AppDynamics, Splunk)",
        "Identity & Access Management (IAM)",
        "SaaS Reliability Engineering & Digital Resilience ",
        "Kubernetes & Cloud‑Native Architectures",
        "Customer Engineering Leadership",
        "Machine Learning for Predictive Monitoring",
        "Judging, Peer Review & Advisory",
        "Publications & Conference Leadership",
    ],
    "experience": [
        {
            "company": "Cisco Systems, Inc. (AppDynamics/Splunk)",
            "title": "Technical Leader",
            "dates": "Apr 2019 – Present",
            "location": "San Francisco Bay Area, CA",
            "details": [
                "Led end-to-end SaaS observability strategies ensuring uninterrupted performance across multi-billion-dollar deployments.",
                "Won an award at Cisco for creating CaseMaster tool that reduced manual effort by 1500 hours every month for the customer engineering team. Also won $2500 worth of awards from various team members for my great job.",
                "Engineered signal-driven diagnostics and runbooks → −45% MTTR; protected Fortune 500 and U.S. federal agencies (DHS, DOS/CA, IRS, NASA).",
                "Resolved 120+ high-priority escalations annually, safeguarding $500M+ in customer continuity.",
                "CSOne↔Webex automation standard across CX → 1,550+ hrs/yr saved, faster MTTR, higher CSAT.",
                "Built dashboards/health rules for 1,500+ apps (K8s + on-prem) → 99.9% uptime on Black Friday; −80% migration-risk downtime.",
                "Optimized tracing/JVM instrumentation for booking/check-in → 99.95% uptime, −30% latency, −40% response time.",
                "Custom API-volume views → 99.9% availability across 700k+ patent transactions/year.",
                "Authored K8s/containers/serverless monitoring runbooks used by 20+ enterprises → 35% faster time-to-value, −25% incident response time.",
                "Built and tuned AI for HTOM → +70% improvement in Golden Rules ratings.",
                "Contributed to Splunk community by writing Technical articles and helping our product users."
            ]
        },
        {
            "company": "Persistent Systems",
            "title": "Senior Implementation Engineer",
            "dates": "Aug 2015 – Mar 2019",
            "location": "San Francisco Bay Area, CA",
            "details": [
                "ERCOT (OEM for Oracle IAM): Observability for OAM/OIM/OVD/OID → 99.9% uptime, −40% incident response time, +15% login success.",
                "Intuit (IAM support automation): Observability-driven runbooks → −60% MTTR on ~500 tickets/mo, −40% OPEX (~$200K/yr).",
                "USAA (IAM roles & advanced auth): Risk-based observability → +40% security efficiency, −30% unauthorized access.",
                "Exelon (OUD migration): Observability-first directory stack → +40% directory speed, 100% migration success."
            ]
        },
        {
            "company": "Wipro",
            "title": "Technical Lead",
            "dates": "Jul 2013 – Jul 2015",
            "location": "San Jose, USA / Gurugram, India",
            "details": [
                "Kohl’s (Lead Engineer): Led OWASP Top-10 testing; risk/MTTR dashboards → −35% MTTR, 2× vuln-closure rate.",
                "Seagate (Senior Software Engineer): Built Oracle IAM end-to-end; SLO dashboards & alerts → 99.5% uptime, −50% provisioning time.",
                "Telenor Myanmar: Setup Identity and access management for the first ever Telecom setup in Myanmar."
            ]
        },
        {
            "company": "AlertEnterprise, Inc.",
            "title": "Sr. Specialist Development Engineer",
            "dates": "Nov 2011 – Jun 2013",
            "location": "Chandigarh, India",
            "details": [
                "Shipped core IAM modules and suite hardening; acted as Scrum Master → +22% velocity, −28% defect leakage.",
                "Built 12+ connectors (incl. OAuth Salesforce, SCIM, Linux/Unix) and a Connector Management portal.",
                "Embedded identity telemetry on 100% new connectors → −35% MTTR, −40% reconciliation lag."
            ]
        },
        {
            "company": "CampusEAI Consortium",
            "title": "Sr. Consultant Engineer",
            "dates": "Mar 2011 – Nov 2011",
            "location": "Gurugram, India",
            "details": [
                "Led IAM rollouts for 4+ universities; owned delivery from install to handover.",
                "Added audit/health logs and baseline dashboards → −30% MTTR, −35% reconciliation lag; improved go-live SLA adherence to >98%."
            ]
        },
        {
            "company": "Persistent Systems",
            "title": "Software Strategist / Analyst",
            "dates": "Jul 2006 – Nov 2010",
            "location": "Pune, India",
            "details": [
                "Drove RFIs/RFPs with Presales; crafted GTM for Identity & Access Management.",
                "Built provisioning/reconciliation connectors for Avaya PBX, Oracle DB, Siebel, and Sun ONE/Active Directory.",
                "Generated $2M+ in connector revenue; earned Spot Award for contributions."
            ]
        }
    ],
    "awards": [
        {"name": "Claro Awards — Winner (2025)", "url": "https://claroawards.com/winner"},
        {"name": "Global Recognition Awards — Winner (2025)", "url": ""},
        {"name": "Titan Innovation Awards — Winner (2025, Customer Engineering & Transformation)", "url": "https://thetitanawards.com/winner-info.php?id=7460"},
        {"name": "Cisco Innovation Award — Recognition for automation in SaaS reliability", "url": ""},
        {"name": "Global Tech Awards — Nominee (2025)", "url": ""},
        {"name": "Cisco Connected Recognition — 2019–2025, cumulative ~$2,500 in peer/manager spot awards", "url": ""},
        {"name": "Topmate Recognition — In progress", "url": ""},
        {"name": "Army Institute of Technology (AIT) — Highly selective admission (2002)", "url": ""},
    ],
    "memberships": [
        "Fellow — IETE (Granted Jun 2025)",
        "Distinguished Fellow — Soft Computing Research Society (SCRS) (Granted Jul 2025)",
        "Senior Member — IEEE (Granted Jul 2025)",
        "Full Member — Sigma Xi (Accepted Aug 2025)",
        "PeopleCert Ambassador (Accepted 2025)",
        "DASA Ambassador (DevOps/Agile) (Accepted 2025)",
        "ISCEA Ambassador (Supply Chain) (Granted Jun 2025)",
    ],
    "publications": [
        {
            "title": "A Review of Hybrid Neural Network and Fuzzy Logic Control Techniques for Optimising Electric Vehicle Performance",
            "authors": "Singh, S., Pahuja, V., Handaragal, R., Susurani, V., & Malhotra, H.",
            "date": "2026-01-01",
            "venue": "ICICC 2026 — Special Session",
            "category": "under_review",
            "excerpt": "Paper shows full author list and scope in the submitted manuscript."
        },
        {
            "title": "Unifying DevOps and MLOps Pipelines Via AI-driven Observability: A Mixed-Methods Study",
            "authors": "Singh, S.",
            "date": "2025-06-01",
            "venue": "Asian Journal of Research in Computer Science, 18(6), 334-342",
            "category": "published",
            "excerpt": "A study on integrating AI-driven observability to unify DevOps and MLOps pipelines.",
            "url": "https://hal.science/hal-05107405/"
        },
        {
            "title": "From Ops to Experience: AIOps-Enabled MLOps with Identity-Aware and Customer-Informed Pipelines",
            "authors": "Singh, S.",
            "date": "2025-01-01",
            "venue": "Proceedings of IEEE WCONF 2025",
            "category": "published",
            "excerpt": "Single-author paper; shows >50% MTTR improvement in the evaluation framework and a tenant-secure SaaS design."
        },
        {
            "title": "Blockchain-Based Intrusion Detection and Response Framework for Secure Industrial IoT Networks",
            "authors": "Lakshma Reddy, B., Jadhav, S., Singh, S., Mapari, N. B., Gupta, S., Reshma, S., & Bhutani, M.",
            "date": "2025-01-02",
            "venue": "Proceedings of IEEE ICCSD 2025",
            "category": "published",
            "excerpt": ""
        }
    ],
    "talks": [
        {
            "title": "Monitoring to Observability",
            "type": "Podcast",
            "venue": "Page it to the Limit",
            "date": "2025-09-02",
            "url": "https://www.pageittothelimit.com/monitoring-o11y-satbir-singh/",
            "description": "The transition from traditional monitoring technologies to modern observability tools can leave teams confused. Satbir Singh joins us to talk about the new goals of observability tooling and how it will help teams conquer challenges in complex systems."
        },
        {
            "title": "Keynote Speaker",
            "type": "Keynote",
            "venue": "Supply Chain Technology Conference",
            "date": "2025-01-02",
            "url": "https://www.sctechshow.com/agenda-day-2"
        },
        {
            "title": "DASA Ambassador Talks",
            "type": "Talk",
            "venue": "DASA",
            "date": "2025-01-03",
            "url": ""
        },
        {
            "title": "Advisory Board Member",
            "type": "Advisory",
            "venue": "Tensech Inc.",
            "date": "2025-07-01",
            "url": "https://www.tensech.com/"
        }
    ],
    "education": {
        "degree": "B.S. in Computer Science & Engineering",
        "institution": "Army Institute of Technology, Pune University, India",
        "year": "2006"
    }
}

# --- UTILITY FUNCTIONS ---
def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    text = re.sub(r'^-+|-+$', '', text)
    return text

def clean_directory(dir_path):
    if not os.path.exists(dir_path):
        print(f"Directory not found, skipping cleanup: {dir_path}")
        return
    print(f"Cleaning directory: {dir_path}")
    for filename in os.listdir(dir_path):
        if filename.endswith((".md", ".html")):
            os.remove(os.path.join(dir_path, filename))

# --- CORE FUNCTIONS ---
def clean_repository(root_dir):
    print("--- Cleaning Repository ---")
    dirs_to_clean = ['_posts', '_portfolio', '_teaching', '_publications', '_talks']
    for d in dirs_to_clean:
        clean_directory(root_dir / d)

    items_to_remove = [
        'talkmap.ipynb', 'talkmap.py', 'talkmap_out.ipynb', 'talkmap',
        'markdown_generator', 'CONTRIBUTING.md', 'README.md',
        '.github'
    ]
    for item in items_to_remove:
        path = root_dir / item
        try:
            if path.is_file():
                path.unlink()
                print(f"Removed file: {item}")
            elif path.is_dir():
                shutil.rmtree(path)
                print(f"Removed directory: {item}")
        except FileNotFoundError:
            pass

    with open(root_dir / 'README.md', 'w') as f:
        f.write(f"# {SATBIR_DATA['name']}'s Personal Website\n\nThis repository contains the source code for my personal website, built with Jekyll and the Academic Pages theme.\n")
    print("Created new README.md")

def update_config(root_dir):
    print("--- Updating _config.yml ---")
    config_path = root_dir / '_config.yml'
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    github_user = SATBIR_DATA['profiles']['github_user']
    
    config['url'] = ""
    config['baseurl'] = ""
    
    config['title'] = SATBIR_DATA['name']
    config['name'] = SATBIR_DATA['name']
    config['description'] = "Satbir Singh's Professional Portfolio"
    config['repository'] = f"{github_user}/{github_user}.github.io"

    config['author']['name'] = SATBIR_DATA['name']
    config['author']['avatar'] = SATBIR_DATA['avatar']
    config['author']['bio'] = "Technology Leader in AIOps, Observability, and SaaS Reliability."
    config['author']['location'] = SATBIR_DATA['location']
    config['author']['employer'] = "Cisco Systems, Inc."
    config['author']['email'] = SATBIR_DATA['email']
    
    config['author']['github'] = github_user
    config['author']['linkedin'] = SATBIR_DATA['profiles']['linkedin_user']
    config['author']['facebook'] = SATBIR_DATA['profiles']['facebook_user']
    config['author']['instagram'] = SATBIR_DATA['profiles']['instagram_user']
    
    for key in ['googlescholar', 'twitter', 'medium', 'stackoverflow', 'orcid', 'pubmed', 'bluesky']:
        if key in config['author']:
            config['author'][key] = None

    config['publication_category'] = {
        'published': {'title': 'Peer-Reviewed Publications'},
        'under_review': {'title': 'Manuscripts Under Review'}
    }

    with open(config_path, 'w') as f:
        yaml.dump(config, f, sort_keys=False)
    print("Successfully updated _config.yml")

def update_homepage(root_dir):
    print("--- Updating Homepage ---")
    homepage_path = root_dir / '_pages' / 'about.md'
    
    content = f"""---
permalink: /
title: "About"
author_profile: true
---

{SATBIR_DATA['summary']}

## Core Competencies
"""
    for competency in SATBIR_DATA['competencies']:
        content += f"- {competency}\n"

    content += "\n## Recent News\n"
    all_items = []
    for pub in SATBIR_DATA['publications']:
        all_items.append({'date': pub['date'], 'type': 'Publication', 'title': pub['title'], 'venue': pub['venue']})
    for talk in SATBIR_DATA['talks']:
        all_items.append({'date': talk['date'], 'type': talk['type'], 'title': talk['title'], 'venue': talk['venue']})
    
    sorted_items = sorted(all_items, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'), reverse=True)
    
    for item in sorted_items[:3]:
        content += f"* **{item['type']}:** \"{item['title']}\" at *{item['venue']}*.\n"

    with open(homepage_path, 'w') as f:
        f.write(content)
    print("Successfully updated homepage with News section.")

def create_experience_page(root_dir):
    print("--- Creating Experience Page ---")
    page_path = root_dir / '_pages' / 'experience.md'
    content = """---
layout: archive
title: "Professional Experience"
permalink: /experience/
author_profile: true
---

"""
    for job in SATBIR_DATA['experience']:
        content += f"## {job['title']}\n"
        content += f"**{job['company']}** | _{job['dates']}_ | {job['location']}\n\n"
        for detail in job['details']:
            content += f"- {detail}\n"
        content += "\n"
    with open(page_path, 'w') as f:
        f.write(content)
    print("Successfully created experience.md")

def create_publication_files(root_dir):
    print("--- Creating Publication Files ---")
    pub_dir = root_dir / '_publications'
    pub_dir.mkdir(exist_ok=True)
    for pub in SATBIR_DATA['publications']:
        filename = f"{pub['date']}-{slugify(pub['title'][:50])}.md"
        filepath = pub_dir / filename
        
        citation = f"{pub['authors']}. ({pub['date'][:4]}) \"{pub['title']}.\" <i>{pub['venue']}</i>."
        
        # --- THIS IS THE CORRECTED CONTENT BLOCK ---
        # It now includes "collection: publications" which is essential for Jekyll.
        content = f"""---
title: "{pub['title']}"
collection: publications
permalink: /publication/{filename.replace('.md', '')}
excerpt: "{pub['excerpt']}"
date: {pub['date']}
venue: "{pub['venue']}"
citation: '{citation}'
"""
        # Add paperurl only if it exists
        if pub.get('url'):
            content += f"paperurl: '{pub['url']}'\n"
        
        # Add the category for sorting on the publications page
        if pub.get('category'):
            content += f"category: {pub['category']}\n"

        content += "---\n"
        # --- END OF CORRECTED BLOCK ---

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    print(f"Created {len(SATBIR_DATA['publications'])} publication files.")

def create_talk_files(root_dir):
    print("--- Creating Talk Files ---")
    talk_dir = root_dir / '_talks'
    talk_dir.mkdir(exist_ok=True)
    for talk in SATBIR_DATA['talks']:
        filename = f"{talk['date']}-{slugify(talk['title'])}.md"
        filepath = talk_dir / filename
        content = f"""---
title: "{talk['title']}"
collection: talks
type: "{talk['type']}"
permalink: /talks/{talk['date']}-{slugify(talk['title'])}
venue: "{talk['venue']}"
date: {talk['date']}
location: ""
---
"""
        if talk.get('url'):
            content += f"\n[More information here]({talk['url']})\n"
        if talk.get('description'):
            content += f"\n{talk['description']}\n"
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    print(f"Created {len(SATBIR_DATA['talks'])} talk files.")

def create_awards_page(root_dir):
    print("--- Creating Awards & Memberships Page ---")
    page_path = root_dir / '_pages' / 'awards.md'
    content = """---
layout: archive
title: "Awards & Professional Activities"
permalink: /awards/
author_profile: true
---

## Awards & Recognitions
"""
    for award in SATBIR_DATA['awards']:
        if award['url']:
            content += f"- [{award['name']}]({award['url']})\n"
        else:
            content += f"- {award['name']}\n"
    content += "\n## Professional Memberships\n"
    for membership in SATBIR_DATA['memberships']:
        content += f"- {membership}\n"
    with open(page_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully created awards.md")

def update_navigation(root_dir):
    print("--- Updating Navigation ---")
    nav_path = root_dir / '_data' / 'navigation.yml'
    new_nav = {
        'main': [
            {'title': 'About', 'url': '/'},
            {'title': 'Experience', 'url': '/experience/'},
            {'title': 'Publications', 'url': '/publications/'},
            {'title': 'Talks', 'url': '/talks/'},
            {'title': 'Awards', 'url': '/awards/'},
            {'title': 'CV', 'url': '/cv/'},
        ]
    }
    with open(nav_path, 'w') as f:
        yaml.dump(new_nav, f, sort_keys=False)
    print("Successfully updated navigation.yml")

def update_cv_json(root_dir):
    print("--- Updating cv.json ---")
    cv_json_path = root_dir / '_data' / 'cv.json'
    profiles = []
    for key, user in SATBIR_DATA['profiles'].items():
        network = key.replace('_user', '').capitalize()
        url = ""
        if network == 'Linkedin':
            url = f"https://www.linkedin.com/in/{user}/"
        elif network == 'Github':
            url = f"https://github.com/{user}/"
        if url:
            profiles.append({"network": network, "username": user, "url": url})
    cv_data = {
        "basics": {
            "name": SATBIR_DATA['name'],
            "email": SATBIR_DATA['email'],
            "phone": SATBIR_DATA['phone'],
            "website": f"https://{SATBIR_DATA['profiles']['github_user']}.github.io",
            "summary": SATBIR_DATA['summary'],
            "location": {"city": SATBIR_DATA['location']},
            "profiles": profiles
        },
        "work": [
            {
                "company": job['company'],
                "position": job['title'],
                "startDate": job['dates'].split('–')[0].strip(),
                "endDate": job['dates'].split('–')[1].strip(),
                "summary": "",
                "highlights": job['details']
            } for job in SATBIR_DATA['experience']
        ],
        "education": [
            {
                "institution": SATBIR_DATA['education']['institution'],
                "area": SATBIR_DATA['education']['degree'],
                "studyType": "B.S.",
                "endDate": SATBIR_DATA['education']['year']
            }
        ],
        "skills": [{"name": "Core Competencies", "keywords": SATBIR_DATA['competencies']}],
        "publications": [
            {
                "name": pub['title'],
                "publisher": pub['venue'],
                "releaseDate": pub['date'],
                "summary": pub['excerpt']
            } for pub in SATBIR_DATA['publications'] if pub['category'] == 'published'
        ],
        "presentations": [
            {
                "name": talk['title'],
                "event": talk['venue'],
                "date": talk['date']
            } for talk in SATBIR_DATA['talks']
        ]
    }
    with open(cv_json_path, 'w') as f:
        json.dump(cv_data, f, indent=2)
    print("Successfully updated cv.json")

def overwrite_template_files(root_dir):
    print("--- Overwriting template files for fixes ---")
    publications_page_path = root_dir / '_pages' / 'publications.html'
    publications_content = """---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

{% if site.publication_category %}
  {% for category in site.publication_category  %}
    {% assign title_shown = false %}
    {% for post in site.publications reversed %}
      {% if post.category != category[0] %}
        {% continue %}
      {% endif %}
      {% unless title_shown %}
        <h2>{{ category[1].title }}</h2><hr />
        {% assign title_shown = true %}
      {% endunless %}
      {% include archive-single.html %}
    {% endfor %}
  {% endfor %}
{% else %}
  {% for post in site.publications reversed %}
    {% include archive-single.html %}
  {% endfor %}
{% endif %}
"""
    with open(publications_page_path, 'w', encoding='utf-8') as f:
        f.write(publications_content)
    print("Fixed publications page.")

    talks_include_path = root_dir / '_includes' / 'archive-single-talk.html'
    talks_include_content = """{% include base_path %}
{% if post.id %}{% assign title = post.title | markdownify | remove: "<p>" | remove: "</p>" %}{% else %}{% assign title = post.title %}{% endif %}
<div class="{{ include.type | default: "list" }}__item">
  <article class="archive__item" itemscope itemtype="http://schema.org/CreativeWork">
    <h2 class="archive__item-title" itemprop="headline">
      <a href="{{ base_path }}{{ post.url }}" rel="permalink">{{ title }}</a>
    </h2>
    {% if post.date %}<p class="page__meta"><i class="fa fa-clock" aria-hidden="true"></i> {{ post.date | date: '%B %d, %Y' }}</p>{% endif %}
    <p class="archive__item-excerpt" itemprop="description">{{ post.type }} at {{ post.venue }}{% if post.location and post.location != "" %}, {{ post.location }}{% endif %}</p>
    {% if post.content and post.content != "" %}<p class="archive__item-excerpt" itemprop="description">{{ post.content | markdownify | strip_html | truncatewords: 30 }}</p>{% endif %}
  </article>
</div>
"""
    with open(talks_include_path, 'w', encoding='utf-8') as f:
        f.write(talks_include_content)
    print("Fixed talks page formatting.")

def create_cv_page(root_dir):
    print("--- Creating CV Page ---")
    cv_page_path = root_dir / '_pages' / 'cv.md'
    
    work_experience_md = ""
    for job in SATBIR_DATA['experience']:
        work_experience_md += f"### {job['title']}\n"
        work_experience_md += f"**{job['company']}** | *{job['dates']}, {job['location']}*\n\n"
        for detail in job['details']:
            work_experience_md += f"- {detail}\n"
        work_experience_md += "\n"

    competencies_md = "\n".join([f"* {c}" for c in SATBIR_DATA['competencies']])

    content = f"""---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
---

{{% include base_path %}}

## Education
* **{SATBIR_DATA['education']['degree']}**, {SATBIR_DATA['education']['institution']}, {SATBIR_DATA['education']['year']}

## Work Experience
{work_experience_md}

## Core Competencies
{competencies_md}

## Publications
<ul>{{% for post in site.publications reversed %}}
  {{% include archive-single-cv.html %}}
{{% endfor %}}</ul>

## Talks & Presentations
<ul>{{% for post in site.talks reversed %}}
  {{% include archive-single-talk-cv.html %}}
{{% endfor %}}</ul>
"""
    content = content.replace("{{%", "{%").replace("%}}", "}}")
    
    with open(cv_page_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully created cv.md")

def main():
    repo_root = Path(__file__).parent.resolve()
    print(f"Updating repository at: {repo_root}")
    
    clean_repository(repo_root)
    update_config(repo_root)
    
    update_homepage(repo_root)
    create_experience_page(repo_root)
    create_awards_page(repo_root)
    create_cv_page(repo_root)
    
    create_publication_files(repo_root)
    create_talk_files(repo_root)
    
    update_navigation(repo_root)
    update_cv_json(repo_root)
    overwrite_template_files(repo_root)
    
    print("\n✅ All tasks completed successfully!")
    print("Please make sure 'profile.jpeg' is in the 'images/' directory.")
    print("You can now commit and push your changes to GitHub using './update.sh'.")

if __name__ == '__main__':
    main()