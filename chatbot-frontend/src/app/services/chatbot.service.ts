import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { JobSummary, ClientSummary, Question } from '../models/chatbot';

@Injectable({
  providedIn: 'root'
})
export class ChatbotService {
  private apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) { }

  getJobs(): Observable<JobSummary[]> {
    return this.http.get<JobSummary[]>(`${this.apiUrl}/jobs`);
  }

  getClients(): Observable<ClientSummary[]> {
    return this.http.get<ClientSummary[]>(`${this.apiUrl}/clients`);
  }

  getJobQuestions(jobId: string): Observable<Question[]> {
    return this.http.get<Question[]>(`${this.apiUrl}/jobs/${jobId}/questions`);
  }

  getClientQuestions(clientId: string): Observable<Question[]> {
    return this.http.get<Question[]>(`${this.apiUrl}/clients/${clientId}/questions`);
  }
}
