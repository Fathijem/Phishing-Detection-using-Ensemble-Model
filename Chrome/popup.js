document.getElementById("urlInput").addEventListener("input", function () {
  let url = this.value.trim();
  let resultElement = document.getElementById("result");

  if (url.length > 5) { 
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
        resultElement.innerHTML = "⚠️ <span class='text-red-400'>Phishing Website Detected!</span>";
      } else {
        resultElement.innerHTML = "✅ <span class='text-green-400'>Safe Website</span>";
      }
    })
    .catch(error => {
      console.error("API Error:", error);
      resultElement.innerHTML = "<span class='text-yellow-400'>⚠️ Error Checking URL</span>";
    });
  } else {
    resultElement.innerHTML = "";
  }
});
