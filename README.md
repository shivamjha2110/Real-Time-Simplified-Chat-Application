# Real-Time Simplified Chat Application

A real-time chat application where multiple users can instantly send and receive messages within a single chat room using WebSocket communication.

## Live Deployments

- **Frontend (Vercel)**: [https://chat-app-front-mdovn81pc-shivam-jhas-projects-70346416.vercel.app/](https://chat-app-front-mdovn81pc-shivam-jhas-projects-70346416.vercel.app/)
- **Backend (Render)**: [https://chat-app-backen-x8ic.onrender.com](https://chat-app-backen-x8ic.onrender.com)

## Application Functionality

This application provides:
- Real-time messaging through WebSocket connections
- Connection status indicator (Connected/Disconnected)
- Messages displayed in chronological order
- Responsive design for various screen sizes
- Error handling with user-friendly messages

## Running the Application Locally

### Frontend Setup

```bash
# Navigate to the frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

The frontend will be available at http://localhost:3000

### Backend Setup

```bash
# Navigate to the backend directory
cd backend

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the backend server
uvicorn app.main:app --reload
```

The backend will be available at http://localhost:8000

## Environment Variables

### Frontend (.env.example)

```
NEXT_PUBLIC_WEBSOCKET_URL=ws://localhost:8000/ws
```

### Backend (.env.example)

```
HOST=0.0.0.0
PORT=8000
```

## Running Tests

### Frontend Tests

```bash
cd frontend
npm test
```

### Backend Tests

```bash
cd backend
pytest
```

## Deployment Instructions

### Frontend (Vercel)

1. Connect your GitHub repository to Vercel
2. Configure the build settings:
   - Framework Preset: Next.js
   - Build Command: `npm run build`
   - Output Directory: `.next`
3. Add environment variables:
   - `NEXT_PUBLIC_WEBSOCKET_URL=wss://chat-app-backen-x8ic.onrender.com/ws`

### Backend (Render)

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Configure the build settings:
   - Runtime: Python 3.9
   - Build Command: `pip install -r backend/requirements.txt`
   - Start Command: `cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT`

## Testing with Postman

For testing the WebSocket connection:

1. Open Postman
2. Create a new WebSocket request
3. Enter the WebSocket URL: `wss://chat-app-backen-x8ic.onrender.com/ws`
4. Click "Connect"
5. Send messages in the following JSON format:

```json
{
  "sender": "Admin",
  "content": "Hello, world!",
  "timestamp": "2025-02-27T12:00:00Z"
}
```
