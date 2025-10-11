# AfiYor Backend v2 (Postgres-ready)

## Quick start (local + production notes)

1. Copy files into backend/ (use GitHub web editor or local git).
2. Set environment variables (on Render/host):
   - DATABASE_URL (Postgres connection string)
   - GROQ_API_KEY (optional)
   - SECRET_KEY
3. Install deps:
   pip install -r requirements.txt
4. Run:
   uvicorn app.main:app --host 0.0.0.0 --port 8000
5. Test:
   GET / -> health
   POST /auth/register -> register JSON body {name,email,country,industry}
   POST /auth/login -> {email}
   POST /chat/ -> ChatRequest
   GET /history/{user_id}

Notes:
- Use Postgres in production and set DATABASE_URL accordingly.
- Add GROQ_API_KEY to host env if you want AI refinement.
