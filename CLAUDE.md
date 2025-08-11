# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Start Development Server
```bash
# Quick start (recommended)
./run.sh

# Manual start
cd backend && uv run uvicorn app:app --reload --port 8000
```

### Dependencies
```bash
# Install all dependencies
uv sync

# Add new dependency
uv add package_name
```

### Environment Setup
Create `.env` file in root directory with:
```
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

## Architecture Overview

This is a RAG (Retrieval-Augmented Generation) system with clear separation between backend services and frontend interface.

### Core Components

**RAGSystem (`backend/rag_system.py`)**: Main orchestrator that coordinates all components. Handles document ingestion, query processing, and response generation.

**VectorStore (`backend/vector_store.py`)**: ChromaDB-based vector storage with two collections:
- `course_catalog`: Course metadata with lesson links for semantic course matching
- `course_content`: Actual text chunks for retrieval

**DocumentProcessor (`backend/document_processor.py`)**: Processes course documents with structured format:
- Line 1: `Course Title: [title]`
- Line 2: `Course Link: [url]`  
- Line 3: `Course Instructor: [instructor]`
- Following lines: `Lesson X: [title]` with optional `Lesson Link: [url]`

**Search Tools (`backend/search_tools.py`)**: Tool-based architecture for AI function calls:
- `CourseSearchTool`: Handles semantic search with course/lesson filtering
- `ToolManager`: Registers and executes tools for Claude function calling
- Sources include clickable lesson links when available

**AI Generator (`backend/ai_generator.py`)**: Anthropic Claude integration with function calling capability.

**Session Manager (`backend/session_manager.py`)**: Manages conversation history with configurable message retention.

### Data Flow

1. **Document Processing**: Course files in `/docs` → DocumentProcessor → Course + CourseChunk objects
2. **Storage**: Course metadata → course_catalog collection, Content chunks → course_content collection  
3. **Query Processing**: User query → VectorStore search → Retrieved chunks + metadata (including lesson links) → Claude with function calling → Response
4. **Frontend**: Sources rendered as clickable links when lesson_link available

### Configuration

All settings centralized in `backend/config.py`:
- Chunk size/overlap for document processing
- Vector search parameters
- Claude model selection
- Database paths

### Frontend Architecture

**Single-page application** (`frontend/`):
- `index.html`: Main interface with sidebar for course stats and suggestions
- `script.js`: Handles API communication, markdown rendering, and clickable source links
- `style.css`: Dark theme with responsive design

**Source Link Implementation**: 
- Backend returns sources as objects with `display` text and optional `link` 
- Frontend renders links with `target="_blank"` and proper styling
- Links open lesson videos in new tabs invisibly (no visible URL text)

### Key Integrations

- **ChromaDB**: Persistent vector storage with sentence-transformer embeddings
- **Anthropic Claude**: Function calling for tool-based search with lesson link retrieval
- **FastAPI**: REST API with static file serving for frontend
- **Sentence Transformers**: `all-MiniLM-L6-v2` for embeddings

### Important Implementation Details

- Course titles serve as unique IDs in ChromaDB
- Lesson links stored as JSON in course metadata and retrieved via `get_lesson_link()`
- Tool-based search enables semantic course name matching (e.g., "MCP" finds "MCP: Build Rich-Context AI Apps")
- Session-based conversation history with configurable retention
- Uvicorn with auto-reload for development

### Application URLs

- Web Interface: `http://localhost:8000`
- API Documentation: `http://localhost:8000/docs`
- API Endpoints: `/api/query` (POST), `/api/courses` (GET)