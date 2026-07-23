This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
🌿 AgriScan AI: Intelligent Pest Detection & Crop Management
First-Prize Winning Hackathon Project – An advanced, production-grade agricultural platform that leverages Computer Vision and LLMs to detect crop pests and diagnose diseases in real-time.

Tech Stack

📸 Overview
AgriScan AI bridges the gap between cutting-edge AI and everyday farming. Users can upload or capture images of crops via a web application, instantly receiving AI-powered diagnoses, confidence scores, and actionable organic/chemical treatment plans.

✨ Key Features
AI Vision Diagnosis: Powered by Google Gemini 1.5 Flash for instant pest and disease recognition.
Structured Reports: AI returns structured JSON containing disease name, confidence score, and treatment plans.
Secure Authentication: JWT-based user registration and login.
PostgreSQL Database: Stores user profiles and scan history securely.
Premium UI/UX: Built with Next.js, Tailwind CSS, and modern glassmorphism design principles.
🛠️ Tech Stack
Frontend: Next.js (App Router), TypeScript, Tailwind CSS
Backend: Python, FastAPI, SQLAlchemy, Pydantic
Database: PostgreSQL
AI/ML: Google Gemini Vision API
Security: Passlib (Bcrypt hashing), Python-Jose (JWT)
🚀 Getting Started
Prerequisites
Node.js (v18+)
Python (v3.10+)
PostgreSQL
Backend Setup (/backend)
Create a virtual environment: python -m venv venv
Activate it: source venv/bin/activate (Mac) or venv\Scripts\activate (Windows)
Install dependencies: pip install -r requirements.txt
Create a .env file with your database URL, Secret Key, and Gemini API Key.
Run the server: uvicorn main:app --reload
Frontend Setup (/frontend)
Install dependencies: npm install
Run the dev server: npm run dev
Open http://localhost:3000 in your browser.
📂 Folder Structure
agriscan-ai/├── backend/               # FastAPI application│   ├── api/endpoints/     # API routes (auth, scans)│   ├── core/              # Database config, security│   ├── models/            # SQLAlchemy DB models│   ├── schemas/           # Pydantic validation│   └── services/          # AI logic (Gemini integration)└── frontend/              # Next.js application    └── src/app/           # Main UI components
🏗️ Future Roadmap
YOLOv11 integration for precise bounding boxes on pests.
Offline mode for farmers in remote areas.
Satellite data integration for early outbreak prediction.
