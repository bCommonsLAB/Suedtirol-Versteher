document.addEventListener("DOMContentLoaded", () => {
  const statusElement = document.getElementById("status");
  const sendBtn = document.getElementById("sendbutton");
  const centerSprachanalyse = document.getElementById("center");
  const sprachanalyse = document.getElementById("sprachanalyse");
  const loadingScreen = document.getElementById("loading-screen");
  const germanTranscriptionElement = document.getElementById("german-transcription");
  const germanSummaryElement = document.getElementById("german-summary");
  const italianTranscriptionElement = document.getElementById("italian-transcription");
  const italianSummaryElement = document.getElementById("italian-summary");

  centerSprachanalyse.style.display = "none";
  sprachanalyse.style.display = "none";

  function showCenter() {
    centerSprachanalyse.style.display = "flex";
    sprachanalyse.style.display = "flex";

    animateExpansion(centerSprachanalyse);
    animateExpansion(sprachanalyse);
  }

  function animateExpansion(element) {
    element.animate(
      [
        { transform: "scaleY(0)", height: "0px" },
        { transform: "scaleY(1)", height: element.scrollHeight + "px" },
      ],
      {
        duration: 500,
        easing: "ease-out",
        fill: "forwards",
      }
    );
  }

  function showLoading() {
    loadingScreen.style.display = "flex";
  }

  function hideLoading() {
    loadingScreen.style.display = "none";
  }

  function resetAll() {
    if (statusElement) statusElement.innerText = "Bereit zur Analyse";
    if (germanTranscriptionElement) germanTranscriptionElement.innerText = "";
    if (germanSummaryElement) germanSummaryElement.innerText = "";
    if (italianTranscriptionElement) italianTranscriptionElement.innerText = "";
    if (italianSummaryElement) italianSummaryElement.innerText = "";

    updateCircle("circle-höflichkeit", "höflichkeit-prozent", 0);
    updateCircle("circle-sympathisch", "sympathisch-prozent", 0);
    updateCircle("circle-lobend", "lobend-prozent", 0);
    updateCircle("circle-wortwahl", "wortwahl-prozent", 0);
  }

  sendBtn.addEventListener("click", () => {
    resetAll();
    const userTextElement = document.getElementById("user-text");
    if (!userTextElement) {
      if (statusElement) statusElement.innerText = "Fehler: Text-Eingabefeld nicht gefunden";
      return;
    }

    showLoading();
    const formData = new FormData();
    formData.append("text", userTextElement.value);

    fetch("https://api.bcommonslab.org/suedtirol/analyze-text", {
      method: "POST",
      body: formData,
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok " + response.statusText);
        }
        return response.json();
      })
      .then((data) => {
        hideLoading();
        if (data.error) {
          if (statusElement) statusElement.innerText = "Fehler bei der Analyse: " + data.error;
          console.error("Analyse Fehler:", data.error);
        } else {
          if (germanTranscriptionElement) germanTranscriptionElement.innerText = data.Transcript_D || "";
          if (germanSummaryElement) germanSummaryElement.innerText = data.Eindruck_D || "";
          if (italianTranscriptionElement) italianTranscriptionElement.innerText = data.Transcript_I || "";
          if (italianSummaryElement) italianSummaryElement.innerText = data.Eindruck_I || "";

          updateCircle("circle-höflichkeit", "höflichkeit-prozent", data.Höflichkeit);
          updateCircle("circle-sympathisch", "sympathisch-prozent", data.Sympathisch);
          updateCircle("circle-lobend", "lobend-prozent", data.Lobend);
          updateCircle("circle-wortwahl", "wortwahl-prozent", data.Wortwahl);

          if (statusElement) statusElement.innerText = "Analyse beendet";
        }
        showCenter();
      })
      .catch((error) => {
        hideLoading();
        if (statusElement) statusElement.innerText = "Fehler bei der Analyse";
        console.error(error);
      });
  });

  function updateCircle(circleId, percentId, value) {
    const circle = document.getElementById(circleId);
    const percent = document.getElementById(percentId);
    if (circle) circle.style.setProperty("--p", value);
    if (percent) percent.innerText = value + "%";
  }
});
