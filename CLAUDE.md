# Sahiwal Tech Community Website - Development Guidelines

## Project Overview

**Community:** Sahiwal Tech Community
**Founder:** Kashif Sohail (AI Data Engineer)
**Established:** June 2023
**Members:** ~1,000 across 3 WhatsApp groups
**Purpose:** Knowledge-sharing, opportunity-creating platform for tech professionals in Sahiwal, Pakistan

---

## Brand Identity

### Colors (Extracted from Logo)
```css
:root {
  --green-primary:    #1a6b2e;    /* Main green */
  --green-light:      #2d9e47;    /* Light green */
  --green-pale:       #e8f5ec;    /* Pale green background */
  --gold-primary:     #c8923a;    /* Main gold */
  --gold-light:       #f0c96a;    /* Light gold highlight */
  --dark:             #0e1f14;    /* Dark background */
  --cream:            #faf8f3;    /* Cream background */
  --text:             #1c2e22;    /* Text color */
}
```

### Typography
```css
/* Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500;600&display=swap');

/* Usage */
font-family: 'Playfair Display', serif;  /* Headings */
font-family: 'DM Sans', sans-serif;      /* Body text */
```

### Taglines
- Primary: "Knowledge is for Everyone"
- Secondary: "Where Sahiwal's Tech Talent Grows Together"

---

## Website Structure

### Page Overview
```
sahiwal-tech-community/
├── index.html              # Homepage (✓ exists - use as template)
├── about.html              # About page
├── services.html           # Services/What We Offer
├── jobs.html               # Job listings
├── companies.html          # IT Companies in Sahiwal (with map) ⭐ NEW
├── events.html             # Events & Hackathons
├── blog.html               # Blog/News
├── blog-details.html       # Single blog post
├── contact.html            # Contact page
├── team.html               # Team/Leadership
├── assets/
│   ├── css/
│   │   ├── style.css           # Main stylesheet
│   │   └── responsive.css      # Mobile styles
│   ├── js/
│   │   └── main.js             # Main JavaScript
│   ├── images/
│   │   ├── logo/               # Logo files
│   │   ├── icons/              # Icon files
│   │   └── content/            # Content images
│   └── fonts/                  # Custom fonts
```

### Page Content Requirements

#### 1. index.html (Homepage)
- Hero section with community stats
- Four pillars (Jobs, Mentorship, Safety, Networking)
- Member journey flowchart
- Community impact statistics
- Join WhatsApp CTA

#### 2. about.html
- Community story and mission
- Founder profile (Kashif Sohail)
- History since 2023
- Community values and principles
- Growth milestones

#### 3. services.html
- Job opportunities board
- Mentorship programs
- Internship postings
- Hackathon updates
- Safety alerts and awareness

#### 4. jobs.html
- Current job listings
- Job categories
- Company partners (Million Miles Technologies, Wateen, The Tech Axe)
- How to apply guide
- Success stories

#### 5. companies.html ⭐ NEW
- Interactive map showing IT companies in Sahiwal
- Company directory with info cards:
  - Company logo
  - Name and description
  - Address
  - Phone number
  - Website link
  - Email contact
- Featured companies:
  - Million Miles Technologies
  - The Tech Axe
  - Wateen
  - *(and more)*
- "Add Your Company" submission form

#### 6. events.html
- Upcoming events calendar
- Hackathon announcements (e.g., Entangled 2026)
- Past events gallery
- Event registration info

#### 7. blog.html
- Tech articles
- Community news
- Success stories
- Tutorials and guides

#### 8. contact.html
- Join WhatsApp links
  - Main: https://chat.whatsapp.com/HS0ZesKSH9gB3lHulLQ1c7
- Contact form
- Social media links
- Email contact

#### 9. team.html
- Join WhatsApp links
  - Main: https://chat.whatsapp.com/HS0ZesKSH9gB3lHulLQ1c7
- Contact form
- Social media links
- Email contact

#### 9. team.html
- Community admins
- Active contributors
- Volunteer mentors

---

## Design System

### Layout Principles
- **Mobile-first** responsive design
- **Card-based** content sections
- **Generous whitespace** for readability
- **Consistent spacing** using 8px grid
- **Rounded corners** (16-20px for cards)

### Component Styles

#### Buttons
```css
.btn-primary {
  background: var(--green-light);
  color: white;
  border-radius: 40px;
  padding: 12px 24px;
  font-weight: 600;
}

.btn-secondary {
  background: var(--gold-primary);
  color: white;
  border-radius: 40px;
  padding: 12px 24px;
  font-weight: 600;
}
```

#### Cards
```css
.card {
  background: white;
  border-radius: 20px;
  padding: 32px;
  border: 1.5px solid rgba(45, 158, 71, 0.1);
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.08);
}
```

#### Sections
```css
.section {
  padding: 70px 60px;
}

.section-dark {
  background: var(--dark);
  color: white;
}

.section-pale {
  background: var(--green-pale);
}
```

### Icons
Use emoji icons or Font Awesome for consistency:
- 💼 Jobs & Opportunities
- 🎓 Mentorship & Guidance
- 🛡️ Safety & Awareness
- 🤝 Peer-to-Peer Networking
- 🚀 Internships, Events & Beyond
- 🌐 Community/Globe
- 📈 Growth
- 🌟 Excellence
- 🔗 Links/Join

---

## Content Guidelines

### Tone of Voice
- **Welcoming** - "Assalam-o-Alaikum! 👋"
- **Professional yet friendly** - Balance expertise with accessibility
- **Community-focused** - Emphasize "we" over "I"
- **Supportive** - Encourage questions and learning

### Key Messages
1. **Free & Open** - No fees, open to all tech enthusiasts
2. **Local Impact** - Sahiwal-based, serving local talent
3. **Real Opportunities** - Verified job postings and internships
4. **Peer Support** - Seniors helping juniors in real-time
5. **Safety First** - Scam alerts and cybersecurity awareness

### Content Sources
- `/docs/info-whats-app-message.md` - Community overview
- `/docs/WhatsApp Chat with *` - Real conversations and testimonials
- `/index.html` - Existing design and content
- `/images/Sahiwal-Tech-Community-logo.png` - Brand asset

---

## Technical Stack

### Core Technologies
- **HTML5** - Semantic markup
- **CSS3** - Styling with CSS variables
- **JavaScript (ES6+)** - Interactivity
- **Bootstrap 5** - Grid and components (optional)
- **Font Awesome** - Icons
- **Google Fonts** - Typography

### External Libraries
- Swiper.js - Carousels/sliders
- AOS/Animate.css - Scroll animations
- Magnific Popup - Lightboxes
- **Leaflet.js** - Interactive maps (for IT Companies page) ⭐ NEW

### Performance Guidelines
- Optimize images (WebP format preferred)
- Minify CSS and JS
- Lazy load images
- Use CDNs for external libraries
- Mobile-first responsive design

---

## Development Workflow

### Phase 1: Setup & Foundation
1. Create project folder structure
2. Set up CSS variables and base styles
3. Create reusable components
4. Set up navigation and footer

### Phase 2: Core Pages
1. Customize homepage (index.html)
2. Create about page
3. Create services page
4. Create jobs page

### Phase 3: Extended Pages
1. Create events page
2. Create **IT Companies** page with interactive map ⭐ NEW
3. Create blog listing page
4. Create contact page
5. Create team page

### Phase 4: Polish & Launch
1. Add animations and transitions
2. Optimize performance
3. Test all devices and browsers
4. SEO optimization
5. Deploy

---

## File Naming Conventions

- Use lowercase with hyphens: `about.html`, `contact.html`
- CSS files: `style.css`, `responsive.css`
- JS files: `main.js`, `animations.js`
- Images: descriptive names: `hero-bg.jpg`, `team-kashif.jpg`

---

## SEO & Accessibility

### SEO Requirements
- Unique meta title and description for each page
- Semantic HTML (header, nav, main, section, footer)
- Alt text for all images
- Proper heading hierarchy (h1 > h2 > h3)

### Accessibility
- ARIA labels for interactive elements
- Keyboard navigation support
- Color contrast minimum 4.5:1
- Focus indicators on all interactive elements

---

## Testing Checklist

### Functionality
- [ ] All links work correctly
- [ ] Forms submit properly
- [ ] Mobile menu functions
- [ ] Animations trigger correctly
- [ ] No console errors

### Responsiveness
- [ ] Mobile (320px - 767px)
- [ ] Tablet (768px - 1023px)
- [ ] Desktop (1024px+)

### Browser Compatibility
- [ ] Chrome
- [ ] Firefox
- [ ] Safari
- [ ] Edge

---

## Deployment

### Deployment Steps
1. Final testing and bug fixes
2. Optimize all assets
3. Set up hosting (Netlify, Vercel, or GitHub Pages)
4. Configure domain (if applicable)
5. Set up SSL certificate
6. Submit to search engines

---

## Skills & Workflows

This project includes custom Claude Code skills and workflows:

### Skills (`.claude/skills/`)
- `create-page.md` - Generate new pages from template
- `add-section.md` - Add reusable sections
- `apply-branding.md` - Apply brand colors consistently
- `setup-assets.md` - Initialize asset folders

### Workflows (`.claude/workflows/`)
- `website-development.md` - Complete development workflow

---

## Contact & Resources

### WhatsApp Join Links
- **Main Group:** https://chat.whatsapp.com/HS0ZesKSH9gB3lHulLQ1c7

### Founder
- **Name:** Kashif Sohail
- **Role:** AI Data Engineer
- **LinkedIn:** https://www.linkedin.com/in/kshfse/
- **Community:** Sahiwal Tech Community

### Website Developer
- **Name:** Javeed Ishaq
- **LinkedIn:** https://www.linkedin.com/in/javeed-ishaq/
- **Footer Credit:** "Crafted with 💚 by Javeed Ishaq"

### Reference Materials
- `/docs/` - All documentation and templates
- `/docs/MAP_EMBEDDING_GUIDE.md` - Guide for embedding IT companies map ⭐ NEW
- `/docs/IMPLEMENTATION_ROADMAP.md` - Complete task checklist
- `/images/Sahiwal-Tech-Community-logo.png` - Official logo
- `/index.html` - Design reference

---

*Last Updated: 2025-03-09*
*Version: 1.1*
*Built for Claude Code*
