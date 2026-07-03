/* =========================================================================
   MM Teamspeak — Verbindung zu Supabase (für GETEILTE Kommentare & Likes)

   Solange beide Felder leer sind, läuft die Seite im LOKALEN Modus:
   Kommentare/Likes bleiben nur auf dem jeweiligen Gerät.

   Sobald du beide Werte aus deinem Supabase-Projekt einträgst
   (Supabase → Project Settings → API), sehen ALLE Besucher die
   Kommentare & Likes dauerhaft und in Echtzeit.

   Schritt-für-Schritt + fertige SQL: siehe SUPABASE_SETUP.md
   ========================================================================= */
window.MM_CONFIG = {
  SUPABASE_URL: "https://nihwsujlmspthvdqlmhg.supabase.co",       // z.B. "https://abcdefgh.supabase.co"
  SUPABASE_ANON_KEY: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5paHdzdWpsbXNwdGh2ZHFsbWhnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODIyNDg2MTQsImV4cCI6MjA5NzgyNDYxNH0.ORkDYn8vF1widtkeGepcxnhD1SwpooFgUBil3li8F8Y"   // der "anon public" Key (langer Token)
};
