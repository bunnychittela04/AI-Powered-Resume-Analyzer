const form = document.getElementById("analyze-form");
const results = document.getElementById("results");
const scoreEl = document.getElementById("match-score");
const missingEl = document.getElementById("missing-keywords");
const foundEl = document.getElementById("found-skills");
const suggEl = document.getElementById("suggestions-list");
const aiBtn = document.getElementById("ai-btn");

let lastMissing = [];

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const formData = new FormData(form);

  const res = await fetch("/suggest", { method: "POST", body: formData });
  const data = await res.json();
  if (data.error) { alert(data.error); return; }

  // Score
  scoreEl.textContent = (data.match_score ?? 0) + "%";

  // Missing tags
  lastMissing = data.missing_keywords || [];
  missingEl.innerHTML = lastMissing.length
    ? lastMissing.map(k => `<span class="bg-red-100 text-red-800 text-sm px-2 py-1 rounded-full">${k}</span>`).join(" ")
    : `<span class="text-green-700">Great job! All key skills from the JD were found.</span>`;

  // Found tags
  const found = data.found_skills || [];
  foundEl.innerHTML = found.length
    ? found.map(k => `<span class="bg-green-100 text-green-800 text-sm px-2 py-1 rounded-full">${k}</span>`).join(" ")
    : `<span class="text-gray-500">No common skills found.</span>`;

  // Suggestions list
  const suggestions = data.suggestions || [];
  suggEl.classList.remove("italic");
  suggEl.innerHTML = suggestions.length
    ? `<ul class="list-disc ml-6">${suggestions.map(s => `<li>${s}</li>`).join("")}</ul>`
    : `<span class="text-gray-500 italic">Click the button above to get tailored suggestions for improvement.</span>`;

  results.classList.remove("hidden");
});

// Optional: client-side “AI-powered suggestions” placeholder (no external API key needed)
aiBtn.addEventListener("click", () => {
  if (!lastMissing.length) {
    suggEl.innerHTML = "Your resume is a great match! Consider adding measurable impact (%, time saved, $).";
    return;
  }
  const tips = [
    "Create a 'Technical Skills' section near the top.",
    "Add 2–3 bullets under recent roles showing how you used the missing skills.",
    "Include tools, versions, and quantifiable impact."
  ];
  suggEl.classList.remove("italic");
  suggEl.innerHTML = `
    <p class="mb-2"><b>Missing Keywords:</b> ${lastMissing.join(", ")}</p>
    <ul class="list-disc ml-6">${tips.map(t => `<li>${t}</li>`).join("")}</ul>
  `;
});
