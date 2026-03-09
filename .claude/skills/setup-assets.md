# Setup Assets Skill

## Description
Sets up the asset folder structure and copies necessary files from the template.

## Usage
Invoke with: `/setup-assets`

## Asset Structure to Create

```
assets/
├── css/
│   ├── bootstrap.min.css
│   ├── font-awesome-pro.css
│   ├── swiper.css
│   ├── nice-select.css
│   ├── animate.css
│   ├── odometer-theme-default.min.css
│   ├── magnific-popup.css
│   ├── style.css          # Main custom stylesheet
│   └── responsive.css     # Mobile overrides
├── js/
│   ├── jquery.min.js
│   ├── bootstrap.min.js
│   ├── swiper.js
│   ├── wow.js
│   ├── nice-select.js
│   ├── magnific-popup.js
│   ├── jarallax.min.js
│   ├── imagesloaded-pkgd.js
│   └── main.js            # Custom JavaScript
├── images/
│   ├── logo/
│   │   ├── logo.svg       # Will be replaced with STC logo
│   │   └── logo-2.svg
│   ├── favicon.png        # Will be replaced with STC favicon
│   ├── icons/             # Template icons to reuse
│   └── content/           # Page-specific content images
└── fonts/
    └── (Font Awesome fonts from template)
```

## Steps

1. **Create folder structure** if it doesn't exist
2. **Copy template assets** from `docs/sample-html-template/assets/`
3. **Verify all dependencies** are present
4. **Update logo references** for STC branding
5. **Create placeholder images** where needed

## Template Assets to Copy

### Required CSS Files
- `bootstrap.min.css` - Bootstrap 5 framework
- `font-awesome-pro.css` - Font Awesome icons
- `swiper.css` - Swiper carousel
- `animate.css` - CSS animations
- `magnific-popup.css` - Lightbox plugin
- `style.css` - Main template styles (will be customized)

### Required JS Files
- `jquery.min.js` - jQuery dependency
- `bootstrap.min.js` - Bootstrap JS
- `swiper.js` - Swiper carousel
- `wow.js` - Scroll animations
- `magnific-popup.js` - Lightbox
- `main.js` - Custom template JS (will be reviewed)

### Images to Review
- Check `assets/images/icons/` for reusable icons
- Note template images that need STC replacements

## STC-Specific Assets

### Logo
- Source: `/images/Sahiwal-Tech-Community-logo.png`
- Actions:
  - Convert to SVG for scalability
  - Create resized versions (favicon, etc.)

### Favicon
- Generate from logo
- Sizes: 16x16, 32x32, 180x180 (apple-touch-icon)

### Placeholder Images
Create these for development:
- `hero-bg.jpg` - Hero section background
- `about-image.jpg` - About section image
- `team-placeholder.jpg` - Default team member photo
- `event-placeholder.jpg` - Default event image
- `blog-placeholder.jpg` - Default blog thumbnail

## Example Usage
```
/setup-assets
```

## Output
- Creates complete `assets/` folder structure
- Copies all template dependencies
- Lists assets that need STC-specific replacements
- Reports any missing files

## Notes
- Always maintain original template files as reference
- Don't modify `bootstrap.min.css` or `jquery.min.js`
- Custom styles go in `style.css` or `responsive.css`
- Template uses Font Awesome Pro - ensure license compliance
