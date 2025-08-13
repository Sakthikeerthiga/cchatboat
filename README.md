# ChatBoat - Full-Stack Chatbot System

A modern chatbot system built with Python FastAPI backend and Angular 16+ frontend, featuring interactive job and client management with dynamic question generation.

## 🚀 Features

- **Interactive Chatbot Interface**: Modern, responsive design with smooth animations
- **Job Management**: Browse available jobs and view related questions
- **Client Management**: Access client information and specific inquiries
- **Smart Navigation**: Intuitive back/forward navigation with state management
- **Minimize/Restore**: Collapsible chatbot interface that maintains session state
- **Reset Functionality**: Quick return to main menu from any point
- **Real-time API Integration**: Dynamic data fetching from backend services

## 🏗️ Architecture

### Backend (Python FastAPI)
- **Framework**: FastAPI with automatic API documentation
- **Data Models**: Pydantic models for type safety
- **CORS Support**: Configured for Angular frontend
- **Static Data**: Sample jobs, clients, and questions for demonstration

### Frontend (Angular 16+)
- **Framework**: Angular 16+ with standalone components
- **Styling**: Bootstrap 5 + custom CSS with animations
- **Icons**: Font Awesome for rich iconography
- **State Management**: Component-based state handling
- **Responsive Design**: Mobile-friendly interface

## 📁 Project Structure

```
chat-boat/
├── chatbot-backend/          # Python FastAPI backend
│   ├── main.py              # Main application file
│   ├── requirements.txt     # Python dependencies
│   └── README.md           # Backend setup guide
├── chatbot-frontend/        # Angular frontend
│   ├── src/
│   │   ├── app/
│   │   │   ├── chatbot/    # Main chatbot component
│   │   │   ├── services/   # API service layer
│   │   │   └── models/     # TypeScript interfaces
│   │   └── ...
│   ├── angular.json        # Angular configuration
│   └── package.json        # Node.js dependencies
└── README.md               # This file
```

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 18+
- Angular CLI 16+

### Quick Start (Windows)
For Windows users, we've provided convenient startup scripts:

1. **Start Both Services**: Double-click `start-chatboat.bat` or run `start-chatboat.ps1` in PowerShell
2. **Start Backend Only**: Double-click `start-backend.bat` or run `start-backend.ps1` in PowerShell  
3. **Start Frontend Only**: Double-click `start-frontend.bat`

### Manual Setup

#### Backend Setup

1. Navigate to the backend directory:
```bash
cd chatbot-backend
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Run the FastAPI server:
```bash
python main.py
```

The backend will be available at `http://localhost:8000`

#### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd chatbot-frontend
```

2. Install Node.js dependencies:
```bash
npm install
```

3. Start the development server:
```bash
ng serve
```

The frontend will be available at `http://localhost:4200`

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/jobs` | Get all available jobs |
| GET | `/clients` | Get all available clients |
| GET | `/jobs/{id}/questions` | Get questions for a specific job |
| GET | `/clients/{id}/questions` | Get questions for a specific client |

## 🎯 Usage

1. **Start the Application**: Ensure both backend and frontend are running
2. **Access the Chatbot**: Click on the chatbot icon in the bottom right corner
3. **Navigate Options**: Choose between Jobs or Clients
4. **Explore Content**: Click on specific items to view related questions
5. **Use Navigation**: Use "Go Back" to return to previous menus
6. **Reset**: Use "Reset" to return to the main greeting
7. **Minimize**: Use "Minimize" to collapse the chatbot

## 🎨 Customization

### Adding New Jobs/Clients
Edit the `data` dictionary in `chatbot-backend/main.py` to add new entries.

### Styling Changes
Modify `chatbot-frontend/src/app/chatbot/chatbot.component.css` for custom styling.

### API Modifications
Extend the FastAPI endpoints in `chatbot-backend/main.py` for additional functionality.

## 🔧 Development

### Backend Development
- FastAPI provides automatic API documentation at `/docs`
- Hot reload enabled for development
- Type hints and validation with Pydantic

### Frontend Development
- Angular CLI for component generation
- Standalone components for modern Angular architecture
- CSS animations and responsive design

## 🚀 Deployment

### Backend Deployment
- Use uvicorn with production settings
- Consider using Gunicorn for production
- Environment variables for configuration

### Frontend Deployment
- Build with `ng build --configuration production`
- Deploy to static hosting (Netlify, Vercel, etc.)
- Update API URL for production backend

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 🆘 Support

For issues and questions:
- Check the API documentation at `/docs` when backend is running
- Review the console for any error messages
- Ensure both services are running on correct ports

---

**Happy Chatting! 🚀**
