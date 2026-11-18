// Sphere chrome: the shared components every projection uses.
//   top bar and navigation (built from registry.js, never written into pages),
//   freshness badge, panels, footer with provenance.
// Plain JavaScript, no build step, works from a double-clicked file.
// Load registry.js first, then this file:
//   <script src="../../assets/registry.js"></script>
//   <script src="../../assets/sphere-chrome.js"></script>
(function () {
  "use strict";

  // assets/ → projections/ → surface/ → the sphere's root. Registry homes are relative to the root.
  var script = document.currentScript;
  var root = script ? new URL("../../../", script.src) : new URL("./", location.href);
  var registry = window.SPHERE || { name: "", projections: [] };

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text != null) node.textContent = text;
    return node;
  }

  /** The URL a projection opens at. Markdown views open in the index page's viewer. */
  function hrefFor(entry) {
    var home = entry.home || "";
    if (entry.opens === "markdown") {
      return new URL("surface/projections.html?view=" + encodeURIComponent(home), root).href;
    }
    return new URL(/\/$/.test(home) ? home + "index.html" : home, root).href;
  }

  /** The registry entry for the page being shown, if it's a registered projection. */
  function currentEntry() {
    var here = location.href.replace(/[?#].*$/, "").replace(/index\.html$/, "");
    return (registry.projections || []).filter(function (entry) {
      return new URL(entry.home || "", root).href.replace(/index\.html$/, "") === here;
    })[0];
  }

  // ------------------------------------------------------------ time

  var UNITS = { minute: 6e4, hour: 36e5, day: 864e5, week: 6048e5 };

  function ago(iso) {
    var ms = Date.now() - new Date(iso).getTime();
    if (isNaN(ms)) return "";
    if (ms < UNITS.minute) return "just now";
    var steps = [["week", UNITS.week], ["day", UNITS.day], ["hour", UNITS.hour], ["minute", UNITS.minute]];
    for (var i = 0; i < steps.length; i++) {
      var n = Math.floor(ms / steps[i][1]);
      if (n >= 1) return n + " " + steps[i][0] + (n === 1 ? "" : "s") + " ago";
    }
    return "";
  }

  /** "stale after 2 days" → milliseconds; anything else → null. */
  function staleAfter(freshness) {
    var match = /stale after (\d+) (minute|hour|day|week)s?/.exec(freshness || "");
    return match ? Number(match[1]) * UNITS[match[2]] : null;
  }

  function day(iso) {
    var date = new Date(iso);
    return isNaN(date.getTime()) ? "" : date.toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" });
  }

  // ------------------------------------------------------------ components

  /** How fresh a view is, from its registry entry and when it was rendered. */
  function freshness(entry, generated) {
    entry = entry || {};
    if (entry.kind === "live") return { label: "Live", state: "fresh" };
    if (entry.kind === "snapshot") return { label: "Snapshot" + (generated ? " · " + day(generated) : ""), state: "frozen" };
    if (entry.kind === "external") return { label: "External app", state: "" };
    if (!generated) return { label: "Not rendered yet", state: "stale" };
    var window_ = staleAfter(entry.freshness);
    var age = Date.now() - new Date(generated).getTime();
    if (window_ !== null && age > window_) return { label: "Updated " + ago(generated) + " · may be out of date", state: "stale" };
    return { label: "Updated " + ago(generated), state: "fresh" };
  }

  function badge(entry, generated) {
    var info = freshness(entry, generated);
    var node = el("span", "sphere-badge" + (info.state ? " sphere-badge--" + info.state : ""), info.label);
    if (generated) node.title = "Rendered " + new Date(generated).toLocaleString();
    return node;
  }

  function topbar() {
    var bar = el("header", "sphere-topbar");
    var inner = el("div", "sphere-topbar__inner");
    var home = el("a", "sphere-topbar__home", registry.name || "My sphere");
    home.href = new URL("surface/projections.html", root).href;
    inner.appendChild(home);
    var nav = el("nav", "sphere-topbar__nav");
    nav.setAttribute("aria-label", "Projections");
    var here = currentEntry();
    (registry.projections || []).forEach(function (entry) {
      var link = el("a", "", entry.title || entry.name);
      link.href = hrefFor(entry);
      if (here && here.name === entry.name) link.setAttribute("aria-current", "page");
      nav.appendChild(link);
    });
    inner.appendChild(nav);
    bar.appendChild(inner);
    return bar;
  }

  /** One panel. kind: "stats" | "list" | "text" | "markdown". */
  function panel(spec) {
    var node = el("section", "sphere-panel" + (spec.wide ? " sphere-panel--wide" : ""));
    if (spec.title) node.appendChild(el("h2", "", spec.title));
    var items = spec.items || [];
    var empty = (spec.kind === "stats" || spec.kind === "list") && items.length === 0;
    if (empty || (spec.kind !== "stats" && spec.kind !== "list" && !spec.text)) {
      node.appendChild(el("p", "sphere-panel__empty", spec.empty || "Nothing here yet."));
      return node;
    }
    if (spec.kind === "stats") {
      var stats = el("div", "sphere-stats");
      items.forEach(function (item) {
        var stat = el("div", "sphere-stat");
        stat.appendChild(el("span", "sphere-stat__value", String(item.value)));
        stat.appendChild(el("span", "sphere-stat__label", item.label));
        stats.appendChild(stat);
      });
      node.appendChild(stats);
    } else if (spec.kind === "list") {
      var list = el("ul", "sphere-list");
      items.forEach(function (item) {
        var li = el("li");
        var text = item.href ? el("a", "", item.text) : el("span", "", item.text);
        if (item.href) text.href = item.href;
        li.appendChild(text);
        if (item.meta) li.appendChild(el("span", "sphere-list__meta", item.meta));
        list.appendChild(li);
      });
      node.appendChild(list);
    } else if (spec.kind === "markdown" && window.SphereMarkdown) {
      var prose = el("div", "sphere-prose");
      prose.innerHTML = window.SphereMarkdown.render(spec.text);
      node.appendChild(prose);
    } else {
      node.appendChild(el("p", "", spec.text));
    }
    return node;
  }

  function panels(container, specs) {
    container.classList.add("sphere-panels");
    (specs || []).forEach(function (spec) {
      container.appendChild(panel(spec));
    });
  }

  /** The footer: when this was rendered, and from what. */
  function footer(generated, sources) {
    var node = el("footer", "sphere-footer");
    var line = generated ? "Rendered " + new Date(generated).toLocaleString() : "Not rendered yet";
    node.appendChild(el("div", "", line + (sources && sources.length ? ", from:" : ".")));
    if (sources && sources.length) {
      var list = el("ul");
      sources.forEach(function (source) {
        list.appendChild(el("li", "", source));
      });
      node.appendChild(list);
    }
    return node;
  }

  // ------------------------------------------------------------ wiring

  function start() {
    if (!document.body.hasAttribute("data-no-topbar")) document.body.insertBefore(topbar(), document.body.firstChild);
    if (/\/_scratch\//.test(location.pathname)) {
      var page = document.querySelector(".sphere-page");
      var note = el("div", "sphere-notice", "Preview. This isn't saved yet: the real view changes when the focus grounds.");
      if (page) page.insertBefore(note, page.firstChild);
    }
  }

  window.Sphere = {
    root: root,
    registry: registry,
    hrefFor: hrefFor,
    currentEntry: currentEntry,
    freshness: freshness,
    badge: badge,
    panel: panel,
    panels: panels,
    footer: footer,
    ago: ago,
  };

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start);
  else start();
})();
