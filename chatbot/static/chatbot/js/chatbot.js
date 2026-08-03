document.addEventListener("DOMContentLoaded", () => {
  const launcher = document.getElementById("chat-launcher");
  const win = document.getElementById("chat-window");
  const closeBtn = document.getElementById("chat-close");
  const body = document.getElementById("chat-body");
  const form = document.getElementById("chat-form");
  const input = document.getElementById("chat-input");
  const quickWrap = document.getElementById("chat-quick-replies");

  if (!launcher || !win) return;

  const csrfInput = document.querySelector('input[name="csrfmiddlewaretoken"]');
  const csrfToken = csrfInput ? csrfInput.value : "";

  const CHAT_ENDPOINT = "/api/chat/";
  let greeted = false;

  function toggleChat(forceOpen) {
    const willOpen = forceOpen !== undefined ? forceOpen : !win.classList.contains("open");
    win.classList.toggle("open", willOpen);
    launcher.setAttribute("aria-expanded", willOpen ? "true" : "false");
    if (willOpen && !greeted) {
      greeted = true;
      sendMessage("", true);
    }
    if (willOpen) input.focus();
  }

  launcher.addEventListener("click", () => toggleChat());
  closeBtn.addEventListener("click", () => toggleChat(false));

  function addMessage(text, who) {
    const el = document.createElement("div");
    el.className = `chat-msg ${who}`;
    el.textContent = text;
    body.appendChild(el);
    body.scrollTop = body.scrollHeight;
  }

  function showTyping() {
    const el = document.createElement("div");
    el.className = "chat-typing";
    el.id = "chat-typing-indicator";
    el.innerHTML = "<span></span><span></span><span></span>";
    body.appendChild(el);
    body.scrollTop = body.scrollHeight;
  }

  function hideTyping() {
    const el = document.getElementById("chat-typing-indicator");
    if (el) el.remove();
  }

  function renderQuickReplies(options) {
    quickWrap.innerHTML = "";
    (options || []).forEach((label) => {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.textContent = label;
      btn.addEventListener("click", () => sendMessage(label));
      quickWrap.appendChild(btn);
    });
  }

  async function sendMessage(text, isInitial) {
    if (!isInitial) {
      addMessage(text, "user");
    }
    showTyping();
    quickWrap.innerHTML = "";

    try {
      const res = await fetch(CHAT_ENDPOINT, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify({ message: isInitial ? "" : text }),
      });
      const data = await res.json();
      hideTyping();
      addMessage(data.reply, "bot");
      renderQuickReplies(data.quick_replies);
    } catch (err) {
      hideTyping();
      addMessage(
        "Sorry, I couldn't reach the server just now. Please try again or email info@accutech.ae.",
        "bot"
      );
    }
  }

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const text = input.value.trim();
    if (!text) return;
    input.value = "";
    sendMessage(text);
  });
});
