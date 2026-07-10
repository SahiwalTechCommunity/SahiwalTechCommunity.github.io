# Angular + Supabase + GitHub Pages Plan

For this project, the cleanest zero-cost architecture is:

`Angular + Supabase + GitHub Pages`

Use Angular for the public site and admin panel, Supabase for auth/database/storage, and GitHub Pages only for static hosting. This works because Angular is a SPA framework designed for static deployment, while Supabase handles login and data APIs from the browser.

Official references:
- https://angular.dev/guide/routing
- https://angular.dev/tools/cli/deployment
- https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
- https://supabase.com/docs/guides/getting-started/tutorials/with-angular
- https://supabase.com/docs/guides/auth/

## Architecture

### Frontend
- Angular standalone app
- Public routes for homepage, about, services, jobs, events, companies, blog, contact
- Protected `/admin` area for superadmin/editor

### Backend
- Supabase Postgres for content
- Supabase Auth for login
- Supabase Storage for images
- Supabase Row Level Security for authorization

### Hosting
- GitHub Pages serves the built Angular app
- GitHub Actions builds and deploys `dist/`

### Important constraint
- GitHub Pages has no server runtime
- So all protection must be enforced by Supabase policies, not by GitHub Pages
- Angular route guards improve UX, but real security is in Supabase RLS

## Recommended Folder Plan

```txt
sahiwal-tech-community/
├── docs/
│   └── html-webiste/
├── public/
│   ├── assets/
│   │   ├── images/
│   │   ├── fonts/
│   │   ├── css/
│   │   └── js/
│   └── favicon.ico
├── src/
│   ├── app/
│   │   ├── core/
│   │   │   ├── config/
│   │   │   │   └── app.config.ts
│   │   │   ├── guards/
│   │   │   │   ├── auth.guard.ts
│   │   │   │   └── admin.guard.ts
│   │   │   ├── interceptors/
│   │   │   ├── models/
│   │   │   │   ├── event.model.ts
│   │   │   │   ├── job.model.ts
│   │   │   │   ├── company.model.ts
│   │   │   │   ├── blog-post.model.ts
│   │   │   │   └── user-profile.model.ts
│   │   │   ├── services/
│   │   │   │   ├── supabase.service.ts
│   │   │   │   ├── auth.service.ts
│   │   │   │   ├── events.service.ts
│   │   │   │   ├── jobs.service.ts
│   │   │   │   ├── companies.service.ts
│   │   │   │   ├── blog.service.ts
│   │   │   │   ├── settings.service.ts
│   │   │   │   └── storage.service.ts
│   │   │   └── utils/
│   │   ├── shared/
│   │   │   ├── components/
│   │   │   │   ├── header/
│   │   │   │   ├── footer/
│   │   │   │   ├── hero/
│   │   │   │   ├── section-title/
│   │   │   │   ├── stat-card/
│   │   │   │   ├── event-card/
│   │   │   │   ├── job-card/
│   │   │   │   ├── company-card/
│   │   │   │   ├── blog-card/
│   │   │   │   └── loading-spinner/
│   │   │   ├── pipes/
│   │   │   └── directives/
│   │   ├── features/
│   │   │   ├── public/
│   │   │   │   ├── home/
│   │   │   │   ├── about/
│   │   │   │   ├── services/
│   │   │   │   ├── jobs/
│   │   │   │   ├── events/
│   │   │   │   ├── companies/
│   │   │   │   ├── blog/
│   │   │   │   └── contact/
│   │   │   ├── auth/
│   │   │   │   ├── login/
│   │   │   │   └── callback/
│   │   │   └── admin/
│   │   │       ├── layout/
│   │   │       ├── dashboard/
│   │   │       ├── events-admin/
│   │   │       ├── jobs-admin/
│   │   │       ├── companies-admin/
│   │   │       ├── blog-admin/
│   │   │       ├── media-admin/
│   │   │       └── settings-admin/
│   │   ├── app.routes.ts
│   │   ├── app.component.ts
│   │   ├── app.component.html
│   │   └── app.component.css
│   ├── environments/
│   │   ├── environment.ts
│   │   └── environment.prod.ts
│   ├── styles.css
│   └── main.ts
├── supabase/
│   ├── migrations/
│   ├── seed.sql
│   └── policies.sql
├── .github/
│   └── workflows/
│       └── deploy-pages.yml
├── angular.json
├── package.json
└── README.md
```

## Database Design

Create these tables first:

- `profiles`
- `events`
- `jobs`
- `companies`
- `blog_posts`
- `site_settings`

Suggested minimum columns:

### `profiles`
- `id uuid primary key`
- `email text`
- `role text`
- `full_name text`
- `created_at timestamptz`

### `events`
- `id uuid`
- `slug text unique`
- `title text`
- `summary text`
- `content text`
- `event_date timestamptz`
- `location text`
- `cover_image_url text`
- `published boolean`
- `created_at timestamptz`

### `jobs`
- `id uuid`
- `title text`
- `company text`
- `location text`
- `job_type text`
- `apply_url text`
- `description text`
- `published boolean`
- `expires_at timestamptz`

### `companies`
- `id uuid`
- `slug text unique`
- `name text`
- `description text`
- `website text`
- `map_url text`
- `logo_url text`
- `published boolean`

### `blog_posts`
- `id uuid`
- `slug text unique`
- `title text`
- `excerpt text`
- `content text`
- `cover_image_url text`
- `published boolean`
- `published_at timestamptz`

### `site_settings`
- `id uuid`
- `key text unique`
- `value jsonb`

## Roles and Security

Use one role model only at first:

- `superadmin`
- optional later: `editor`

Policy strategy:

- Public users can `select` only rows where `published = true`
- Logged-in admins can `insert`, `update`, `delete`
- Storage buckets should allow public read, admin write

Example logic:
- `events`, `jobs`, `companies`, `blog_posts`: public read on published content
- `profiles`: only user can read own profile, admin can read admin-needed rows
- `site_settings`: public read only for safe/public keys, admin full access

Do not trust Angular alone for security. Supabase Auth uses JWTs and is designed to work with RLS for authorization. That is the core safety mechanism.

Source:
- https://supabase.com/docs/guides/auth/

## Route Plan

### Public
- `/`
- `/about`
- `/services`
- `/jobs`
- `/events`
- `/companies`
- `/blog`
- `/contact`

### Auth
- `/login`
- `/auth/callback`

### Admin
- `/admin`
- `/admin/events`
- `/admin/jobs`
- `/admin/companies`
- `/admin/blog`
- `/admin/media`
- `/admin/settings`

## Step-by-Step Build Plan

1. Preserve the current site.
   Copy the existing HTML/CSS/JS site into `docs/html-webiste/`.

2. Create the Angular app.
   Use a standalone Angular app with routing enabled.
   Angular’s current docs recommend modern standalone patterns.

3. Add Supabase client.
   Install `@supabase/supabase-js` and create a single `supabase.service.ts` to initialize the client.

4. Set environments.
   Add `supabaseUrl` and `supabaseAnonKey` in `src/environments/`.
   The anon key is safe in the frontend when RLS is configured correctly; Supabase’s Angular tutorial states this explicitly.

5. Build the app shell.
   Create:
   - global layout
   - header
   - footer
   - mobile nav
   - shared cards and section components

6. Migrate static assets.
   Move images/fonts to `public/assets/`.
   Convert repeated HTML sections into Angular shared components.

7. Migrate public pages first.
   Build the public pages as feature folders under `features/public/`.
   Initially use static mock data so layout work is independent from backend setup.

8. Create Supabase schema.
   Add SQL migrations for the tables above.
   Create a `profiles` row automatically on signup if needed.

9. Add authentication.
   Create:
   - `auth.service.ts`
   - `login` page
   - session state handling
   - sign-in/sign-out methods
   Start with email/password auth.

10. Add route guards.
    `auth.guard.ts` checks for a session.
    `admin.guard.ts` checks that the signed-in user has role `superadmin`.

11. Add RLS policies.
    Implement RLS before wiring admin CRUD.
    This is mandatory since the app runs client-side on GitHub Pages.

12. Build admin layout.
    Create:
    - admin sidebar
    - dashboard
    - CRUD pages for events/jobs/companies/blog/settings

13. Connect public pages to Supabase.
    Replace mock data with service calls:
    - `events.service.ts`
    - `jobs.service.ts`
    - `companies.service.ts`
    - `blog.service.ts`

14. Add image upload flow.
    Use Supabase Storage for:
    - event banners
    - company logos
    - blog cover images
    Store returned URLs in the relevant tables.

15. Add basic content management UX.
    In admin pages:
    - list entries
    - create/edit form
    - publish/unpublish toggle
    - delete confirmation

16. Configure routing for GitHub Pages.
    Angular routing is SPA-based. Deep links on static hosts need special handling.
    Best practical option:
    - use path-based routes
    - deploy a `404.html` fallback that loads the Angular app
    Alternative:
    - use hash routing if you want the simplest Pages behavior, but URLs are uglier

17. Add GitHub Pages workflow.
    Use GitHub Actions custom workflow to build and deploy `dist/` to Pages. GitHub documents this flow officially.

18. Test production behavior.
    Verify:
    - direct opening `/events`
    - admin login
    - logout
    - unauthorized users blocked from admin
    - published content visible publicly
    - unpublished content hidden publicly

19. Add polish.
    Move old CSS carefully into Angular global styles.
    Then gradually refactor page-by-page into cleaner component styles.

20. Document the content workflow.
    Write a short admin guide:
    - how to log in
    - how to add event
    - how to upload image
    - how to publish post

## Recommended Service Responsibilities

### `auth.service.ts`
- sign in
- sign out
- get current session
- observe auth state
- check current user role

### `events.service.ts`
- list public events
- list admin events
- create event
- update event
- delete event

### `storage.service.ts`
- upload image
- delete image
- generate public URLs

### `settings.service.ts`
- load home page text
- update contact/social/WhatsApp links

## GitHub Pages Deployment Shape

Use a workflow like this conceptually:

1. Checkout repo
2. Install Node dependencies
3. Run Angular production build
4. Copy SPA fallback if needed
5. Upload `dist/.../browser` or `dist/...` as Pages artifact
6. Deploy with Pages action

Use GitHub custom Pages workflow, not manual branch pushes. GitHub supports this directly.

Source:
- https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages

## Recommended Build Sequence For This Project

1. Preserve current HTML in `docs/html-webiste`
2. Scaffold Angular app
3. Migrate shared header/footer/styles
4. Build homepage
5. Build about/services/contact
6. Build events/jobs/companies/blog public pages
7. Create Supabase schema
8. Add auth
9. Build admin panel
10. Connect CRUD and storage
11. Deploy to GitHub Pages

## Practical Recommendation

Start with only these editable modules in v1:

- Events
- Blog
- Companies
- Site settings

Keep `about` and `services` static initially. That reduces complexity and gets value faster.

## Next Step

Turn this into a concrete implementation checklist for the repo, including:

- exact Angular route map
- exact Supabase SQL schema
- exact RLS policies
- exact GitHub Actions workflow structure
