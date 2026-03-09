# Apply Branding Skill

## Description
Applies Sahiwal Tech Community branding (colors, fonts, logo) to pages and components.

## Usage
Invoke with: `/apply-branding <target>`

## Parameters
- `target`: What to apply branding to (css-file, page, all)

## Brand Assets

### Colors
```css
:root {
  /* Primary Green */
  --stc-green-primary: #1a6b2e;
  --stc-green-light: #2d9e47;
  --stc-green-pale: #e8f5ec;

  /* Gold/Accent */
  --stc-gold-primary: #c8923a;
  --stc-gold-light: #f0c96a;

  /* Neutrals */
  --stc-dark: #0e1f14;
  --stc-cream: #faf8f3;
  --stc-text: #1c2e22;
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

### Logo
- **File:** `/images/Sahiwal-Tech-Community-logo.png`
- **Usage:** Navigation bar, footer, favicon
- **Alt text:** "Sahiwal Tech Community Logo"

### Taglines
- Primary: "Knowledge is for Everyone"
- Secondary: "Where Sahiwal's Tech Talent Grows Together"

## Color Application Rules

### Navigation
- Background: White or `--stc-cream`
- Links: `--stc-text`
- Hover: `--stc-green-light`
- CTA Button: `--stc-green-light` with white text

### Hero Sections
- Background: `--stc-dark`
- Headings: White
- Subheadings: rgba(255, 255, 255, 0.7)
- Accents: `--stc-gold-light`

### Buttons
- Primary: `--stc-green-light` background, white text, rounded-pill
- Secondary: `--stc-gold-primary` background, white text, rounded-pill
- Hover: Darken by 10%

### Cards
- Background: White
- Border: 1px solid rgba(26, 107, 46, 0.1)
- Accent: `--stc-green-light` top border or icon
- Title: `--stc-text`
- Text: `--stc-text-light`

### Sections
- Standard: `--stc-cream` background
- Featured: `--stc-green-pale` background
- Dark: `--stc-dark` background

## Font Application

### Heading Hierarchy
```css
h1, .h1 { font-family: 'Playfair Display', serif; font-weight: 900; }
h2, .h2 { font-family: 'Playfair Display', serif; font-weight: 700; }
h3, .h3 { font-family: 'DM Sans', sans-serif; font-weight: 600; }
body, p, a { font-family: 'DM Sans', sans-serif; }
```

## What This Skill Does

1. **Replaces template colors** with STC brand colors
2. **Updates font imports** and font-family declarations
3. **Replaces logo references** with STC logo
4. **Updates alt text** for accessibility
5. **Creates CSS variable mappings** for template classes

## CSS Override Pattern

```css
/* Override template colors with STC branding */
:root {
  /* Template color mappings */
  --trucker-green: var(--stc-green-primary);
  --trucker-gold: var(--stc-gold-primary);
}

/* Specific overrides */
.trucker__btn-style-1 {
  background: var(--stc-green-light);
  /* ... */
}

/* Or create new STC-specific classes */
.stc__btn-primary {
  background: var(--stc-green-light);
  color: white;
  border-radius: 50px;
  padding: 14px 32px;
  font-weight: 600;
  font-family: 'DM Sans', sans-serif;
}
```

## Example Usage
```
/apply-branding css-file     # Update main CSS with STC branding
/apply-branding about.html   # Apply branding to about page
/apply-branding all          # Apply branding across entire project
```

## Notes
- Maintain WCAG AA contrast ratios (4.5:1 minimum)
- Gold is used sparingly for emphasis only
- Green variants are the primary brand colors
- Always test branding changes on multiple pages
