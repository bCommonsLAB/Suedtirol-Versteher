function text2Speech(elementId, lang) {
  var text = document.getElementById(elementId).innerText;

  fetch("https://api.bcommonslab.org/suedtirol/tts", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ text: text, section: "", lang: lang }),
  })
    .then((response) => response.blob())
    .then((blob) => {
      var url = window.URL.createObjectURL(blob);
      var audio = new Audio(url);
      audio.play();
    })
    .catch((error) => console.error("Error:", error));
}
