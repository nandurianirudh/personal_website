# Anirudh Nanduri - Professional Portfolio

A modern, responsive, and secure professional portfolio website designed to showcase data power, product strategy expertise, and academic achievements. Built with a focus on **Premium Aesthetics (Glassmorphism)** and **Data Security**.

## 🚀 Key Features

### 🎨 UI/UX Design
-   **Glassmorphism Identity**: Extensive use of translucent backgrounds (`backdrop-blur`), subtle gradients, and floating elements for a modern, high-end feel.
-   **Responsive Layout**: Fully adaptive design that works seamlessly on Desktops, Tablets, and Mobile devices.
-   **Interactive Carousels**: Custom-built, single-row horizontal carousels for **Projects** and **Accolades** using CSS Grid for perfect height alignment.
-   **Animations**: Scroll-triggered fade-ins (`IntersectionObserver`), hover lifts, and distinct entrance animations.
-   **Bento Grid Skills**: A modern grid layout for skills and tools.

### 🔒 Security & Protection
This portfolio implements multiple layers of protection for sensitive documents:
-   **Right-Click Disabled**: Global `oncontextmenu="return false"` prevents standard context menus.
-   **Print Protection**: CSS `@media print` blocks hides all content and shows a warning when printing is attempted.
-   **Shortcut Blocking**: JavaScript intercepts and disables `Ctrl+P` / `Cmd+P` commands.
-   **Secure Document Viewer**: Custom Modal for PDF viewing with `#view=FitH` and disabled toolbars to discourage casual downloading/copying.

## 🛠️ Technology Stack

-   **Core**: Semantic HTML5, Vanilla JavaScript (ES6+).
-   **Styling**: 
    -   **Tailwind CSS (v3.4)**: Utility-first framework via CDN for rapid styling.
    -   **Custom CSS**: Specialized classes for glassmorphism, scrollbars, and animations.
-   **Icons**: Heroicons (SVG).
-   **Fonts**: Google Fonts (**Inter** family).

## 📂 Project Structure

```
personal_website/
├── assets/                 # Static assets directory
│   ├── accolades/          # Certificate PDFs
│   ├── generic_logos/      # Company logos
│   ├── profile/            # Profile images
│   └── resume/             # Downloadable Resume PDF
├── index.html              # Main application entry point
├── README.md               # Project documentation
├── extract_pdf.py          # Utility script (Python)
├── parse_resume.py         # Utility script (Python)
└── resume_text.txt         # Content source
```

## ⚙️ How to Run

Since this is a static website, no complex build process is required.

1.  **Local**: Simply double-click `index.html` to open it in any modern web browser.
2.  **Deployment**: content of this folder can be dropped into any static host (GitHub Pages, Netlify, Vercel, or standard Apache/Nginx servers).

## 🌟 Highlights

-   **Split Hero Layout**: Optimized for desktop to balance text density and visual impact.
-   **Smart Modals**: Document viewer specifically tuned for mobile (95% width) and desktop (80% width) for optimal readability.
-   **Performance**: Lightweight assets and clean DOM manipulation ensure fast load times.

---
*Built by [Anirudh Nanduri](https://www.linkedin.com/in/anirudh-nanduri/)*
