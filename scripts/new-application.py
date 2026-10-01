#!/usr/bin/env python3
"""
Create a tailored application page for a specific company.

Usage:
    python scripts/new-application.py "Company Name" "Job Title" "Job Description"

This script:
1. Reads the main profile.json
2. Creates a tailored HTML page in /apply/ based on a template
3. Highlights skills relevant to the job description
4. Adds a custom greeting for the company
"""

import json
import sys
import os
import re
from pathlib import Path
from datetime import datetime

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
PROFILE_PATH = PROJECT_ROOT / 'data' / 'profile.json'
TEMPLATE_PATH = PROJECT_ROOT / 'scripts' / 'application-template.html'
APPLY_DIR = PROJECT_ROOT / 'apply'

# Keywords to look for in job descriptions to match skills
SKILL_KEYWORDS = {
    'siem': ['siem', 'splunk', 'mcafee', 'esm', 'correlation', 'log', 'event'],
    'soar': ['soar', 'siemplify', 'playbook', 'automation', 'orchestration'],
    'edr': ['edr', 'endpoint', 'crowdstrike', 'sentinelone', 'defender', 'rapid7'],
    'ndr': ['ndr', 'network detection', 'network traffic'],
    'vulnerability': ['vulnerability', 'vm', 'insightvm', 'qualys', 'nessus', 'scanning'],
    'incident response': ['incident response', 'ir', 'incident handling', 'escalation'],
    'mss': ['mss', 'managed security', 'mssp', 'security operations', 'soc'],
    'itsm': ['itsm', 'itil', 'servicedesk', 'service desk', 'incident management', 'problem management', 'change management'],
    'nms': ['nms', 'network monitoring', 'site24x7', 'librenms', 'observability'],
    'pam': ['pam', 'privileged access', 'beyondtrust', 'cyberark'],
    'firewall': ['firewall', 'fortigate', 'cisco asa', 'palo alto', 'checkpoint', 'sophos'],
    'cloud': ['cloud', 'aws', 'azure', 'gcp', 'cloud security'],
    'compliance': ['compliance', 'audit', 'pci', 'hipaa', 'gdpr', 'iso 27001'],
    'threat intelligence': ['threat intelligence', 'ti', 'ioc', 'threat hunting'],
    'python': ['python', 'scripting', 'automation'],
    'api': ['api', 'rest', 'openapi', 'integration'],
    'leadership': ['lead', 'manage', 'team lead', 'supervise', 'mentor', 'coordinate'],
}

def load_profile():
    """Load the profile data from JSON."""
    with open(PROFILE_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_template():
    """Load the HTML template."""
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        return f.read()

def analyze_job_description(job_description):
    """Analyze job description and return relevant skill categories."""
    jd_lower = job_description.lower()
    matched_skills = set()

    for category, keywords in SKILL_KEYWORDS.items():
        for keyword in keywords:
            if keyword.lower() in jd_lower:
                matched_skills.add(category)
                break

    return matched_skills

def get_highlighted_skills(profile, matched_categories):
    """Get skills from profile that match the job description categories."""
    highlighted = {
        'core': [],
        'tools': [],
        'soft': []
    }

    # Map categories to profile skills
    category_to_core = {
        'siem': ['SIEM Platform Management', 'Correlation Rule Engineering'],
        'soar': ['SOAR Playbook Development'],
        'edr': ['EDR / NDR Operations'],
        'ndr': ['EDR / NDR Operations'],
        'vulnerability': ['Vulnerability Management'],
        'incident response': ['Incident & Problem Management'],
        'mss': ['Managed Security Services (MSS)', 'Security Operations (SOC)'],
        'itsm': ['ITSM / ITIL Service Management', 'Incident & Problem Management'],
        'nms': ['Platform Onboarding & Migration'],
        'pam': [],  # Not explicitly in core skills
        'firewall': [],  # Covered in tools
        'cloud': [],
        'compliance': [],
        'threat intelligence': [],
        'python': [],
        'api': [],
        'leadership': ['Team Leadership', 'Operational Coordination', 'Stakeholder Management', 'Escalation Management'],
    }

    category_to_tools = {
        'siem': ['Splunk Cloud / Enterprise SIEM', 'McAfee SIEM (ESM)', 'Rapid7 (InsightVM/InsightIDR)'],
        'soar': ['Siemplify (SOAR)'],
        'edr': ['Rapid7 (InsightVM/InsightIDR)'],
        'vulnerability': ['Rapid7 (InsightVM/InsightIDR)'],
        'nms': ['Site24x7 (NMS)', 'LibreNMS'],
        'itsm': ['ManageEngine ServiceDesk Plus', 'Ivanti / SDP'],
        'pam': ['BeyondTrust (PAM)'],
        'firewall': ['Fortigate / Cisco ASA / Sophos / TippingPoint / Trend Micro'],
        'api': ['OpenAPI', 'OmniRoute (AI Gateway)'],
        'cloud': ['TrueWatch (Observability)'],
    }

    category_to_soft = {
        'leadership': ['Team Leadership', 'Mentoring & Coaching', 'Cross-functional Collaboration'],
        'incident response': ['Escalation Management', 'Technical Communication'],
        'mss': ['Stakeholder Management', 'Operational Coordination'],
    }

    # Collect highlighted skills
    for cat in matched_categories:
        if cat in category_to_core:
            highlighted['core'].extend(category_to_core[cat])
        if cat in category_to_tools:
            highlighted['tools'].extend(category_to_tools[cat])
        if cat in category_to_soft:
            highlighted['soft'].extend(category_to_soft[cat])

    # Remove duplicates while preserving order
    for key in highlighted:
        seen = set()
        highlighted[key] = [x for x in highlighted[key] if not (x in seen or seen.add(x))]

    return highlighted

def get_relevant_experience(profile, matched_categories):
    """Filter experience bullets that are most relevant to the job."""
    relevant_bullets = []

    category_keywords = {
        'siem': ['siem', 'correlation', 'rule', 'detection', 'log'],
        'soar': ['soar', 'playbook', 'automation', 'orchestration'],
        'edr': ['edr', 'endpoint', 'insightidr'],
        'vulnerability': ['vulnerability', 'vm', 'insightvm'],
        'incident response': ['incident', 'escalation', 'response'],
        'mss': ['mss', 'security operations', 'monitoring', 'client'],
        'itsm': ['itsm', 'itil', 'incident', 'problem', 'change', 'service request', 'servicedesk', 'sdp', 'ivanti'],
        'nms': ['nms', 'site24x7', 'librenms', 'network monitoring'],
        'pam': ['pam', 'beyondtrust', 'privileged'],
        'firewall': ['firewall', 'fortigate', 'cisco', 'sophos', 'tippingpoint'],
        'leadership': ['lead', 'manage', 'oversee', 'team', 'mentor', 'coordinate', 'escalation'],
    }

    for job in profile['experience']:
        relevant_job_bullets = []
        for bullet in job['bullets']:
            bullet_lower = bullet.lower()
            for cat in matched_categories:
                if cat in category_keywords:
                    for kw in category_keywords[cat]:
                        if kw in bullet_lower:
                            relevant_job_bullets.append(bullet)
                            break
                    if bullet in relevant_job_bullets:
                        break

        if relevant_job_bullets:
            relevant_bullets.append({
                'company': job['company'],
                'title': job['title'],
                'dates': job['dates'],
                'location': job.get('location', ''),
                'additional': job.get('additional', ''),
                'bullets': relevant_job_bullets[:4]  # Limit to 4 most relevant
            })

    return relevant_bullets

def slugify(text):
    """Convert text to URL-friendly slug."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    return text.strip('-')

def generate_application_page(company, job_title, job_description):
    """Generate the tailored application page."""
    profile = load_profile()
    template = load_template()

    # Analyze job description
    matched_categories = analyze_job_description(job_description)
    highlighted_skills = get_highlighted_skills(profile, matched_categories)
    relevant_experience = get_relevant_experience(profile, matched_categories)

    # If no matches, use top skills
    if not any(highlighted_skills.values()):
        highlighted_skills = {
            'core': profile['skills']['core'][:6],
            'tools': profile['skills']['tools'][:8],
            'soft': profile['skills']['soft'][:5]
        }

    # If no relevant experience found, use first 2 roles
    if not relevant_experience:
        relevant_experience = profile['experience'][:2]

    # Prepare template variables
    context = {
        'company': company,
        'job_title': job_title,
        'date': datetime.now().strftime('%B %d, %Y'),
        'name': profile['basics']['name'],
        'headline': profile['basics']['headline'],
        'pitch': profile['basics']['pitch'],
        'email': profile['basics']['email'],
        'phone': profile['basics']['phone'],
        'location': profile['basics']['location'],
        'linkedin': profile['basics']['linkedin'],
        'about': profile['about'],
        'highlighted_core_skills': highlighted_skills['core'],
        'highlighted_tool_skills': highlighted_skills['tools'],
        'highlighted_soft_skills': highlighted_skills['soft'],
        'relevant_experience': relevant_experience,
        'education': profile['education'],
        'certifications': profile['certifications'],
        'languages': profile['languages'],
    }

    # Render template
    html = render_template(template, context)

    # Write output file
    slug = slugify(company)
    output_path = APPLY_DIR / f'{slug}.html'

    APPLY_DIR.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✅ Created tailored application page: {output_path}")
    print(f"   Company: {company}")
    print(f"   Role: {job_title}")
    print(f"   Matched skill categories: {', '.join(sorted(matched_categories)) if matched_categories else 'None (using defaults)'}")
    print(f"   Relevant experience entries: {len(relevant_experience)}")

    return output_path

def render_template(template, context):
    """Simple template rendering with {{ variable }} syntax."""
    def replace_var(match):
        key = match.group(1).strip()
        keys = key.split('.')
        value = context
        try:
            for k in keys:
                if isinstance(value, list):
                    k = int(k)
                value = value[k]
        except (KeyError, IndexError, ValueError, TypeError):
            return match.group(0)

        if isinstance(value, list):
            return ', '.join(str(v) for v in value)
        return str(value)

    # Replace simple variables
    template = re.sub(r'\{\{\s*([^}]+)\s*\}\}', replace_var, template)

    # Handle loops: {{#each array}}...{{/each}}
    def replace_loop(match):
        array_key = match.group(1).strip()
        content = match.group(2)
        array = context.get(array_key, [])
        if not array:
            return ''

        result = []
        for i, item in enumerate(array):
            item_content = content
            # Replace item properties
            if isinstance(item, dict):
                for k, v in item.items():
                    item_content = item_content.replace(f'{{{{{k}}}}}', str(v))
                # Handle nested loops
                item_content = re.sub(r'\{\{#each\s+(\w+)\}\}(.*?)\{\{/each\}\}',
                                    lambda m: replace_nested_loop(m, item), item_content, flags=re.DOTALL)
            else:
                item_content = item_content.replace('{{this}}', str(item))
            result.append(item_content)
        return ''.join(result)

    def replace_nested_loop(match, parent_item):
        array_key = match.group(1).strip()
        content = match.group(2)
        array = parent_item.get(array_key, [])
        if not array:
            return ''
        result = []
        for item in array:
            item_content = content
            if isinstance(item, dict):
                for k, v in item.items():
                    item_content = item_content.replace(f'{{{{{k}}}}}', str(v))
            else:
                item_content = item_content.replace('{{this}}', str(item))
            result.append(item_content)
        return ''.join(result)

    template = re.sub(r'\{\{#each\s+(\w+)\}\}(.*?)\{\{/each\}\}', replace_loop, template, flags=re.DOTALL)

    # Handle conditionals: {{#if condition}}...{{/if}}
    def replace_if(match):
        condition = match.group(1).strip()
        content = match.group(2)
        else_content = match.group(3) or ''

        # Simple condition evaluation
        keys = condition.split('.')
        value = context
        try:
            for k in keys:
                if isinstance(value, list):
                    k = int(k)
                value = value[k]
        except (KeyError, IndexError, ValueError, TypeError):
            value = False

        # Truthy check
        is_truthy = bool(value) if not isinstance(value, list) else len(value) > 0
        return content if is_truthy else else_content

    template = re.sub(r'\{\{#if\s+([^}]+)\}\}(.*?)(?:\{\{else\}\}(.*?))?\{\{/if\}\}', replace_if, template, flags=re.DOTALL)

    return template

def main():
    if len(sys.argv) < 4:
        print("Usage: python scripts/new-application.py \"Company Name\" \"Job Title\" \"Job Description\"")
        print("\nExample:")
        print('  python scripts/new-application.py "Acme Corp" "Senior Security Engineer" "Looking for SIEM/SOAR expert with Splunk and Python experience..."')
        sys.exit(1)

    company = sys.argv[1]
    job_title = sys.argv[2]
    job_description = sys.argv[3]

    generate_application_page(company, job_title, job_description)

if __name__ == '__main__':
    main()