# CLAUDE.md: Personal Portfolio Website for Gemalyn Cabanos

> Put this file in the root of an empty project folder (for example `gemalyn-portfolio/`), then run `claude` in that folder.
> Fill in every `TODO` in Section 2 before asking Claude to build. Claude must NOT invent facts.

---

## 1. Project goal

Build a clean, fast, professional **personal website** for **Gemalyn Cabanos** to send to employers when applying for jobs.

The site must:
- Quickly show **who she is, what she does, and her key skills**
- Make it easy for a recruiter to **contact her or download her resume**
- Work well on **phones and desktops** (recruiters often open links on mobile)
- Be easy for a beginner to **edit and redeploy**

**LinkedIn:** https://www.linkedin.com/in/gemcabanos
**Location:** Naga, Bicol Region, Philippines (show city/region only, never a street address)

---

## 2. Content (fill these in first)

> Claude: use ONLY the information in this section. If something is missing or still says TODO, leave a clearly marked placeholder or ask Gemalyn. Never make up employers, dates, degrees, numbers or certifications.

### 2.1 Basics
- Full name: Gemalyn Cabanos
- Professional title / headline: `TODO` (example: "IT Support Specialist | Observability & Monitoring")
- One-sentence pitch: `TODO` (what you do and who you help)
- Email: `TODO`
- Phone (optional, only if she wants it public): `TODO`
- Profile photo file: `TODO` (put it in `/assets/`, or leave blank for initials avatar)
- Resume PDF: `TODO` (put it at `/assets/resume.pdf`)

### 2.2 About me (3-5 sentences, first person)
`TODO: paste from LinkedIn "About"`

### 2.3 What I do (3-4 service or role cards)
| Title | One-line description |
|---|---|
| `TODO` | `TODO` |
| `TODO` | `TODO` |
| `TODO` | `TODO` |

### 2.4 Skills
Group them. Remove anything that isn't true.
- **Core skills:** `TODO`
- **Tools & platforms:** `TODO`
- **Soft skills:** `TODO`

> Topics Gemalyn has recently been working with (confirm each before using): Splunk Cloud custom apps, TrueWatch (observability/monitoring) OpenAPI, AI gateways such as OmniRoute, Claude / Claude Code. Include only the ones she can honestly claim.

### 2.5 Experience (newest first)
For each role: Company, Job title, Dates, Location (optional), 2-4 bullet points of **achievements** (results, not just duties).
```
Company: TODO
Title: TODO
Dates: TODO
Bullets:
  - TODO
  - TODO
```

### 2.6 Education, Certifications, Languages
- Education: `TODO`
- Certifications: `TODO`
- Languages: `TODO`

### 2.7 Projects / Featured work (optional but strong)
For each: name, 1-2 sentence description, tools used, link (if public).
- `TODO`

### 2.8 Testimonials (optional)
Only real quotes with permission. Leave this section out if there are none.

---

## 3. Site structure

A **single-page site** with smooth anchor navigation:

1. **Hero:** name, headline, short pitch, buttons: "Download Resume", "Contact Me", "LinkedIn"
2. **About:** short bio plus optional photo
3. **What I Do:** 3-4 cards
4. **Skills:** grouped chips or bars (prefer chips; avoid fake percentage bars)
5. **Experience:** simple timeline
6. **Projects:** cards (skip the section if empty)
7. **Education & Certifications**
8. **Contact:** email link, LinkedIn link, optional simple contact method (mailto is fine)
9. **Footer:** name and year

### Tailoring for each company application
Add a lightweight way to customize the site per application:
- Create `data/profile.json` holding all content from Section 2
- Create `/apply/` pages (for example `/apply/acme.html`) generated from a small script or template that shows a **custom greeting** ("Hi Acme team") and **reorders/highlights skills** relevant to the job
- Provide a script `npm run new-application -- "Company Name"` (or a simple Python script) that creates a new tailored page from a template
- Keep the main page generic and evergreen

---

## 4. Design direction

- Modern, minimal, **professional** (not flashy). Lots of white space.
- Pick **one accent color** plus neutrals. Suggested: deep teal or indigo on white, with a dark mode that follows the visitor's system setting.
- Typography: one clean sans-serif (system font stack or a single Google Font) with clear hierarchy.
- Subtle motion only (fade-in on scroll, hover states). Respect `prefers-reduced-motion`.
- No stock-photo clutter, no auto-playing media, no popups.
- Mobile-first layout, tested at 360px, 768px and 1280px widths.

---

## 5. Technical requirements

- **Stack:** plain **HTML + CSS + a little vanilla JavaScript** (no build step required) so a beginner can edit it. If a build tool is truly helpful, explain why before adding it.
- Files should be small and readable, with comments in the code explaining each section.
- **Accessibility:** semantic HTML, alt text on images, color contrast of at least WCAG AA, keyboard navigable, visible focus states.
- **SEO & sharing:** proper `<title>`, meta description, Open Graph tags (for nice link previews on LinkedIn/WhatsApp), favicon.
- **Performance:** optimize images, no heavy libraries, target a Lighthouse score above 90.
- **Privacy:** do not publish her home address or personal phone unless she explicitly adds it. Use an email link instead of exposing data in plain-text forms.
- **No tracking or analytics** unless Gemalyn asks. If added, use a privacy-friendly option.
- **Deployment-ready** for free hosting (GitHub Pages, Netlify or Cloudflare Pages). Include a short `README.md` explaining how to deploy and how to edit the content.

Suggested folder layout:
```
gemalyn-portfolio/
  CLAUDE.md
  README.md
  index.html
  css/styles.css
  js/main.js
  data/profile.json
  assets/ (photo, resume.pdf, favicon, og-image)
  apply/ (per-company pages)
  scripts/ (new-application script)
```

---

## 6. How Claude should work

1. **Read this whole file first.** Then list any TODOs that are still empty and ask Gemalyn for them in one short message.
2. Propose a short plan (pages, colors, fonts) and wait for a quick OK before generating lots of files.
3. Build in small steps: skeleton, then content, then styling, then the per-company tailoring, then polish.
4. After each step, explain in simple language what changed and how to preview it (for example "open `index.html` in your browser" or run a local server).
5. Never use fake or placeholder statistics, logos or testimonials in the final site.
6. Write copy in a confident, honest, concise tone. Use active verbs and concrete results.
7. Ask before installing packages, deleting files, or doing anything outside this folder.
8. At the end, run a checklist (Section 7) and report the result.

---

## 7. Definition of done

- [ ] All Section 2 content filled in and reviewed by Gemalyn
- [ ] Looks good and works on phone and desktop
- [ ] Resume download and contact links work
- [ ] LinkedIn link opens https://www.linkedin.com/in/gemcabanos
- [ ] No placeholder text, broken links or unverified claims remain
- [ ] Spelling and grammar checked
- [ ] Lighthouse: Performance, Accessibility, SEO all 90 or higher
- [ ] README explains how to deploy and how to create a per-company page
- [ ] Link preview (Open Graph) tested

---

## 8. Starter prompts to use with Claude Code

1. `Read CLAUDE.md and tell me which TODO items you still need from me.`
2. `Here is my LinkedIn About, Experience, and Skills text: [paste]. Fill in Section 2 and show me before building.`
3. `Build the first version of the site based on CLAUDE.md. Start with index.html, css and data/profile.json.`
4. `Create a tailored application page for [Company], for the role of [Job Title]. Here is the job description: [paste]. Highlight my most relevant skills.`
5. `Review the site for accessibility, mobile layout and any claims not supported by my profile data.`
