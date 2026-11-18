// A small markdown renderer for the index page's viewer and markdown panels.
// Covers what a sphere writes: frontmatter (skipped), headings, paragraphs, lists (nested by
// indentation), task boxes, quotes, fenced code, tables, rules, emphasis, code and links.
// Everything is escaped first, so a file can't inject markup. No library, no build step.
(function () {
  "use strict";

  function escape(text) {
    return text.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  function safeHref(href) {
    return /^(https?:|mailto:|#|\.{0,2}\/|[\w.-]+(\/|$|\.))/i.test(href) && !/^javascript:/i.test(href) ? href : "#";
  }

  function inline(text) {
    var codes = [];
    var out = escape(text).replace(/`([^`]+)`/g, function (_, code) {
      codes.push("<code>" + code + "</code>");
      return "\u0000" + (codes.length - 1) + "\u0000";
    });
    out = out
      .replace(/!\[([^\]]*)\]\(([^)\s]+)[^)]*\)/g, function (_, alt, href) {
        return '<a href="' + safeHref(href) + '">' + (alt || href) + "</a>";
      })
      .replace(/\[([^\]]+)\]\(([^)\s]+)[^)]*\)/g, function (_, label, href) {
        return '<a href="' + safeHref(href) + '">' + label + "</a>";
      })
      .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
      .replace(/(^|[^*\w])\*([^*\s][^*]*)\*/g, "$1<em>$2</em>")
      .replace(/(^|[^_\w])_([^_\s][^_]*)_(?!\w)/g, "$1<em>$2</em>");
    return out.replace(/\u0000(\d+)\u0000/g, function (_, i) {
      return codes[Number(i)];
    });
  }

  function cells(row) {
    return row
      .trim()
      .replace(/^\||\|$/g, "")
      .split("|")
      .map(function (cell) {
        return cell.trim();
      });
  }

  function list(lines, start) {
    // Gather a list block: items and their deeper-indented continuation lines.
    var match = /^(\s*)([-*+]|\d+[.)])\s+/.exec(lines[start]);
    var indent = match[1].length;
    var ordered = /\d/.test(match[2]);
    var html = ordered ? "<ol>" : "<ul>";
    var i = start;
    while (i < lines.length) {
      var item = /^(\s*)([-*+]|\d+[.)])\s+(.*)$/.exec(lines[i]);
      if (!item || item[1].length !== indent) break;
      var text = item[3];
      var box = /^\[( |x|X)\]\s+/.exec(text);
      if (box) text = (box[1] === " " ? "☐ " : "☑ ") + text.slice(box[0].length);
      var body = inline(text);
      i++;
      var nested = [];
      while (i < lines.length && lines[i].trim() !== "" && /^(\s*)/.exec(lines[i])[1].length > indent) {
        nested.push(lines[i]);
        i++;
      }
      if (nested.length) {
        var sub = /^\s*([-*+]|\d+[.)])\s+/.test(nested[0]) ? blocks(nested) : "<p>" + inline(nested.join(" ").trim()) + "</p>";
        body += sub;
      }
      html += "<li>" + body + "</li>";
    }
    return { html: html + (ordered ? "</ol>" : "</ul>"), next: i };
  }

  function blocks(lines) {
    var html = "";
    var i = 0;
    while (i < lines.length) {
      var line = lines[i];
      var fence = /^\s*(```|~~~)/.exec(line);
      if (fence) {
        var code = [];
        i++;
        while (i < lines.length && lines[i].trim().indexOf(fence[1]) !== 0) code.push(lines[i++]);
        i++;
        html += "<pre><code>" + escape(code.join("\n")) + "</code></pre>";
      } else if (!line.trim()) {
        i++;
      } else if (/^#{1,6}\s/.test(line)) {
        var level = /^#+/.exec(line)[0].length;
        html += "<h" + level + ">" + inline(line.replace(/^#+\s+/, "").replace(/\s+#+\s*$/, "")) + "</h" + level + ">";
        i++;
      } else if (/^\s*([-*_])(\s*\1){2,}\s*$/.test(line)) {
        html += "<hr>";
        i++;
      } else if (/^\s*>/.test(line)) {
        var quote = [];
        while (i < lines.length && /^\s*>/.test(lines[i])) quote.push(lines[i++].replace(/^\s*>\s?/, ""));
        html += "<blockquote>" + blocks(quote) + "</blockquote>";
      } else if (/^\s*\|/.test(line) && i + 1 < lines.length && /^\s*\|?\s*:?-{3,}/.test(lines[i + 1])) {
        var head = cells(line);
        i += 2;
        var rows = [];
        while (i < lines.length && /^\s*\|/.test(lines[i])) rows.push(cells(lines[i++]));
        html +=
          "<table><thead><tr>" +
          head.map(function (cell) {
            return "<th>" + inline(cell) + "</th>";
          }).join("") +
          "</tr></thead><tbody>" +
          rows.map(function (row) {
            return "<tr>" + row.map(function (cell) {
              return "<td>" + inline(cell) + "</td>";
            }).join("") + "</tr>";
          }).join("") +
          "</tbody></table>";
      } else if (/^\s*([-*+]|\d+[.)])\s+/.test(line)) {
        var result = list(lines, i);
        html += result.html;
        i = result.next;
      } else {
        var para = [];
        while (
          i < lines.length &&
          lines[i].trim() &&
          !/^(#{1,6}\s|\s*```|\s*~~~|\s*>|\s*\||\s*([-*+]|\d+[.)])\s+)/.test(lines[i])
        ) {
          para.push(lines[i++].trim());
        }
        if (!para.length) para.push(lines[i++].trim());
        html += "<p>" + inline(para.join(" ")) + "</p>";
      }
    }
    return html;
  }

  /** Markdown text → HTML. Frontmatter at the top is left out. */
  function render(text) {
    var lines = String(text || "").replace(/\r\n?/g, "\n").split("\n");
    if (lines[0] === "---") {
      var end = lines.indexOf("---", 1);
      if (end > 0) lines = lines.slice(end + 1);
    }
    return blocks(lines);
  }

  window.SphereMarkdown = { render: render };
})();
