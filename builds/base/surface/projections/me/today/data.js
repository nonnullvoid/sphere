// Derived view data, rendered from the sources. Rewritten at every render; never edited by hand.
window.VIEW_DATA = {
  title: "Today",
  subtitle: "What's waiting, what you're in the middle of, and what's next.",
  generated: "",
  sources: ["layers/focus", "layers/work/index.md", "layers/ideas"],
  panels: [
    { title: "Waiting on you", kind: "list", items: [], empty: "Nothing waiting." },
    { title: "In the middle of", kind: "list", items: [], empty: "Nothing open yet." },
    { title: "Next up", kind: "list", items: [], empty: "No work yet. Tell me what you're working on." },
    { title: "Ideas", kind: "stats", items: [], empty: "No ideas caught yet." },
  ],
};
