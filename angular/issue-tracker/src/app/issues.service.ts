import { Issue } from './issue';
import { Injectable } from '@angular/core';
import { issues as issuesList } from '../assets/mock-issues';

@Injectable({
  providedIn: 'root',
})
export class IssuesService {
  private issues: Issue[] = issuesList;

  constructor() {}

  getPendingIssues(): Issue[] {
    return this.issues.filter((issue) => !issue.completed);
  }

  createIssue(issue: Issue) {
    issue.issueNo = this.issues.length + 1;
    this.issues.push(issue);
  }

  completeIssue(issue: Issue) {
    const selectdIssue: Issue = {
      ...issue,
      completed: new Date(),
    };
    const index = this.issues.findIndex((i) => i === issue);
    this.issues[index] = selectdIssue;
  }

  getSuggestions(title: string): Issue[] {
    if (title.length > 3) {
      return this.issues.filter((issue) => issue.title.indexOf(title) !== -1);
    }
    return [];
  }
}
