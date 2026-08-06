import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

// CHANGE THIS PART:
export const metadata: Metadata = {
  title: "AgriScan AI 🌿 | Smart Pest Detection",
  description: "AI-powered crop pest and disease detection for modern farmers.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  );
}