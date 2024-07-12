const text1 = document.getElementById('text1');
const text2 = document.getElementById('text2');

const fullText1 = "Ich bin dein Südtirol Versteher und du kannst mir etwas diktieren. Ich versuche es auf Deutsch und Italienisch zu transkribieren. Deine Daten werden nicht gepeichert, müssen aber an openAI zur Verarbeitung gesendet werden. Formuliere deinen Text höflich und sympathisch - ob es geklappt hat, sieht du unten in der Bewertung. Viel Spass!";
const fullText2 = "Sono il tuo Capitore Suedtirolesini e puoi dettarmi qualcosa. Cercherò di trascriverlo in tedesco e in italiano. I tuoi dati non verranno memorizzati, ma devono essere inviati a OpenAI per l'elaborazione. Formula il tuo testo in modo educato e simpatico - vedrai se ha funzionato nella valutazione sottostante. Divertiti!";

const initialText1 = fullText1.split(' ').slice(0, 5).join(' ') + '...';
const initialText2 = fullText2.split(' ').slice(0, 5).join(' ') + '...';

text1.innerText = initialText1;
text2.innerText = initialText2;

text1.addEventListener('mouseover', () => {
    text1.innerText = fullText1;
});

text1.addEventListener('mouseout', () => {
    text1.innerText = initialText1;
});

text2.addEventListener('mouseover', () => {
    text2.innerText = fullText2;
});

text2.addEventListener('mouseout', () => {
    text2.innerText = initialText2;
});