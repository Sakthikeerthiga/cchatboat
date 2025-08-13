export interface Question {
  id: string;
  name: string;
  answer: string;
}

export interface Job {
  id: string;
  name: string;
  questions: Question[];
}

export interface Client {
  id: string;
  name: string;
  questions: Question[];
}

export interface JobSummary {
  id: string;
  name: string;
}

export interface ClientSummary {
  id: string;
  name: string;
}
