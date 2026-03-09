# Sahiwal Tech Community Website - Implementation Roadmap

> This document provides a step-by-step task list for building the complete multi-page website. Use this as your execution guide.

---

## Table of Contents

1. [Phase 1: Project Setup](#phase-1-project-setup)
2. [Phase 2: Asset Preparation](#phase-2-asset-preparation)
3. [Phase 3: CSS Foundation](#phase-3-css-foundation)
4. [Phase 4: Core Components](#phase-4-core-components)
5. [Phase 5: Homepage Build](#phase-5-homepage-build)
6. [Phase 6: Secondary Pages](#phase-6-secondary-pages)
7. [Phase 7: Extended Pages](#phase-7-extended-pages)
8. [Phase 8: IT Companies Page](#phase-8-it-companies-page) ⭐ NEW
9. [Phase 9: Branding & Polish](#phase-9-branding--polish)
10. [Phase 10: Testing & QA](#phase-10-testing--qa)
11. [Phase 11: Deployment](#phase-11-deployment)

> **Map Embedding Guide:** See `/docs/MAP_EMBEDDING_GUIDE.md` for detailed instructions on embedding interactive maps for IT companies.

---

## Phase 1: Project Setup

### 1.1 Initialize Project Structure
- [ ] Create `assets/` folder structure
- [ ] Create `assets/css/` directory
- [ ] Create `assets/js/` directory
- [ ] Create `assets/images/` directory
- [ ] Create `assets/images/logo/` directory
- [ ] Create `assets/images/icons/` directory
- [ ] Create `assets/images/content/` directory
- [ ] Create `assets/fonts/` directory

### 1.2 Review Template Structure
- [ ] Study `docs/sample-html-template/index.html`
- [ ] Study `docs/sample-html-template/about.html`
- [ ] Study `docs/sample-html-template/service.html`
- [ ] Study `docs/sample-html-template/team.html`
- [ ] Study `docs/sample-html-template/contact.html`
- [ ] Note all CSS classes and patterns used
- [ ] Note all JS dependencies and their load order

**Status:** Not Started

---

## Phase 2: Asset Preparation

### 2.1 Copy Template CSS Files
- [ ] Copy `bootstrap.min.css` to `assets/css/`
- [ ] Copy `font-awesome-pro.css` to `assets/css/`
- [ ] Copy `swiper.css` to `assets/css/`
- [ ] Copy `nice-select.css` to `assets/css/`
- [ ] Copy `animate.css` to `assets/css/`
- [ ] Copy `odometer-theme-default.min.css` to `assets/css/`
- [ ] Copy `magnific-popup.css` to `assets/css/`
- [ ] Copy `style.css` to `assets/css/` (will customize)

### 2.2 Copy Template JS Files
- [ ] Copy `jquery.min.js` to `assets/js/`
- [ ] Copy `bootstrap.min.js` to `assets/js/`
- [ ] Copy `swiper.js` to `assets/js/`
- [ ] Copy `wow.js` to `assets/js/`
- [ ] Copy `nice-select.js` to `assets/js/`
- [ ] Copy `magnific-popup.js` to `assets/js/`
- [ ] Copy `jarallax.min.js` to `assets/js/`
- [ ] Copy `imagesloaded-pkgd.js` to `assets/js/`
- [ ] Copy `main.js` to `assets/js/` (will customize)

### 2.3 Copy Fonts
- [ ] Copy all Font Awesome font files to `assets/fonts/`
- [ ] Copy `flaticon` files to `assets/fonts/`
- [ ] Verify font file integrity

### 2.4 Prepare STC Brand Assets
- [ ] Convert `Sahiwal-Tech-Community-logo.png` to SVG
- [ ] Create favicon from logo (16x16, 32x32)
- [ ] Create apple-touch-icon (180x180)
- [ ] Create logo variations for dark/light backgrounds
- [ ] Prepare placeholder images for development

**Status:** Not Started

---

## Phase 3: CSS Foundation

### 3.1 Create Main Stylesheet
Create `assets/css/stc-style.css` with:
- [ ] CSS variables for brand colors
- [ ] Font imports (Playfair Display, DM Sans)
- [ ] Base HTML element styles
- [ ] Bootstrap overrides for STC branding
- [ ] Utility classes for colors and spacing

### 3.2 Create Responsive Stylesheet
Create `assets/css/responsive.css` with:
- [ ] Mobile styles (< 768px)
- [ ] Tablet styles (768px - 1023px)
- [ ] Desktop overrides (> 1024px)
- [ ] Container max-width adjustments

### 3.3 Define CSS Variables
```css
:root {
  --stc-green-primary: #1a6b2e;
  --stc-green-light: #2d9e47;
  --stc-green-pale: #e8f5ec;
  --stc-gold-primary: #c8923a;
  --stc-gold-light: #f0c96a;
  --stc-dark: #0e1f14;
  --stc-cream: #faf8f3;
  --stc-text: #1c2e22;
}
```

**Status:** Not Started

---

## Phase 4: Core Components

### 4.1 Navigation Component
- [ ] Create header structure based on template
- [ ] Add STC logo
- [ ] Add navigation links (Home, About, Services, Jobs, **IT Companies**, Events, Blog, Team, Contact)
- [ ] Add "Join WhatsApp" CTA button
- [ ] Implement mobile hamburger menu
- [ ] Add smooth scroll behavior

### 4.2 Footer Component
- [ ] Create footer structure based on template
- [ ] Add community name and tagline
- [ ] Add founder info section:
  - [ ] Name: Kashif Sohail
  - [ ] Role: AI Data Engineer
  - [ ] LinkedIn link: https://www.linkedin.com/in/kshfse/
  - [ ] LinkedIn icon + "Connect on LinkedIn" text
- [ ] Add WhatsApp join link
- [ ] Add social media links
- [ ] Add copyright notice with dynamic year
- [ ] **Add developer credit section:**
  - [ ] Text: "Crafted with 💚 by Javeed Ishaq" (recommended)
  - [ ] LinkedIn link: https://www.linkedin.com/in/javeed-ishaq/
  - [ ] Subtle styling (smaller font, muted color)
  - [ ] Heart animation on the emoji
- [ ] Add scroll-to-top button

> **Reference:** See `/docs/FOOTER_CREDIT_GUIDE.md` for complete HTML/CSS templates

### Founder & Developer Links
**Kashif Sohail - Founder:**
- LinkedIn: https://www.linkedin.com/in/kshfse/
- Role: AI Data Engineer
- Use for: About page founder section, footer

**Javeed Ishaq - Website Developer:**
- LinkedIn: https://www.linkedin.com/in/javeed-ishaq/
- Credit text: "Crafted with 💚 by Javeed Ishaq"
- Use for: Footer credit section on all pages

### 4.3 Hero Section Component
- [ ] Create hero section structure
- [ ] Add background image handling
- [ ] Add headline styling (Playfair Display)
- [ ] Add subheadline styling (DM Sans)
- [ ] Add CTA button styling
- [ ] Add animation classes (WOW.js)

### 4.4 Card Component
- [ ] Create base card styling
- [ ] Add border/shadow styling
- [ ] Add hover effects
- [ ] Create card variations (feature, job, event, blog, team)

**Status:** Not Started

---

## Phase 5: Homepage Build

### 5.1 Homepage Structure
- [ ] Create `index.html` from template
- [ ] Add all required CSS files in head
- [ ] Add navigation component
- [ ] Add footer component

### 5.2 Homepage Sections

**Hero Section:**
- [ ] Add "Knowledge is for Everyone" headline
- [ ] Add community stats (1,000+ members, 3 groups, since 2023)
- [ ] Add background gradient overlays
- [ ] Add Join WhatsApp CTA

**Four Pillars Section:**
- [ ] Create 2x2 grid
- [ ] Add pillar cards: Jobs 💼, Mentorship 🎓, Safety 🛡️, Networking 🤝
- [ ] Add icons and descriptions
- [ ] Add hover animations

**Member Journey Section:**
- [ ] Create flowchart visualization
- [ ] Add steps: Join → Learn → Connect → Grow → Give Back
- [ ] Add arrows between steps
- [ ] Add responsive layout for mobile

**Impact Stats Section:**
- [ ] Create stats counter section
- [ ] Add: Members (1,000+), Jobs Posted (100+), Events (20+), Success Stories (50+)
- [ ] Add odometer animation
- [ ] Style with gold accents

**Final CTA Section:**
- [ ] Add "Join Our Community" section
- [ ] Add WhatsApp join button
- [ ] Add community values statement

**Status:** Not Started

---

## Phase 6: Secondary Pages

### 6.1 About Page (`about.html`)
- [ ] Create page from template
- [ ] Add hero: "Our Story"
- [ ] Add community story section
- [ ] Add founder profile section:
  - [ ] Name: Kashif Sohail
  - [ ] Role: AI Data Engineer
  - [ ] Photo placeholder
  - [ ] Bio/description
  - [ ] **LinkedIn profile link:** https://www.linkedin.com/in/kshfse/
  - [ ] LinkedIn button/icon with "Connect on LinkedIn" text
- [ ] Add founding date (June 2023)
- [ ] Add community values section
- [ ] Add growth timeline
- [ ] Add mission statement

### 6.2 Services Page (`services.html`)
- [ ] Create page from template
- [ ] Add hero: "What We Offer"
- [ ] Add service cards:
  - [ ] Job Opportunities Board
  - [ ] Mentorship Programs
  - [ ] Internship Postings
  - [ ] Hackathon Updates
  - [ ] Safety Alerts & Awareness
- [ ] Add descriptions for each service
- [ ] Add "Get Started" CTA

### 6.3 Jobs Page (`jobs.html`)
- [ ] Create page from template
- [ ] Add hero: "Opportunities"
- [ ] Add job listing cards (at least 6-8 sample listings)
- [ ] Add company partner logos:
  - [ ] Million Miles Technologies
  - [ ] Wateen
  - [ ] The Tech Axe
- [ ] Add "How to Apply" section
- [ ] Add success stories/testimonials

**Status:** Not Started

---

## Phase 7: Extended Pages

### 7.1 Events Page (`events.html`)
- [ ] Create page from template
- [ ] Add hero: "Events & Hackathons"
- [ ] Add upcoming events section
- [ ] Add Entangled 2026 hackathon banner (PKR 10M prizes)
- [ ] Add past events gallery
- [ ] Add event registration info
- [ ] Add calendar view (optional)

### 7.2 Blog Page (`blog.html`)
- [ ] Create page from template
- [ ] Add hero: "Community News"
- [ ] Add blog grid layout
- [ ] Create sample blog posts:
  - [ ] "How to Get the Most Out of STC"
  - [ ] "Success Story: From Junior to Senior"
  - [ ] "Hackathon Preparation Guide"
  - [ ] "Scam Alert: Spotting Fake Opportunities"
- [ ] Add category filters
- [ ] Add "Read More" links

### 7.3 Contact Page (`contact.html`)
- [ ] Create page from template
- [ ] Add hero: "Join Us"
- [ ] Add WhatsApp join section (prominent)
- [ ] Add WhatsApp link: https://chat.whatsapp.com/HS0ZesKSH9gB3lHulLQ1c7
- [ ] Add contact form
- [ ] Add social media links
- [ ] Add email contact option

### 7.4 Team Page (`team.html`)
- [ ] Create page from template
- [ ] Add hero: "Our Team"
- [ ] Add founder/admin section
- [ ] Add team member cards
- [ ] Add social links for each member
- [ ] Add "Become a Contributor" CTA

**Status:** Not Started

---

## Phase 8: IT Companies Page ⭐ NEW

### 8.1 IT Companies Page (`companies.html`)
- [ ] Create page from template
- [ ] Add hero: "Sahiwal's Tech Ecosystem"
- [ ] Add subtitle: "Discover IT companies driving innovation in our city"

### 8.2 Interactive Map Section
- [ ] Include Leaflet.js CSS and JS files
- [ ] Create map container (500px height, full width)
- [ ] Initialize map centered on Sahiwal (30.6668, 73.0946)
- [ ] Add OpenStreetMap tiles
- [ ] Create custom marker icon with STC branding
- [ ] Add company markers with coordinates
- [ ] Configure popups with company info
- [ ] Style popups to match STC design

### 8.3 Company Data Structure
- [ ] Create `assets/js/companies-data.js` with company information
- [ ] Include for each company:
  - [ ] Name and logo
  - [ ] Address (Sahiwal location)
  - [ ] Phone number
  - [ ] Website URL
  - [ ] Email address
  - [ ] Description
  - [ ] Founded year
  - [ ] Employee count
  - [ ] Specialties/skills
  - [ ] Latitude/Longitude coordinates

### 8.4 Company Directory Grid
- [ ] Create company card component
- [ ] Add company logo placeholder
- [ ] Add company name and description
- [ ] Add contact details:
  - [ ] 📍 Address
  - [ ] 📞 Phone (clickable link)
  - [ ] 🌐 Website (external link)
  - [ ] ✉️ Email (mailto link)
- [ ] Add "View on Map" button (zooms to marker)
- [ ] Add "Visit Website" button
- [ ] Implement card hover effects
- [ ] Add responsive grid layout

### 8.5 Featured Companies
Add at least these known Sahiwal IT companies:
- [ ] **Million Miles Technologies** - Software development, web/mobile apps
- [ ] **The Tech Axe** - Tech training, internships, skill development
- [ ] **Wateen** - Internet, telecommunications, fiber optics
- [ ] *(Add more companies as discovered)*

### 8.6 Add Your Company CTA
- [ ] Create submission form section
- [ ] Add form fields:
  - [ ] Company name
  - [ ] Contact person
  - [ ] Email
  - [ ] Phone
  - [ ] Address
  - [ ] Website
  - [ ] Description
  - [ ] Logo upload
- [ ] Add "Community Review Process" notice
- [ ] Add submission button

### 8.7 Map Features
- [ ] Add map controls (zoom in/out)
- [ ] Add map legend if needed
- [ ] Ensure map is responsive on mobile
- [ ] Add map loading state
- [ ] Test marker popups on all devices

### 8.8 Cross-Page Integration
- [ ] Link to companies page from Jobs page (hiring companies)
- [ ] Link to companies page from About page (local ecosystem)
- [ ] Add "IT Companies" to navigation menu
- [ ] Add featured companies section to homepage

**Status:** Not Started

**Reference:** See `/docs/MAP_EMBEDDING_GUIDE.md` for detailed implementation instructions

---

## Phase 9: Branding & Polish

### 8.1 Apply Brand Colors
- [ ] Update all CSS with STC color variables
- [ ] Replace template green with STC green
- [ ] Replace template gold with STC gold
- [ ] Update button styles
- [ ] Update link colors
- [ ] Update section backgrounds

### 8.2 Update Typography
- [ ] Apply Playfair Display to all headings
- [ ] Apply DM Sans to all body text
- [ ] Set proper font weights
- [ ] Adjust font sizes for hierarchy
- [ ] Add responsive font sizing

### 8.3 Replace Logo
- [ ] Update navigation logo
- [ ] Update footer logo
- [ ] Update preloader logo
- [ ] Update favicon
- [ ] Add proper alt text

### 8.4 Add Animations
- [ ] Initialize WOW.js
- [ ] Add scroll animations to sections
- [ ] Add hover effects to cards
- [ ] Add button hover states
- [ ] Add navigation hover effects

### 8.5 Add Interactive Elements
- [ ] Initialize Swiper for carousels (if used)
- [ ] Initialize Magnific Popup for lightboxes
- [ ] Add mobile menu toggle functionality
- [ ] Add smooth scroll behavior
- [ ] Add form validation (contact form)

**Status:** Not Started

---

## Phase 9: Testing & QA

### 9.1 Functionality Testing
- [ ] Test all navigation links
- [ ] Test all CTA buttons
- [ ] Test contact form submission
- [ ] Test mobile menu
- [ ] Test all animations trigger correctly
- [ ] Check browser console for errors

### 9.2 Responsiveness Testing
- [ ] Test on mobile (320px - 767px)
  - [ ] iPhone SE (375px)
  - [ ] iPhone 12/13 (390px)
  - [ ] Android (360px)
- [ ] Test on tablet (768px - 1023px)
  - [ ] iPad (768px)
  - [ ] iPad Pro (1024px)
- [ ] Test on desktop (1024px+)
  - [ ] Laptop (1366px)
  - [ ] Desktop (1920px)

### 9.3 Browser Compatibility
- [ ] Test in Chrome
- [ ] Test in Firefox
- [ ] Test in Safari
- [ ] Test in Edge

### 9.4 Accessibility Testing
- [ ] Check all images have alt text
- [ ] Check color contrast (minimum 4.5:1)
- [ ] Test keyboard navigation
- [ ] Check ARIA labels on interactive elements
- [ ] Test screen reader compatibility

### 9.5 Performance Testing
- [ ] Run Lighthouse audit
- [ ] Optimize images (WebP)
- [ ] Minify CSS and JS
- [ ] Implement lazy loading
- [ ] Check load times

**Status:** Not Started

---

## Phase 11: Deployment

### 10.1 Pre-Deployment
- [ ] Final review of all pages
- [ ] Check all content for accuracy
- [ ] Verify all links work
- [ ] Update meta tags for SEO
- [ ] Create sitemap.xml
- [ ] Create robots.txt

### 10.2 Deployment Steps
- [ ] Choose hosting platform (Netlify/Vercel/GitHub Pages)
- [ ] Connect repository or upload files
- [ ] Configure custom domain (if applicable)
- [ ] Set up SSL certificate
- [ ] Test live site

### 10.3 Post-Launch
- [ ] Submit to Google Search Console
- [ ] Submit to Bing Webmaster Tools
- [ ] Set up analytics (Google Analytics)
- [ ] Create social media profiles
- [ ] Announce launch in WhatsApp group

**Status:** Not Started

---

## Summary Checklist

### Pages to Create (9 total)
- [ ] `index.html` - Homepage
- [ ] `about.html` - About page
- [ ] `services.html` - Services page
- [ ] `jobs.html` - Jobs page
- [ ] `companies.html` - **IT Companies page** (NEW - with interactive map)
- [ ] `events.html` - Events page
- [ ] `blog.html` - Blog page
- [ ] `contact.html` - Contact page
- [ ] `team.html` - Team page

### CSS Files to Create
- [ ] `assets/css/stc-style.css` - Main custom styles
- [ ] `assets/css/responsive.css` - Responsive overrides

### JS Files to Create
- [ ] `assets/js/stc-main.js` - Custom JavaScript
- [ ] `assets/js/companies-data.js` - Company data for map (NEW)
- [ ] `assets/js/companies-map.js` - Leaflet.js map initialization (NEW)

### Asset Tasks
- [ ] Copy all template CSS/JS files
- [ ] Prepare STC logo (SVG conversion)
- [ ] Create favicon
- [ ] Optimize all images

---

## Quick Reference

### WhatsApp Links
- Main Group: https://chat.whatsapp.com/HS0ZesKSH9gB3lHulLQ1c7

### Brand Colors
- Green Primary: #1a6b2e
- Green Light: #2d9e47
- Gold Primary: #c8923a
- Gold Light: #f0c96a
- Dark: #0e1f14
- Cream: #faf8f3

### Founder
- Name: Kashif Sohail
- Role: AI Data Engineer
- LinkedIn: https://www.linkedin.com/in/kshfse/

### Website Developer
- Name: Javeed Ishaq
- LinkedIn: https://www.linkedin.com/in/javeed-ishaq/
- Footer Credit: "Crafted with 💚 by Javeed Ishaq"

### Community Stats
- Members: ~1,000
- Groups: 3
- Founded: June 2023

---

## Additional Documentation

- **Map Embedding Guide:** `/docs/MAP_EMBEDDING_GUIDE.md` - Complete guide for embedding interactive maps showing IT companies in Sahiwal
- **Footer Credit Guide:** `/docs/FOOTER_CREDIT_GUIDE.md` - Founder and developer credits for footer and About page

---

*Last Updated: 2025-03-09*
*Version: 1.2*
