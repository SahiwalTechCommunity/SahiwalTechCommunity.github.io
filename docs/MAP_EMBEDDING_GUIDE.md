# Map Embedding Guide for Sahiwal Tech Companies

## Overview

This guide explains how to embed an interactive map showing IT companies in Sahiwal, Pakistan on the website.

---

## Option 1: Google Maps Embed

### Basic Google Maps Embed with Search Query

```html
<iframe
  src="https://www.google.com/maps?q=IT+companies+Sahiwal&output=embed"
  width="100%"
  height="450"
  style="border:0;"
  allowfullscreen=""
  loading="lazy"
  title="IT Companies in Sahiwal">
</iframe>
```

### Custom Google My Maps

For more control over markers and company information:

1. Go to [Google My Maps](https://www.google.com/mymaps)
2. Create a new map
3. Add markers for each IT company manually
4. Use the "Embed on my site" option to get the embed code

**Advantages:**
- Familiar Google Maps interface
- Easy to create and maintain
- Mobile-friendly

**Disadvantages:**
- Limited customization
- Requires manual marker creation
- Google API quota limits may apply

---

## Option 2: OpenStreetMap with Leaflet.js (Recommended)

OpenStreetMap is completely free and offers full customization using Leaflet.js.

### Complete Implementation

```html
<!-- Include Leaflet CSS/JS -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<!-- Map container -->
<div id="stc-companies-map" style="height: 500px; width: 100%; border-radius: 20px;"></div>

<script>
// Initialize map centered on Sahiwal
const map = L.map('stc-companies-map').setView([30.6668, 73.0946], 14);

// Add OpenStreetMap tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Company data with coordinates
const companies = [
  {
    name: "Million Miles Technologies",
    lat: 30.668,
    lng: 73.095,
    address: "Farid Town, Sahiwal",
    phone: "+92 XXX XXXXXXX",
    website: "https://millionmiles.com",
    description: "Software development and IT solutions"
  },
  {
    name: "The Tech Axe",
    lat: 30.665,
    lng: 73.092,
    address: "Farid Town, Sahiwal",
    phone: "+92 XXX XXXXXXX",
    website: "https://thetechaxe.com",
    description: "Tech training and internship programs"
  },
  {
    name: "Wateen",
    lat: 30.667,
    lng: 73.098,
    address: "Main Boulevard, Sahiwal",
    phone: "+92 XXX XXXXXXX",
    website: "https://wateen.com",
    description: "Internet and telecommunications"
  },
  // Add more companies as needed
];

// Custom icon for company markers
const companyIcon = L.divIcon({
  className: 'custom-marker',
  html: '<div style="background: var(--stc-green-light); width: 30px; height: 30px; border-radius: 50%; border: 3px solid white; box-shadow: 0 2px 10px rgba(0,0,0,0.3);"></div>',
  iconSize: [30, 30],
  iconAnchor: [15, 15]
});

// Add markers for each company
companies.forEach(company => {
  const marker = L.marker([company.lat, company.lng], { icon: companyIcon })
    .addTo(map);

  // Create popup with company info
  const popupContent = `
    <div style="font-family: 'DM Sans', sans-serif; min-width: 200px;">
      <h3 style="margin: 0 0 8px 0; color: var(--stc-green-primary);">${company.name}</h3>
      <p style="margin: 0 0 8px 0; font-size: 14px; color: #666;">${company.description}</p>
      <div style="margin: 4px 0;">
        <strong>📍</strong> ${company.address}
      </div>
      <div style="margin: 4px 0;">
        <strong>📞</strong> <a href="tel:${company.phone}" style="color: var(--stc-green-light);">${company.phone}</a>
      </div>
      <div style="margin: 4px 0;">
        <strong>🌐</strong> <a href="${company.website}" target="_blank" style="color: var(--stc-green-light);">Visit Website</a>
      </div>
    </div>
  `;

  marker.bindPopup(popupContent);
});
</script>
```

### Styling the Map

Add this CSS to match STC branding:

```css
#stc-companies-map {
  border: 2px solid rgba(45, 158, 71, 0.2);
}

.leaflet-popup-content-wrapper {
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
}

.leaflet-popup-tip {
  background: white;
}

.custom-marker {
  transition: transform 0.2s ease;
}

.custom-marker:hover {
  transform: scale(1.2);
}
```

**Advantages:**
- Completely free, no API key needed
- Fully customizable styling
- No quota limits
- Fast loading
- Mobile-responsive

**Disadvantages:**
- Requires JavaScript knowledge
- Need to maintain company data

---

## Option 3: Static Map Image

For a simpler approach, use a static map image:

```html
<div style="position: relative;">
  <img
    src="https://maps.googleapis.com/maps/api/staticmap?center=Sahiwal,Pakistan&zoom=13&size=800x400&maptype=roadmap&markers=color:0x2d9e47|Sahiwal"
    alt="IT Companies in Sahiwal Map"
    style="width: 100%; height: auto; border-radius: 20px;">
</div>
```

---

## Integration: IT Companies Page

### Page Structure

Create `companies.html` with the following sections:

1. **Hero Section**
   - Title: "Sahiwal's Tech Ecosystem"
   - Subtitle: "Discover IT companies driving innovation in our city"

2. **Map Section**
   - Full-width interactive map
   - Company markers with popups

3. **Company Directory Grid**
   - Cards for each company with:
     - Company logo
     - Company name
     - Address
     - Phone number
     - Website link
     - Description
     - "View on Map" button

4. **Add Your Company CTA**
   - Form for companies to submit their info
   - Community review process

### Company Card Component

```html
<div class="company-card">
  <div class="company-logo">
    <img src="assets/images/companies/company-logo.png" alt="Company Name">
  </div>
  <div class="company-info">
    <h3>Company Name</h3>
    <p class="company-description">Brief description of what the company does...</p>
    <ul class="company-details">
      <li>📍 Address, Sahiwal</li>
      <li>📞 <a href="tel:+92XXXXXXXXXX">+92 XXX XXXXXXX</a></li>
      <li>🌐 <a href="https://companywebsite.com" target="_blank">companywebsite.com</a></li>
    </ul>
    <div class="company-actions">
      <a href="#" class="btn-primary">View on Map</a>
      <a href="https://companywebsite.com" class="btn-secondary">Visit Website</a>
    </div>
  </div>
</div>
```

### Company Card Styling

```css
.company-card {
  background: white;
  border-radius: 20px;
  padding: 32px;
  border: 1.5px solid rgba(45, 158, 71, 0.1);
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.08);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.company-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
}

.company-logo {
  height: 60px;
  margin-bottom: 20px;
}

.company-logo img {
  max-height: 100%;
  width: auto;
}

.company-info h3 {
  font-family: 'Playfair Display', serif;
  font-weight: 700;
  color: var(--stc-text);
  margin-bottom: 8px;
}

.company-description {
  color: var(--stc-text-light);
  margin-bottom: 16px;
  line-height: 1.6;
}

.company-details {
  list-style: none;
  padding: 0;
  margin-bottom: 20px;
}

.company-details li {
  padding: 8px 0;
  color: var(--stc-text);
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
}

.company-details li a {
  color: var(--stc-green-light);
  text-decoration: none;
}

.company-details li a:hover {
  text-decoration: underline;
}

.company-actions {
  display: flex;
  gap: 12px;
}
```

---

## Getting Company Coordinates

To find precise coordinates for each company:

1. **Using Google Maps:**
   - Search for the company address
   - Right-click on the location
   - Copy the coordinates from the popup

2. **Using OpenStreetMap:**
   - Go to [OpenStreetMap](https://www.openstreetmap.org)
   - Search for the address
   - Click on the location
   - Coordinates appear in the left sidebar

---

## Data Structure for Companies

Store company data in a JavaScript object for easy management:

```javascript
const sahiwalITCompanies = [
  {
    id: 1,
    name: "Million Miles Technologies",
    slug: "million-miles-technologies",
    logo: "assets/images/companies/million-miles.png",
    address: "Farid Town, Sahiwal, Punjab, Pakistan",
    phone: "+92 XXX XXXXXXX",
    email: "info@millionmiles.com",
    website: "https://millionmiles.com",
    description: "Leading software development company providing custom IT solutions, web development, and mobile app development services.",
    founded: "20XX",
    employees: "XX-XX",
    specialties: ["Web Development", "Mobile Apps", "Custom Software"],
    lat: 30.668,
    lng: 73.095,
    featured: true
  },
  {
    id: 2,
    name: "The Tech Axe",
    slug: "the-tech-axe",
    logo: "assets/images/companies/tech-axe.png",
    address: "Farid Town, Sahiwal, Punjab, Pakistan",
    phone: "+92 XXX XXXXXXX",
    email: "info@thetechaxe.com",
    website: "https://thetechaxe.com",
    description: "Tech education platform offering internships, training programs, and skill development courses for students and professionals.",
    founded: "20XX",
    employees: "XX-XX",
    specialties: ["Training", "Internships", "Skill Development"],
    lat: 30.665,
    lng: 73.092,
    featured: true
  },
  {
    id: 3,
    name: "Wateen",
    slug: "wateen",
    logo: "assets/images/companies/wateen.png",
    address: "Main Boulevard, Sahiwal, Punjab, Pakistan",
    phone: "+92 XXX XXXXXXX",
    email: "info@wateen.com",
    website: "https://wateen.com",
    description: "Telecommunications company providing broadband internet, fiber optics, and connectivity solutions across Pakistan.",
    founded: "20XX",
    employees: "XXX-XXX",
    specialties: ["Internet", "Telecom", "Fiber Optics"],
    lat: 30.667,
    lng: 73.098,
    featured: true
  }
  // Add more companies...
];
```

---

## Navigation Update

Add the IT Companies page to the main navigation:

```html
<nav>
  <ul>
    <li><a href="index.html">Home</a></li>
    <li><a href="about.html">About</a></li>
    <li><a href="services.html">Services</a></li>
    <li><a href="jobs.html">Jobs</a></li>
    <li><a href="companies.html">IT Companies</a></li>
    <li><a href="events.html">Events</a></li>
    <li><a href="blog.html">Blog</a></li>
    <li><a href="contact.html">Contact</a></li>
  </ul>
</nav>
```

---

## Summary: Recommended Approach

For the Sahiwal Tech Community website, I recommend:

1. **Use OpenStreetMap with Leaflet.js** for the interactive map
   - Free and unlimited
   - Fully customizable to match STC branding
   - Fast loading
   - No API key required

2. **Create a dedicated `companies.html` page** with:
   - Full-width interactive map at the top
   - Company directory grid below with detailed cards
   - Each card shows: logo, name, address, phone, website, description
   - "View on Map" button on each card that zooms to that marker

3. **Add company data to the Jobs page** as well
   - Show hiring companies with links to their profiles

4. **Maintain company data in a central JSON file**
   - Easy to update
   - Can be loaded dynamically
   - Can be used for search/filter functionality

---

*Last Updated: 2025-03-09*
