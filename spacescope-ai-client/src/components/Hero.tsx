"use client";
import { useState } from "react";
import { Copy, Send, Brain, Database } from "lucide-react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";

type HeroProps = {
  isDarkMode: boolean;
};

type Source = {
  title: string;
  url: string;
};

export function Hero({ isDarkMode }: HeroProps) {
  const [query, setQuery] = useState("");
  const [mode, setMode] = useState("normal");
  const [answer, setAnswer] = useState("");
  const [sources, setSources] = useState([]);
  const [error, setError] = useState("");
  const [isDisabled, setIsDisabled] = useState(true);
  const [isSubmitting, setIsSubmitting] = useState(false);

  function handleInputQueryChange(e: React.ChangeEvent<HTMLInputElement>) {
    const input: string = e.target.value;
    setQuery(input);
    if (!input.trim()) {
      setError("Input can not be empty!");
      setIsDisabled(true);
    } else if (input.trim().length < 10) {
      setError("Input must be atleast 10 characters long.");
    } else {
      setError("");
      setIsDisabled(false);
    }
  }

  async function handleSubmit() {
    setIsSubmitting(true);
    setIsDisabled(true);
    setSources([]);
    setAnswer("");
    setError("");
    try {
      const response = await fetch(`${process.env.NEXT_PUBLIC_ANSWER_URL}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: query, mode: mode }),
      });

      if (!response.ok) {
        setError("Answer generation failed. Please try again.");
      }

      const result = await response.json();

      if (result["answer"]) {
        setAnswer(result["answer"]);
      }

      if (result["metadata"]) {
        setSources(result["metadata"]);
      }
    } finally {
      setIsSubmitting(false);
      setIsDisabled(false);
    }
  }

  function copyAnswer() {
    if (answer) {
      navigator.clipboard.writeText(answer);
    }
  }

  return (
    <main className="text-center min-h-100">
      <div className="text-center mb-6">
        <h2 className="text-4xl md:text-5xl xl:text-6xl font-bold">
          Ask the universe
        </h2>
        <p
          className={`text-2xl md:text-3xl xl:text-4xl tracking-widest ${
            isDarkMode ? "text-gray-300" : "text-gray-600"
          }`}
        >
          Learn something steller
        </p>
      </div>
      <div className="max-w-2xl mx-auto backdrop-blur-sm border border-slate-700/50 rounded-2xl p-6 mb-8 shadow-2xl">
        <div className="mb-2">
          <h3 className="text-left font-semibold mb-2">
            Choose between normal AI responses or RAG mode for context-aware
            answers.
          </h3>
          <div className="flex gap-3">
            <Input
              value={query}
              onChange={handleInputQueryChange}
              type="text"
              placeholder="Ask anything about space..."
              className="h-12 border-slate-600/50 placeholder:text-gray-700 text-base px-4 rounded-xl focus:border-blue-400/50 transition-all duration-200"
            />
            <Button
              variant={mode === "normal" ? "default" : "secondary"}
              onClick={() => setMode("normal")}
              className="h-12 cursor-pointer"
            >
              <Brain />
              Normal
            </Button>
            <Button
              variant={mode === "rag" ? "default" : "secondary"}
              onClick={() => setMode("rag")}
              className="h-12 cursor-pointer"
            >
              <Database />
              RAG
            </Button>
          </div>
        </div>
        <div className="flex justify-between items-center mb-2">
          <p className="text-sm">
            {mode === "normal"
              ? "General AI responses using trained knowledge"
              : "Context-aware responses using retrieved documents"}
          </p>
          <Button
            className="cursor-pointer"
            disabled={isDisabled}
            onClick={handleSubmit}
          >
            {isSubmitting ? (
              <>
                <div className="w-4 h-4 mr-2 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                Asking...
              </>
            ) : (
              <>
                <Send className="w-4 h-4 mr-2" />
                Ask Question
              </>
            )}
          </Button>
        </div>
        {error && (
          <div
            className="flex items-center p-2 mb-4 text-sm text-red-800 border border-red-300 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400 dark:border-red-800"
            role="alert"
          >
            <svg
              className="shrink-0 inline w-4 h-4 me-3"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 20 20"
            >
              <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z" />
            </svg>
            <span className="sr-only">Info</span>
            <div>
              <span className="font-medium">{error}</span>
            </div>
          </div>
        )}
      </div>
      {answer && (
        <div className="max-w-2xl text-left mx-auto backdrop-blur-sm border border-slate-700/50 rounded-2xl p-6 shadow-2xl">
          <div className="mb-4">
            <h4 className="text-lg font-bold mb-4">AI answer</h4>
            <p>{answer}</p>
          </div>
          {sources && sources.length > 0 && (
            <div className="mb-4">
              <h5 className="font-bold mb-2 text-blue-700 dark:text-blue-300 flex items-center gap-2">
                <Database className="inline w-5 h-5" />
                Sources
              </h5>
              <ul className="space-y-3">
                {sources.map((source: Source, index) => (
                  <li
                    key={index}
                    className="bg-slate-100 dark:bg-slate-800 rounded-lg p-3 shadow-sm flex flex-col gap-1 border border-slate-200 dark:border-slate-700"
                  >
                    <span className="font-semibold text-base">
                      {source.url ? (
                        <a
                          href={source.url}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="text-blue-600 dark:text-blue-400 underline hover:text-blue-800"
                        >
                          {source.title || `Source ${index + 1}`}
                        </a>
                      ) : (
                        source.title || `Source ${index + 1}`
                      )}
                    </span>
                  </li>
                ))}
              </ul>
            </div>
          )}

          <Button className="cursor-pointer bg-gray-600" onClick={copyAnswer}>
            <Copy />
            Copy
          </Button>
        </div>
      )}
    </main>
  );
}
