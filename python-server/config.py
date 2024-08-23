config = {
    "myopenkey": "YOUR_API_KEY",
    "port": 5000,
    "modelname": "gpt-4o",
     "jsonbuild": """
          Analysiere den folgenden Text auf Deutsch und gib die Ergebnisse in einem strukturierten Json Format zurück ohne einen markdown viewer. Das Ergebnis sollte die folgenden Komponenten enthalten:

        - "Transcript_D": Die Transkription auf Deutsch bzw. falls text=italienisch deutsche Übersetzung.
        - "Transcript_I": Die Transkription auf Italienisch bzw. falls text=deutsch Übersetzung auf Italienisch.
        - "Eindruck_D": Der Eindruck, den der Text auf Deutsch hinterlässt.
        - "Eindruck_I": L'impressione lasciata dal testo in italiano.
        - "Höflichkeit": Eine Zahl zwischen 0% und 100%, wobei 100% sehr höflich und 0% sehr frech ist.
        - "Sympathisch": Eine Zahl zwischen 0% und 100%, wobei 100% sehr sympathisch und 0% sehr unsympathisch ist.
        - "Lobend": Eine Zahl zwischen 0% und 100%, wobei 100% überhaupt nicht beleidigend und 0% sehr beleidigend ist.
        - "Wortwahl": Eine Zahl zwischen 0% und 100%, wobei 100% eine sehr gute Wortwahl hat und 0% eine sehr schlechte Wortwahl hat.

            Hier ist der transkribierte Text:
          """
}
