{
const fullText1 =
  "DISCLAIMER: Deine Daten werden nicht gespeichert, müssen aber an openAI zur Verarbeitung gesendet werden. Formuliere deinen Text höflich und sympathisch - ob es geklappt hat, siehst du unten in der Bewertung. Viel Spass!";
const initialText1 =
  "DISCLAIMER!";

// Referenz zum richtigen Element
const textElement1 = document.getElementById("text1");

// Set the initial height to ensure smooth first transition
textElement1.style.height = "17px";
textElement1.innerText = initialText1;

let timeoutId;

textElement1.addEventListener("mouseover", () => {
  clearTimeout(timeoutId);
  textElement1.innerText = fullText1;

  // Get the full height of the content
  const fullHeight = textElement1.scrollHeight + "px";

  // Set the height to the current height first (for smooth animation)
  textElement1.style.height = textElement1.offsetHeight + "px";

  // Trigger a reflow to apply the current height before changing it
  textElement1.offsetHeight; // This forces a reflow, necessary for the transition

  // Now, set the height to the full height, which will trigger the transition
  textElement1.style.height = fullHeight;
});

textElement1.addEventListener("mouseout", () => {
  // Set the height back to the initial height
  textElement1.style.height = "17px";

  timeoutId = setTimeout(() => {
    textElement1.innerText = initialText1;
  }, 725);
});
}
{
const fullText2 =
  "DISCLAIMER: I tuoi dati non vengono salvati, ma vengono mandatia ad OPENAI per essere elaborati. Formula un testo cortese e sympatico - Vedrai se ha funzionato nella valutazione in fondo alla pagina. Buon divertimento!";
const initialText2 =
  "DISCLAIMER!";

// Referenz zum richtigen Element
const textElement2 = document.getElementById("text2");

// Set the initial height to ensure smooth first transition
textElement2.style.height = "17px";
textElement2.innerText = initialText2;

textElement2.addEventListener("mouseover", () => {
  clearTimeout(timeoutId);
  textElement2.innerText = fullText2;

  // Get the full height of the content
  const fullHeight = textElement2.scrollHeight + "px";

  // Set the height to the current height first (for smooth animation)
  textElement2.style.height = textElement2.offsetHeight + "px";

  // Trigger a reflow to apply the current height before changing it
  textElement2.offsetHeight; // This forces a reflow, necessary for the transition

  // Now, set the height to the full height, which will trigger the transition
  textElement2.style.height = fullHeight;
});

textElement2.addEventListener("mouseout", () => {
  // Set the height back to the initial height
  textElement2.style.height = "17px";

  timeoutId = setTimeout(() => {
    textElement2.innerText = initialText2;
  }, 725);
});
}