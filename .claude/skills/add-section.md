# Add Section Skill

## Description
Adds a content section to a page following the Bootstrap-based template structure and Sahiwal Tech Community design system.

## Usage
Invoke with: `/add-section <section-type>`

## Available Section Types

### 1. hero
Hero section with:
- Background image (use community-appropriate image)
- Main headline (Playfair Display or DM Sans)
- Subheadline
- CTA button(s)
- Animation classes (wow, img-custom-anim-*)

### 2. stats-counter
Statistics counter section with:
- 4-column grid
- Animated numbers (odometer)
- Icons/labels
- Background image option (jarallax)

### 3. features-grid
Grid of feature cards:
- 3 or 4 column layout
- Icon + title + description per card
- Hover animations
- Border/shadow styling

### 4. about-split
Split layout about section:
- Left: Image
- Right: Content with title, description, feature list
- Optional signature/author info

### 5. service-cards
Service cards grid:
- Card-based layout
- Icon/image per card
- Title and description
- Link to details

### 6. team-grid
Team member grid:
- Photo
- Name
- Role
- Social links
- Optional bio

### 7. blog-listing
Blog post listing:
- Card layout
- Featured image
- Category tag
- Title
- Excerpt
- Read more link

### 8. contact-form
Contact form section:
- Form fields (name, email, subject, message)
- Submit button
- Form validation

### 9. cta-banner
Call-to-action banner:
- Headline
- Description
- CTA button
- Green or dark background

### 10. pillars-grid
Four pillars section (community-specific):
- Jobs & Opportunities
- Mentorship & Guidance
- Safety & Awareness
- Peer-to-Peer Networking
- 2x2 grid with icons

## Section Template Pattern

```html
<!-- Start [Section Name] Area -->
<section class="stc__[section-name]-area [optional-class]">
  <div class="stc__container">
    <div class="stc__[section-name]-wrapper">

      <!-- Section Title (if needed) -->
      <div class="stc__title-wrapper">
        <p class="stc__sub-title wow img-custom-anim-left">Subtitle</p>
        <h2 class="stc__main-title wow img-custom-anim-right">Main Title</h2>
      </div>

      <!-- Section Content -->
      <!-- Section-specific content here -->

    </div>
  </div>
</section>
<!-- End [Section Name] Area -->
```

## Brand Color Integration

All sections use these CSS variables:
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

## Animation Classes

The template uses WOW.js with custom animations:
- `wow img-custom-anim-left` - Animate from left
- `wow img-custom-anim-right` - Animate from right
- `wow img-custom-anim-top` - Animate from top
- `wow fadeInUp` - Fade in up
- `wow fadeInDown` - Fade in down

## Example Usage
```
/add-section hero
/add-section stats-counter
/add-section pillars-grid
```

## Notes
- All sections use Bootstrap 5 grid system
- Container class: `stc__container` (max-width: 1296px, padded)
- Maintain template spacing classes
- Use Font Awesome icons from the template
- Sections are mobile-responsive by default
