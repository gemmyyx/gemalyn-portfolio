# Gemalyn Cabanos — Personal Portfolio Website

A clean, fast, professional personal website for job applications. Built with plain HTML, CSS, and vanilla JavaScript — no build step required.

## 🌐 Live Demo

Once deployed, the site will be available at: `https://gemcabanos.github.io/` (or your custom domain)

## 📁 Project Structure

```
gemalyn-portfolio/
├── index.html              # Main portfolio page
├── css/
│   └── styles.css          # All styles
├── js/
│   └── main.js             # Mobile nav, scroll animations, etc.
├── data/
│   └── profile.json        # All content (single source of truth)
├── assets/
│   ├── resume.pdf          # Your resume (downloadable)
│   ├── favicon.svg         # Site favicon
│   ├── og-image.svg        # Open Graph image for social sharing
│   └── photo.jpg           # Your profile photo (optional)
├── apply/                  # Tailored per-company pages (generated)
├── scripts/
│   ├── new-application.py  # Script to create tailored pages
│   └── application-template.html  # Template for tailored pages
└── README.md               # This file
```

## ✏️ How to Edit Content

### Option 1: Edit `data/profile.json` (Recommended)

All content lives in `data/profile.json`. Edit this file and the main site will reflect your changes. No HTML editing needed!

```json
{
  "basics": {
    "name": "Gemalyn Cabanos",
    "headline": "Implementation Lead | Managed Security Services",
    "pitch": "Your one-sentence pitch...",
    "email": "gemalyncabanos@gmail.com",
    "phone": "+63 968 297 0029",
    "location": "Naga City, Philippines",
    "linkedin": "https://www.linkedin.com/in/gemcabanos",
    "photo": "assets/photo.jpg"
  },
  "about": "Your bio...",
  "whatIDo": [...],
  "skills": { "core": [...], "tools": [...], "soft": [...] },
  "experience": [...],
  "education": [...],
  "certifications": [...],
  "projects": [...],
  "languages": [...]
}
```

After editing `profile.json`, open `index.html` in your browser to preview.

### Option 2: Add a Profile Photo

1. Add your photo as `assets/photo.jpg` (recommended: 400x400px, square)
2. Update `photo` path in `profile.json` if needed

### Option 3: Update Resume

Replace `assets/resume.pdf` with your latest resume. The download button will automatically serve the new file.

## 🎨 Customizing Design

### Colors

Edit CSS custom properties in `css/styles.css`:

```css
:root {
  --color-primary: #0f627e;      /* Main accent (deep teal) */
  --color-primary-dark: #0a4d5e;
  --color-primary-light: #147a9a;
  --color-primary-soft: #e6f2f4;  /* Light accent backgrounds */
  /* ... */
}
```

### Font

The site uses **Inter** from Google Fonts. To change:

1. Update the `<link>` in `index.html` head
2. Update `--font-family` in `css/styles.css`

## 🚀 Deployment

### GitHub Pages (Free, Recommended)

1. **Create a GitHub repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOURUSERNAME/gemalyn-portfolio.git
   git push -u origin main
   ```

2. **Enable GitHub Pages**
   - Go to Settings → Pages
   - Source: "Deploy from a branch"
   - Branch: `main` / `(root)`
   - Save

3. **Your site is live at** `https://YOURUSERNAME.github.io/gemalyn-portfolio/`

### Netlify (Free, Drag & Drop)

1. Go to [netlify.com](https://netlify.com) and sign up
2. Drag the entire `gemalyn-portfolio` folder to the deploy area
3. Your site is live instantly with a random subdomain (customize in settings)

### Cloudflare Pages (Free)

1. Connect your GitHub repo to Cloudflare Pages
2. Build command: (leave empty)
3. Output directory: `/` (root)
4. Deploy

### Custom Domain

All three platforms support custom domains. Add a `CNAME` file to the root with your domain, then configure DNS.

## 📄 Creating Tailored Application Pages

For each job application, create a customized page that highlights relevant skills:

```bash
python scripts/new-application.py "Company Name" "Job Title" "Paste job description here"
```

### Example

```bash
python scripts/new-application.py "Acme Corp" "Senior Security Engineer" "We're looking for a SIEM expert with Splunk and SOAR experience. Must have incident response and Python scripting skills. Team leadership a plus."
```

This creates `apply/acme-corp.html` with:
- Custom greeting: "Hi Acme Corp Team"
- Skills filtered to match the job (SIEM, SOAR, Python, Leadership)
- Experience bullets relevant to the role
- All your education, certifications, and contact info

### How It Works

1. Script reads `data/profile.json`
2. Analyzes job description for keywords
3. Maps keywords to your skills/experience
4. Generates a tailored HTML page from `scripts/application-template.html`
5. Outputs to `apply/company-name.html`

Share the link: `https://yoursite.com/apply/acme-corp.html`

## ✅ Pre-Launch Checklist

- [ ] All content in `data/profile.json` is accurate and reviewed
- [ ] Resume PDF is current at `assets/resume.pdf`
- [ ] Profile photo added at `assets/photo.jpg` (or remove photo reference)
- [ ] LinkedIn URL is correct: `https://www.linkedin.com/in/gemcabanos`
- [ ] Email and phone are correct
- [ ] Test on mobile (360px), tablet (768px), desktop (1280px)
- [ ] Test resume download works
- [ ] Test contact links (email, phone, LinkedIn)
- [ ] Run Lighthouse audit (Performance, Accessibility, SEO > 90)
- [ ] Test Open Graph preview (share link on LinkedIn/WhatsApp)

## ♿ Accessibility Features

- Semantic HTML5 structure
- Skip to main content link
- ARIA labels and roles
- Focus visible states
- Color contrast WCAG AA+
- `prefers-reduced-motion` support
- Keyboard navigable
- Alt text on images

## 🔧 Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Android)

## 📝 License

MIT License — feel free to use as a template for your own portfolio.

## 🤝 Need Help?

- Check the [CLAUDE.md](CLAUDE.md) for detailed project specifications
- Open an issue if something isn't working
- The code is intentionally simple — read `css/styles.css` and `js/main.js` to understand how it works