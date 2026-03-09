# Create Page Skill

## Description
Creates a new HTML page for the Sahiwal Tech Community website using the Bootstrap-based template structure from `docs/sample-html-template/`.

## Usage
Invoke with: `/create-page <page-name>`

## Parameters
- `page-name`: The name of the page to create (e.g., "about", "services", "contact")

## Template Structure (Based on sample-html-template)

All pages must follow this structure:

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Page Name | Sahiwal Tech Community</title>

  <!-- CSS Files (match template exactly) -->
  <link rel="stylesheet preload" href="assets/css/font-awesome-pro.css" as="style">
  <link rel="stylesheet preload" href="assets/css/bootstrap.min.css" as="style">
  <link rel="stylesheet preload" href="assets/css/swiper.css" as="style">
  <link rel="stylesheet preload" href="assets/css/nice-select.css" as="style">
  <link rel="stylesheet preload" href="assets/css/animate.css" as="style">
  <link rel="stylesheet preload" href="assets/css/odometer-theme-default.min.css" as="style">
  <link rel="stylesheet preload" href="assets/css/magnific-popup.css" as="style">
  <link rel="stylesheet preload" href="assets/css/style.css" as="style">

  <!-- Favicon -->
  <link rel="shortcut icon" type="image/x-icon" href="assets/images/favicon.png">
</head>

<body>

  <!-- Preloader -->
  <div id="trucker__preloader">
    <div id="trucker__circle_loader"></div>
    <div class="trucker__loader_logo"><img src="assets/images/logo/logo.svg" alt="Preload"></div>
  </div>

  <!-- Scroll To Top -->
  <div class="scroll-up">
    <svg class="scroll-circle svg-content" width="100%" height="100%" viewBox="-1 -1 102 102">
      <path d="M50,1 a49,49 0 0,1 0,98 a49,49 0 0,1 0,-98" />
    </svg>
  </div>

  <!-- Header (Navigation) -->
  <header class="trucker__header-area-home-1">
    <!-- Include full header from template -->
  </header>

  <!-- Main Content Sections -->
  <main>
    <!-- Page-specific sections go here -->
  </main>

  <!-- Footer -->
  <footer class="trucker__footer-area">
    <!-- Include footer from template -->
  </footer>

  <!-- JS Files (match template exactly) -->
  <script src="assets/js/jquery.min.js"></script>
  <script src="assets/js/bootstrap.min.js"></script>
  <script src="assets/js/swiper.js"></script>
  <script src="assets/js/wow.js"></script>
  <script src="assets/js/main.js"></script>
</body>

</html>
```

## Available Page Types

1. **about** - About page with community story and founder info
2. **services** - What We Offer page (jobs, mentorship, events, safety)
3. **jobs** - Job listings page
4. **events** - Events & Hackathons page
5. **blog** - Blog listing page
6. **contact** - Contact page with WhatsApp links and form
7. **team** - Team/Leadership page

## Steps to Create a Page

1. Read the sample template: `docs/sample-html-template/index.html`
2. Copy the HTML structure (head, preloader, scroll-to-top, header, footer)
3. Replace the main content with page-specific sections
4. Update the page title and meta description
5. Update the navigation active state for the current page
6. Apply Sahiwal Tech Community brand colors (see `/apply-colors`)

## Example Usage
```
/create-page about
```
This creates `about.html` with the About page template.

## Notes
- All CSS/JS dependencies must match the template exactly
- The template uses custom class prefixes: `trucker__` - these will be replaced with `stc__` (Sahiwal Tech Community)
- Brand colors will override template colors in the custom CSS
- Mobile-responsive by default (Bootstrap 5)
