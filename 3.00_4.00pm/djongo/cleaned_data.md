⚡ Why two checks (form + model)?
      Form side (clean_email) → user ku friendly error msg show pannum before save.
      Model side (unique=True) → DB ku final strict rule. Even hacker bypass pannina DB block pannidum.

👉 Simple ah solna:
     Form validation → “boss, neenga already apply pannirukeenga, duplicate panna mudiyadhu” nu polite ah sollum.
     Model unique constraint → “entha situation la irundalum duplicate panna allow panna maaten” nu strict ah irukum.