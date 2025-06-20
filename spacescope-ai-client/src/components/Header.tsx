import Image from "next/image";
import Link from "next/link";
import { Sun, Moon } from "lucide-react";

type HeaderProps = {
  isDarkMode: boolean;
  handleModeToggle: () => void;
};

export function Header({ isDarkMode, handleModeToggle }: HeaderProps) {
  return (
    <header className="p-2 rounded-full flex justify-between items-center">
      <div className="p-2 flex items-center gap-2">
        <Image
          src="/logo.svg"
          alt="Logo"
          width={30}
          height={30}
          className="bg-white rounded-full"
        />
        <h1 className="text-xl">SpaceScope AI</h1>
      </div>
      <div className="flex gap-2">
        <button
          className="p-2 cursor-pointer rounded-full"
          onClick={handleModeToggle}
        >
          {isDarkMode ? <Sun /> : <Moon />}
        </button>
        <Link href="https://github.com/bhaskrr/spacescope-ai" target="blank">
          <button className="p-2 cursor-pointer rounded-full">
            <Image
              src="/github-icon.svg"
              alt="github icon"
              width={24}
              height={24}
            />
          </button>
        </Link>
      </div>
    </header>
  );
}
