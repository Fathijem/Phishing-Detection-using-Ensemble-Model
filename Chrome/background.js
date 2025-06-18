chrome.webNavigation.onBeforeNavigate.addListener((details) => {
  const url = details.url;

  fetch("http://localhost:5000/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ url: url })
  })
    .then(response => response.json())
    .then(data => {
      if (data.prediction === "phishing") {
        alert("Phishing Website Detected!\nAccess Blocked");
        chrome.tabs.update(details.tabId, { url: "about:blank" }); // Block the website
      }
    })
    .catch(error => {
      console.error("API Error:", error);
    });
}, { urls: ["<all_urls>"] });
