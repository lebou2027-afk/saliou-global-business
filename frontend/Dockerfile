version: '3.9'

services:
  backend:
    build: ./backend
    container_name: saliou-backend
    ports:
      - "8000:8000"
    env_file:
      - ./backend/.env
    volumes:
      - ./backend:/app

  frontend:
    build: ./frontend
    container_name: saliou-frontend
    ports:
      - "5173:5173"
    env_file:
      - ./frontend/.env
    depends_on:
      - backend
    volumes:
      - ./frontend:/app
