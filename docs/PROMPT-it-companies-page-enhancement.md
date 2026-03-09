# IT Companies Page Enhancement Prompt

## Overview
Enhance the IT Companies page (`companies.html`) following the UI/UX Pro Max skills in .claude/skills/ui-ux-pro-max and the implementation pattern used in `index.html`. This page showcases IT companies in Sahiwal with an interactive map and company directory.

## Current State Analysis
- **File**: `companies.html`
- **Current Issues**:
  - Plain header section without background texture/pattern
  - Company cards may not use optimal grid layout
  - Map section needs proper integration
  - Inconsistent padding between sections

## Enhancement Requirements

### 1. Header/Hero Section Enhancement

**Background Enhancement:**
- Add textured background similar to index.html
- Include animated floating shapes/gradients
- Apply gradient overlay: `linear-gradient(135deg, var(--stc-dark) 0%, var(--stc-green-primary) 100%)`
- Add SVG noise texture pattern overlay
- Include floating animated shapes

**Hero Content:**
- Title wrapper with subtitle, main title, description
- Company count/overview stats
- CTA buttons (Explore Companies, Add Your Company)

### 2. Section Padding Standardization

**Apply consistent padding:**
- Desktop (>992px): `padding: 100px 0`
- Tablet (768px-991px): `padding: 80px 0`
- Tablet Portrait (576px-767px): `padding: 70px 0`
- Mobile (<576px): `padding: 60px 0`

### 3. Interactive Map Section

**Map Container:**
```css
.stc__map-section {
  padding: 100px 0;
  position: relative;
}

.stc__map-container {
  width: 100%;
  height: 500px;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
  border: 3px solid var(--stc-green-light);
}

.stc__map-iframe {
  width: 100%;
  height: 100%;
  border: none;
}
```

**Map Background Enhancement:**
- Add gradient overlay below map
- Include map legend/key
- Add search/filter controls

### 4. Companies Grid Layout

**Primary Companies Grid:**
```css
.stc__companies-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 30px;
  align-items: stretch;
}
```

**Each Company Card Structure:**
- Company logo/icon (80x80px)
- Company name
- Company description
- Category/tag badge
- Contact details (phone, email, website)
- Location info
- Social links
- "View Details" button

**Card Layout:**
```css
.stc__company-card {
  display: grid;
  grid-template-rows: auto auto 1fr auto auto;
  gap: 20px;
  padding: 40px 32px;
  min-height: 420px;
  background: var(--stc-white);
  border-radius: 20px;
  border: 1.5px solid rgba(45, 158, 71, 0.1);
  transition: all 0.4s ease;
}
```

**Responsive Grid:**
- Desktop: 3 columns
- Tablet (768px+): 2 columns
- Mobile (<768px): 1 column

### 5. Company Card Enhancement

**Visual Enhancements:**
```css
.stc__company-card {
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.08);
  position: relative;
  overflow: hidden;
}

/* Top border gradient */
.stc__company-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: linear-gradient(90deg, var(--stc-green-light), var(--stc-gold-light));
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.4s ease;
}

.stc__company-card:hover::before {
  transform: scaleX(1);
}

.stc__company-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 40px rgba(26, 107, 46, 0.15);
}
```

### 6. Company Logo/Icon Enhancement

**Company Logo Box:**
```css
.stc__company-logo-box {
  width: 80px;
  height: 80px;
  background: var(--stc-green-pale);
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 20px;
  font-size: 40px;
  transition: all 0.3s ease;
}

.stc__company-card:hover .stc__company-logo-box {
  background: var(--stc-green-light);
  transform: scale(1.05);
}
```

### 7. Category Tags/Badges

**Badge Styles:**
```css
.stc__company-badge {
  display: inline-block;
  padding: 6px 16px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.stc__badge-software {
  background: var(--stc-green-light);
  color: var(--stc-white);
}

.stc__badge-training {
  background: var(--stc-gold-primary);
  color: var(--stc-white);
}

.stc__badge-telecom {
  background: var(--stc-dark);
  color: var(--stc-white);
}
```

### 8. Filter/Search Section

**Filter Controls (if applicable):**
```css
.stc__company-filters {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  justify-content: center;
  margin-bottom: 40px;
}

.stc__filter-btn {
  padding: 10px 20px;
  border: 2px solid var(--stc-green-light);
  background: transparent;
  color: var(--stc-green-light);
  border-radius: 30px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
}

.stc__filter-btn.active,
.stc__filter-btn:hover {
  background: var(--stc-green-light);
  color: var(--stc-white);
}
```

**Categories:**
- All Companies
- Software Development
- Training & Education
- Telecommunications
- IT Services
- Startups

### 9. Stats Section (Before Map)

**Company Stats Grid:**
```css
.stc__stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 30px;
  margin: 60px 0;
}

.stc__stat-card {
  text-align: center;
  padding: 30px 20px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.stc__stat-number {
  font-size: clamp(36px, 5vw, 48px);
  font-weight: 700;
  color: var(--stc-gold-light);
  margin-bottom: 8px;
}

.stc__stat-label {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.8);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
```

**Stats to Include:**
- Total Companies
- Software Companies
- Training Centers
- Job Openings

### 10. Featured Companies Section

**Featured Companies (if any):**
- Larger card (2-column span)
- Highlighted with gold border
- "Featured" badge
- Extended description
- Priority positioning

### 11. "Add Your Company" CTA Section

**Submission Form Section:**
```css
.stc__company-cta {
  background: var(--stc-green-pale);
  padding: 80px 40px;
  border-radius: 20px;
  text-align: center;
  margin: 60px 0;
}

.stc__cta-form {
  max-width: 600px;
  margin: 40px auto 0;
}
```

**Form Elements:**
- Company name input
- Category dropdown
- Description textarea
- Contact email
- Website URL
- Submit button

### 12. Typography Enhancement

**Title Wrapper:**
```css
.stc__title-wrapper {
  text-align: center;
  margin-bottom: 60px;
}

.stc__sub-title {
  display: inline-block;
  color: var(--stc-green-light);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 2px;
  font-size: 14px;
  margin-bottom: 16px;
}

.stc__main-title {
  font-family: var(--stc-font-heading);
  font-size: clamp(32px, 5vw, 48px);
  font-weight: 700;
  color: var(--stc-text);
  line-height: 1.2;
}

.stc__title-description {
  max-width: 700px;
  margin: 20px auto 0;
  color: var(--stc-text-light);
  font-size: 18px;
  line-height: 1.7;
}
```

### 13. Company Details Modal/Expandable

**For expanded company info:**
- Modal or expandable card
- Full company details
- Job listings from company
- Team photos
- Office photos
- Map location
- Contact form

### 14. Map Integration (Leaflet.js)

**Map Implementation:**
```html
<div class="stc__map-wrapper">
  <div id="stc__companies-map" class="stc__map"></div>
</div>
```

**Map Styling:**
- Custom marker icons
- Popup cards for company info
- Cluster markers for zoom
- Custom tile layer (CartoDB or similar)
- Responsive container

### 15. Color & Theming

**Use brand colors:**
- Map markers: Green and gold
- Company cards: White with green accents
- Badges: Color-coded by category
- CTAs: Primary green, WhatsApp green

### 16. Accessibility Considerations

**Must include:**
- `aria-label` on map controls
- `aria-hidden="true"` on decorative elements
- Keyboard navigation for map
- Proper heading hierarchy
- Alt text for company logos
- Focus visible states
- Touch targets minimum 44x44px
- Color contrast minimum 4.5:1

### 17. Animation & Micro-interactions

**Add animations:**
- Fade-in on scroll for cards
- Map marker pop-in animation
- Hover effects: scale, shadow, border
- Button glow effects
- Filter button transitions

### 18. Responsive Design

**Grid Breakpoints:**
```css
/* Desktop */
.stc__companies-grid {
  grid-template-columns: repeat(3, 1fr);
}

/* Tablet (768px-991px) */
@media (max-width: 991px) {
  .stc__companies-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .stc__stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Mobile (<768px) */
@media (max-width: 767px) {
  .stc__companies-grid {
    grid-template-columns: 1fr;
  }

  .stc__stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .stc__map-container {
    height: 350px;
  }
}
```

## Featured Companies

### 1. Million Miles Technologies
- Software Development
- Sahiwal
- Hiring: Yes

### 2. The Tech Axe
- Tech Training & Internships
- Sahiwal
- Training Partner

### 3. Wateen
- Telecommunications
- Sahiwal
- Infrastructure

### 4. [Additional Companies as available]

## Implementation Checklist

- [ ] Add animated hero background with texture
- [ ] Apply 100px padding to all sections
- [ ] Convert companies to 3-column grid layout
- [ ] Enhance company cards with hover effects
- [ ] Add company logo boxes with gradient backgrounds
- [ ] Integrate interactive map (Leaflet.js)
- [ ] Add stats section above map
- [ ] Create "Add Your Company" CTA section
- [ ] Implement category filters
- [ ] Standardize all title wrappers
- [ ] Add accessibility attributes
- [ ] Add animations and micro-interactions
- [ ] Test all responsive breakpoints
- [ ] Verify color contrast ratios
- [ ] Test map functionality

## Expected Outcome

After enhancement, the IT Companies page should have:
- **Visual Appeal**: Textured hero with animated background
- **Grid Layout**: Companies in 3-column grid (responsive)
- **Interactive Map**: Leaflet.js map with company markers
- **Consistent Spacing**: 100px padding throughout
- **Card Design**: Enhanced cards with hover effects
- **Professional Look**: Company badges, verified tags
- **Accessible**: WCAG AA compliant
- **Interactive**: Filter, search, map integration
- **Responsive**: Optimized for all devices

---

**Page**: IT Companies Page Enhancement
**Created**: 2026-03-09
**Status**: Ready for Implementation
