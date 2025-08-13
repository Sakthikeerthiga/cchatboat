import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ChatbotService } from '../services/chatbot.service';
import { JobSummary, ClientSummary, Question } from '../models/chatbot';

enum ChatbotState {
  GREETING = 'greeting',
  JOBS = 'jobs',
  CLIENTS = 'clients',
  QUESTIONS = 'questions',
  ANSWER = 'answer'
}

@Component({
  selector: 'app-chatbot',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './chatbot.component.html',
  styleUrl: './chatbot.component.css'
})
export class ChatbotComponent implements OnInit {
  isMinimized = false;
  currentState = ChatbotState.GREETING;
  previousState = ChatbotState.GREETING;
  
  jobs: JobSummary[] = [];
  clients: ClientSummary[] = [];
  questions: Question[] = [];
  currentSelection: { type: 'job' | 'client', id: string, name: string } | null = null;
  selectedQuestion: Question | null = null;
  
  greeting = "Hey, good morning! What can I help you with?";

  constructor(private chatbotService: ChatbotService) {}

  ngOnInit(): void {
    this.loadData();
  }

  loadData(): void {
    this.chatbotService.getJobs().subscribe(jobs => {
      this.jobs = jobs;
    });

    this.chatbotService.getClients().subscribe(clients => {
      this.clients = clients;
    });
  }

  toggleMinimize(): void {
    this.isMinimized = !this.isMinimized;
  }

  reset(): void {
    this.currentState = ChatbotState.GREETING;
    this.previousState = ChatbotState.GREETING;
    this.currentSelection = null;
    this.questions = [];
    this.selectedQuestion = null;
  }

  goBack(): void {
    console.log('goBack called. Current state:', this.currentState, 'Previous state:', this.previousState);
    
    if (this.currentState === ChatbotState.ANSWER) {
      this.currentState = ChatbotState.QUESTIONS;
      this.selectedQuestion = null;
      console.log('Going back to QUESTIONS state');
    } else if (this.currentState === ChatbotState.QUESTIONS) {
      // Always go back to greeting from questions
      this.currentState = ChatbotState.GREETING;
      this.previousState = ChatbotState.GREETING;
      this.currentSelection = null;
      this.questions = [];
      console.log('Going back to GREETING state');
    } else {
      this.currentState = ChatbotState.GREETING;
      console.log('Going back to GREETING state (default)');
    }
    
    console.log('New state:', this.currentState);
  }

  showJobs(): void {
    console.log('showJobs called. Current state:', this.currentState);
    this.currentState = ChatbotState.JOBS;
    this.previousState = ChatbotState.GREETING;
    console.log('New state:', this.currentState, 'Previous state:', this.previousState);
  }

  showClients(): void {
    console.log('showClients called. Current state:', this.currentState);
    this.currentState = ChatbotState.CLIENTS;
    this.previousState = ChatbotState.GREETING;
    console.log('New state:', this.currentState, 'Previous state:', this.previousState);
  }

  selectJob(job: JobSummary): void {
    console.log('selectJob called for:', job.name);
    this.currentSelection = { type: 'job', id: job.id, name: job.name };
    this.previousState = ChatbotState.JOBS;
    this.currentState = ChatbotState.QUESTIONS;
    console.log('New state:', this.currentState, 'Previous state:', this.previousState);
    
    this.chatbotService.getJobQuestions(job.id).subscribe(questions => {
      this.questions = questions;
    });
  }

  selectClient(client: ClientSummary): void {
    console.log('selectClient called for:', client.name);
    this.currentSelection = { type: 'client', id: client.id, name: client.name };
    this.previousState = ChatbotState.CLIENTS;
    this.currentState = ChatbotState.QUESTIONS;
    console.log('New state:', this.currentState, 'Previous state:', this.previousState);
    
    this.chatbotService.getClientQuestions(client.id).subscribe(questions => {
      this.questions = questions;
    });
  }

  selectQuestion(question: Question): void {
    this.selectedQuestion = question;
    this.previousState = ChatbotState.QUESTIONS;
    this.currentState = ChatbotState.ANSWER;
  }

  getStateClass(): string {
    if (this.isMinimized) return 'minimized';
    return this.currentState;
  }
}
