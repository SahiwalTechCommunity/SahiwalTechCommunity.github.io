# Footer Component - Founder & Developer Credits

## Overview

This document specifies how to display founder and developer credits in the website footer and About page.

---

## People Information

### Founder: Kashif Sohail
- **Name:** Kashif Sohail
- **Role:** AI Data Engineer
- **LinkedIn:** https://www.linkedin.com/in/kshfse/
- **Founded:** June 2023

### Website Developer: Javeed Ishaq
- **Name:** Javeed Ishaq
- **LinkedIn:** https://www.linkedin.com/in/javeed-ishaq/
- **Role:** Website Designer & Developer

---

## Footer Structure

### Layout
```
┌─────────────────────────────────────────────────────────────┐
│                    SAHIWAL TECH COMMUNITY                    │
│                  Knowledge is for Everyone                    │
├─────────────────────────────────────────────────────────────┤
│  About  |  Services  |  Jobs  |  Companies  |  Contact      │
├─────────────────────────────────────────────────────────────┤
│  Founded by Kashif Sohail  |  [LinkedIn Icon]               │
│  [WhatsApp Join Link]                                         │
├─────────────────────────────────────────────────────────────┤
│  © 2025 Sahiwal Tech Community. All rights reserved.        │
│  Crafted with 💚 by <a href="...">Javeed Ishaq</a>          │
└─────────────────────────────────────────────────────────────┘
```

### HTML Template

```html
<footer class="stc__footer-area">
  <div class="stc__container">
    <!-- Main Footer Content -->
    <div class="stc__footer-wrapper">

      <!-- Left Column - Community Info -->
      <div class="stc__footer-about">
        <a href="index.html" class="stc__footer-logo">
          <img src="assets/images/logo/logo.svg" alt="Sahiwal Tech Community">
        </a>
        <p class="stc__footer-tagline">Knowledge is for Everyone</p>
        <p class="stc__footer-description">
          Sahiwal's premier tech community connecting professionals,
          sharing opportunities, and growing together since 2023.
        </p>
      </div>

      <!-- Middle Column - Quick Links -->
      <div class="stc__footer-links">
        <h4>Quick Links</h4>
        <ul>
          <li><a href="about.html">About Us</a></li>
          <li><a href="services.html">Services</a></li>
          <li><a href="jobs.html">Jobs</a></li>
          <li><a href="companies.html">IT Companies</a></li>
          <li><a href="events.html">Events</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>

      <!-- Right Column - Founder & Contact -->
      <div class="stc__footer-contact">
        <h4>Founder</h4>
        <div class="stc__founder-info">
          <span class="stc__founder-name">Kashif Sohail</span>
          <span class="stc__founder-role">AI Data Engineer</span>
          <a href="https://www.linkedin.com/in/kshfse/" target="_blank" class="stc__linkedin-link" aria-label="Connect with Kashif Sohail on LinkedIn">
            <i class="fa-brands fa-linkedin"></i> Connect on LinkedIn
          </a>
        </div>

        <div class="stc__whatsapp-cta">
          <a href="https://chat.whatsapp.com/HS0ZesKSH9gB3lHulLQ1c7" class="stc__btn-whatsapp">
            <i class="fa-brands fa-whatsapp"></i> Join Community
          </a>
        </div>
      </div>
    </div>

    <!-- Bottom Footer - Copyright & Developer Credit -->
    <div class="stc__footer-bottom">
      <div class="stc__copyright">
        © <span id="current-year">2025</span> Sahiwal Tech Community. All rights reserved.
      </div>
      <div class="stc__developer-credit">
        <span>Crafted with </span>
        <span class="stc__heart">💚</span>
        <span> by </span>
        <a href="https://www.linkedin.com/in/javeed-ishaq/" target="_blank" class="stc__dev-link">
          Javeed Ishaq
        </a>
      </div>
    </div>
  </div>
</footer>
```

---

## CSS Styling

```css
/* Footer Container */
.stc__footer-area {
  background: var(--stc-dark);
  padding: 80px 0 30px;
  position: relative;
}

/* Footer Wrapper */
.stc__footer-wrapper {
  display: grid;
  grid-template-columns: 2fr 1fr 1.5fr;
  gap: 40px;
  margin-bottom: 40px;
}

/* Footer About Section */
.stc__footer-about {
  padding-right: 20px;
}

.stc__footer-logo img {
  height: 50px;
  margin-bottom: 20px;
}

.stc__footer-tagline {
  font-family: 'Playfair Display', serif;
  font-size: 18px;
  color: var(--stc-gold-light);
  margin-bottom: 16px;
}

.stc__footer-description {
  color: rgba(255, 255, 255, 0.7);
  line-height: 1.7;
  font-size: 15px;
}

/* Footer Links */
.stc__footer-links h4,
.stc__footer-contact h4 {
  font-family: 'Playfair Display', serif;
  font-size: 20px;
  color: var(--stc-white);
  margin-bottom: 20px;
}

.stc__footer-links ul {
  list-style: none;
}

.stc__footer-links ul li {
  margin-bottom: 12px;
}

.stc__footer-links ul li a {
  color: rgba(255, 255, 255, 0.7);
  text-decoration: none;
  transition: color 0.3s ease;
}

.stc__footer-links ul li a:hover {
  color: var(--stc-green-light);
}

/* Founder Info */
.stc__founder-info {
  background: rgba(255, 255, 255, 0.05);
  padding: 20px;
  border-radius: 12px;
  margin-bottom: 20px;
}

.stc__founder-name {
  display: block;
  font-size: 18px;
  font-weight: 600;
  color: var(--stc-white);
  margin-bottom: 4px;
}

.stc__founder-role {
  display: block;
  font-size: 14px;
  color: rgba(255, 255, 255, 0.6);
  margin-bottom: 12px;
}

.stc__linkedin-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  color: var(--stc-green-light);
  text-decoration: none;
  font-size: 14px;
  transition: color 0.3s ease;
}

.stc__linkedin-link:hover {
  color: var(--stc-green-light);
  text-decoration: underline;
}

/* WhatsApp CTA */
.stc__whatsapp-cta .stc__btn-whatsapp {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: #25D366;
  color: white;
  padding: 12px 24px;
  border-radius: 50px;
  text-decoration: none;
  font-weight: 600;
  transition: background 0.3s ease;
}

.stc__whatsapp-cta .stc__btn-whatsapp:hover {
  background: #128C7E;
}

/* Footer Bottom */
.stc__footer-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 30px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.stc__copyright {
  color: rgba(255, 255, 255, 0.5);
  font-size: 14px;
}

/* Developer Credit */
.stc__developer-credit {
  display: flex;
  align-items: center;
  gap: 4px;
  color: rgba(255, 255, 255, 0.5);
  font-size: 14px;
}

.stc__heart {
  animation: heartbeat 1.5s ease infinite;
}

@keyframes heartbeat {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.2); }
}

.stc__dev-link {
  color: var(--stc-gold-light);
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s ease;
}

.stc__dev-link:hover {
  color: var(--stc-gold-primary);
  text-decoration: underline;
}

/* Responsive */
@media (max-width: 991px) {
  .stc__footer-wrapper {
    grid-template-columns: 1fr;
    gap: 30px;
  }

  .stc__footer-bottom {
    flex-direction: column;
    gap: 16px;
    text-align: center;
  }

  .stc__developer-credit {
    justify-content: center;
  }
}
```

---

## Alternative Credit Text Options

Choose one of these for the developer credit in the footer:

1. **"Crafted with 💚 by Javeed Ishaq"** (Recommended)
2. **"Made with care by Javeed Ishaq"**
3. **"Website by Javeed Ishaq"**
4. **"Designed & developed by Javeed Ishaq"**
5. **"Built with 💚 by Javeed Ishaq"**

---

## About Page - Founder Section

Include this section on the About page:

```html
<section class="stc__founder-section">
  <div class="stc__container">
    <div class="stc__founder-wrapper">
      <div class="stc__founder-image">
        <img src="assets/images/team/kashif-sohail.jpg" alt="Kashif Sohail - Founder">
      </div>
      <div class="stc__founder-content">
        <span class="stc__founder-label">Founder & Community Lead</span>
        <h2 class="stc__founder-name">Kashif Sohail</h2>
        <p class="stc__founder-role">AI Data Engineer</p>
        <p class="stc__founder-bio">
          Kashif founded Sahiwal Tech Community in June 2023 with a simple mission:
          to create a platform where knowledge, opportunities, and guidance flow freely
          to those who need it most. What started as a small group has grown into a
          thriving community of nearly 1,000 tech professionals across three WhatsApp groups.
        </p>
        <a href="https://www.linkedin.com/in/kshfse/" target="_blank" class="stc__btn-primary">
          <i class="fa-brands fa-linkedin"></i> Connect on LinkedIn
        </a>
      </div>
    </div>
  </div>
</section>
```

---

## Quick Reference

| Person | Role | LinkedIn |
|--------|------|----------|
| Kashif Sohail | Founder | https://www.linkedin.com/in/kshfse/ |
| Javeed Ishaq | Website Developer | https://www.linkedin.com/in/javeed-ishaq/ |

---

*Last Updated: 2025-03-09*
