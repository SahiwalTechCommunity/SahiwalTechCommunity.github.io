# Sahiwal Tech Community Website Development Plan

## Project Overview

**Project:** Sahiwal Tech Community Website
**Founder:** Kashif Sohail (AI Data Engineer)
**Established:** June 2023
**Members:** ~1,000 across 3 WhatsApp groups

### Community Purpose
A knowledge-sharing, opportunity-creating platform for tech professionals in Sahiwal, Pakistan - focused on jobs, mentorship, safety awareness, and networking.

---

## Brand Colors (from Logo)

```css
Primary Green:   #1a6b2e
Light Green:     #2d9e47
Pale Green:      #e8f5ec
Gold:            #c8923a
Light Gold:      #f0c96a
Dark:            #0e1f14
Cream:           #faf8f3
Text:            #1c2e22
```

---

## Website Structure (Multi-Page)

### Required Pages

1. **index.html** - Homepage
   - Hero section with community stats
   - Four pillars section (Jobs, Mentorship, Safety, Networking)
   - Member journey flowchart
   - Community impact statistics
   - Join CTA

2. **about.html** - About Page
   - Community story & mission
   - Founder information (Kashif Sohail)
   - History since 2023
   - Community values

3. **services.html** - What We Offer
   - Job opportunities board
   - Mentorship programs
   - Internship postings
   - Hackathon updates
   - Safety alerts

4. **jobs.html** - Jobs Page
   - Current job listings
   - Job categories
   - How to apply
   - Company partners

5. **events.html** - Events & Hackathons
   - Upcoming events
   - Past events gallery
   - Hackathon announcements

6. **blog.html** - Blog/News
   - Tech articles
   - Community news
   - Success stories

7. **contact.html** - Contact Page
   - Join WhatsApp links
   - Contact form
   - Social media links

8. **team.html** - Team/Leadership
   - Community admins
   - Active contributors

---

## Design Guidelines

### Typography
- Headings: 'Playfair Display' (serif)
- Body: 'DM Sans' (sans-serif)
- Google Fonts import provided in template

### Layout Principles
- Mobile-first responsive design
- Clean, modern aesthetic
- Green/gold color scheme throughout
- Card-based content sections
- Generous whitespace

### Components Needed
- Navigation bar with logo
- Hero sections with background images
- Feature cards/grid
- Statistics counters
- Call-to-action buttons
- Footer with social links

---

## Content Sources

### Available Resources
- `/docs/info-whats-app-message.md` - Community overview
- `/docs/sample-html-template/` - Base HTML template to customize
- `/images/Sahiwal-Tech-Community-logo.png` - Logo file
- `/index.html` - Existing landing page with design system
- WhatsApp chat archives for testimonials/stories

### Key Messages
- "Share knowledge, opportunities, and guidance with those who need it"
- "Knowledge is for Everyone"
- "Where Sahiwal's Tech Talent Grows Together"

---

## Development Workflow

### Phase 1: Setup & Structure
1. Create project folder structure
2. Copy template assets (CSS, JS, fonts)
3. Set up base HTML template
4. Configure color variables

### Phase 2: Core Pages
1. Customize homepage (index.html)
2. Create about page
3. Create services/offers page
4. Create jobs page

### Phase 3: Additional Pages
1. Create events page
2. Create blog page
3. Create contact page
4. Create team page

### Phase 4: Assets & Polish
1. Optimize images
2. Add animations
3. Test responsiveness
4. SEO optimization

---

## Technical Stack

- **HTML5** - Markup
- **CSS3** - Styling (Bootstrap + Custom)
- **JavaScript** - Interactivity
- **Font Awesome** - Icons
- **Swiper** - Carousels
- **Google Fonts** - Typography

---

## File Structure

```
sahiwal-tech-community/
├── index.html
├── about.html
├── services.html
├── jobs.html
├── events.html
├── blog.html
├── blog-details.html
├── contact.html
├── team.html
├── assets/
│   ├── css/
│   │   ├── bootstrap.min.css
│   │   ├── style.css
│   │   └── responsive.css
│   ├── js/
│   │   ├── main.js
│   │   └── plugins/
│   ├── images/
│   │   ├── logo/
│   │   ├── icons/
│   │   └── content/
│   └── fonts/
└── .cloud/
    ├── skills/
    └── workflows/
```

---

## Skills Available

Use these Claude Code skills for development:

- `/sahiwal-site:create-page` - Create new page from template
- `/sahiwal-site:add-component` - Add reusable component
- `/sahiwal-site:style-colors` - Apply brand colors
- `/sahiwal-site:optimize-images` - Optimize images for web
- `/sahiwal-site:test-responsive` - Test mobile responsiveness

---

## Next Steps

1. Run `/sahiwal-site:setup` to initialize project
2. Follow workflow in `.cloud/workflows/website-development.md`
3. Build pages incrementally
4. Test and deploy

---

*Last Updated: 2025-03-09*
*Version: 1.0*
