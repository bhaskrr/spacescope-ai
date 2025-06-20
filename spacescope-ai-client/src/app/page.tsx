"use client";
import { Header } from "../components/Header";
import { Hero } from "../components/Hero";
import { useState } from "react";

export default function Home() {
  const [isDarkMode, setIsDarkMode] = useState(false)
  function handleDarkModeToggle(){
    setIsDarkMode(prev => !prev)
  }
  return (
    <div className="p-4">
      <Header isDarkMode={isDarkMode} handleModeToggle={handleDarkModeToggle} />
      <Hero isDarkMode={isDarkMode} />
    </div>
  );
}
