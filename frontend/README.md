# Frontend App

Local React frontend for Ethiopian Bible Guardian.

## Requirements

- Node.js 20+
- Backend API running at http://127.0.0.1:8000

## Setup

1. Install dependencies:

```powershell
npm install
```

2. Copy environment file:

```powershell
Copy-Item .env.example .env
```

3. Start development server:

```powershell
npm run dev
```

Frontend runs on the URL shown by Vite (usually http://127.0.0.1:5173).

## Build

```powershell
npm run build
```

## API Contract

- POST /chat with JSON body:
	- query: string
	- top_k: number
- The UI renders:
	- Invocation
	- Witness
	- Exhortation
	- Reflection
	- Citation list
