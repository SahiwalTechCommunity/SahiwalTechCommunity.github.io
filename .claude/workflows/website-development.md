# Sahiwal Tech Community Website Development Workflow

## Overview
This workflow guides the complete development of the Sahiwal Tech Community multi-page website from setup to deployment.

## Prerequisites
- Access to `docs/sample-html-template/` for base structure
- Sahiwal Tech Community logo in `/images/`
- Brand colors defined (see CLAUDE.md)
- Content from `docs/website_requirements.md` and `docs/info-whats-app-message.md`

---

## Phase 1: Project Setup

### 1.1 Initialize Project Structure
```
/setup-assets
```
This creates:
- `assets/css/` - Stylesheets
- `assets/js/` - JavaScript files
- `assets/images/` - Images
- `assets/fonts/` - Fonts

### 1.2 Copy Template Assets
Copy all dependencies from `docs/sample-html-template/assets/`:
- CSS files (Bootstrap, Font Awesome, Swiper, etc.)
- JS files (jQuery, Bootstrap, plugins)
- Fonts
- Review and copy relevant icons/images

### 1.3 Create Main CSS File
Create `assets/css/style.css` with:
- CSS variables for STC brand colors
- Font imports (Playfair Display, DM Sans)
- Template class overrides
- Custom STC classes

---

## Phase 2: Foundation Pages

### 2.1 Create Base Template Components

**Navigation:**
- Logo on left
- Links: Home, About, Services, Jobs, Events, Blog, Team, Contact
- Join WhatsApp CTA button
- Mobile hamburger menu

**Footer:**
- Community name and tagline
- Founder: Kashif Sohail
- WhatsApp join link
- Social media links
- Copyright

### 2.2 Create Homepage (`index.html`)
```
/create-page index
```

Sections needed:
1. **Hero** - "Knowledge is for Everyone" with stats
2. **Four Pillars** - Jobs, Mentorship, Safety, Networking
3. **Member Journey** - Flowchart showing community path
4. **Impact Stats** - Member count, jobs posted, etc.
5. **CTA** - Join WhatsApp

### 2.3 Create About Page (`about.html`)
```
/create-page about
```

Sections needed:
1. **Hero** - "Our Story"
2. **Community Story** - Since June 2023
3. **Founder Section** - Kashif Sohail profile
4. **Values** - What we believe in
5. **Growth Timeline** - Milestones

### 2.4 Create Services Page (`services.html`)
```
/create-page services
```

Sections needed:
1. **Hero** - "What We Offer"
2. **Services Grid**:
   - Job Opportunities
   - Mentorship Programs
   - Internship Postings
   - Hackathon Updates
   - Safety Alerts

---

## Phase 3: Extended Pages

### 3.1 Create Jobs Page (`jobs.html`)
```
/create-page jobs
```

Sections needed:
1. **Hero** - "Opportunities"
2. **Job Listings** - Cards with company, title, location
3. **Company Partners** - Million Miles, Wateen, The Tech Axe
4. **How to Apply** - Guide for members

### 3.2 Create Events Page (`events.html`)
```
/create-page events
```

Sections needed:
1. **Hero** - "Events & Hackathons"
2. **Upcoming Events** - Event cards with dates
3. **Past Events** - Gallery
4. **Hackathon Banner** - Entangled 2026 info

### 3.3 Create Blog Page (`blog.html`)
```
/create-page blog
```

Sections needed:
1. **Hero** - "Community News"
2. **Blog Grid** - Article cards
3. **Categories** - Jobs, Events, Success Stories, Guides

### 3.4 Create Contact Page (`contact.html`)
```
/create-page contact
```

Sections needed:
1. **Hero** - "Join Us"
2. **WhatsApp Links** - Main group link
3. **Contact Form** - Name, email, message
4. **Social Links** - Facebook, LinkedIn, etc.

### 3.5 Create Team Page (`team.html`)
```
/create-page team
```

Sections needed:
1. **Hero** - "Our Team"
2. **Admins** - Community administrators
3. **Contributors** - Active members
4. **Mentors** - Volunteer mentors

---

## Phase 4: Branding & Styling

### 4.1 Apply Brand Colors
```
/apply-branding all
```

Updates:
- All CSS files with STC color variables
- Button styles
- Section backgrounds
- Link colors

### 4.2 Update Typography
- Playfair Display for headings
- DM Sans for body text
- Proper heading hierarchy

### 4.3 Replace Logo
- Update all logo references
- Add favicon
- Ensure proper alt text

---

## Phase 5: Content Population

### 5.1 Homepage Content
- Stats: ~1,000 members, 3 groups, since 2023
- Tagline: "Knowledge is for Everyone"
- WhatsApp join link

### 5.2 About Page Content
- Founder: Kashif Sohail (AI Data Engineer)
- Established: June 2023
- Community mission and values

### 5.3 Services Content
- Job postings
- Mentorship opportunities
- Safety alerts information
- Event announcements

### 5.4 Jobs Page Content
- Current job listings
- Company partner logos
- Application instructions

### 5.5 Events Content
- Upcoming hackathons
- Past event highlights
- Registration information

---

## Phase 6: Polish & Testing

### 6.1 Mobile Responsiveness
- Test on mobile (320px - 767px)
- Test on tablet (768px - 1023px)
- Test on desktop (1024px+)

### 6.2 Cross-Browser Testing
- Chrome
- Firefox
- Safari
- Edge

### 6.3 Accessibility Check
- Alt text for all images
- ARIA labels for interactive elements
- Color contrast minimum 4.5:1
- Keyboard navigation

### 6.4 Performance Optimization
- Optimize images (WebP format)
- Minify CSS and JS
- Lazy load images
- Test load times

### 6.5 SEO Optimization
- Unique meta titles and descriptions
- Semantic HTML structure
- Proper heading hierarchy
- Sitemap.xml

---

## Phase 7: Deployment

### 7.1 Final Review
- Check all links work
- Test all forms
- Verify mobile menu
- Check animations trigger

### 7.2 Deploy
- Choose hosting (Netlify, Vercel, GitHub Pages)
- Upload files
- Configure domain
- Set up SSL

### 7.3 Post-Launch
- Submit to search engines
- Set up analytics
- Monitor performance

---

## Skills Reference

| Skill | Usage |
|-------|-------|
| `/setup-assets` | Initialize asset folders and copy template files |
| `/create-page <name>` | Create a new HTML page from template |
| `/add-section <type>` | Add a section to an existing page |
| `/apply-branding <target>` | Apply STC colors and fonts |

---

## Important Notes

1. **Template Structure:** Always reference `docs/sample-html-template/` for structure patterns
2. **Class Prefixes:** Template uses `trucker__` - will replace with `stc__` for STC branding
3. **Dependencies:** Never modify Bootstrap or jQuery files
4. **Custom CSS:** All custom styles go in `assets/css/style.css`
5. **Mobile First:** All sections are responsive by default
6. **Brand Colors:** See CLAUDE.md for exact color values
7. **WhatsApp Link:** https://chat.whatsapp.com/HS0ZesKSH9gB3lHulLQ1c7
