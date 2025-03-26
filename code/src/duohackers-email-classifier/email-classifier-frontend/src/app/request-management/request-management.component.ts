import { Component } from '@angular/core';

@Component({
  selector: 'app-request-management',
  templateUrl: './request-management.component.html',
  styleUrls: ['./request-management.component.css']
})
export class RequestManagementComponent {
  requestTypes: { name: string, subRequests: string[] }[] = [
    { name: 'Loan Request', subRequests: ['New Loan', 'Loan Extension', 'Loan Modification'] },
    { name: 'Document Submission', subRequests: ['KYC Documents', 'Financial Statements'] },
  ];
  newRequestType: string = '';
  newSubRequest: { [key: string]: string } = {};

  addRequestType() {
    if (this.newRequestType.trim()) {
      this.requestTypes.push({ name: this.newRequestType, subRequests: [] });
      this.newRequestType = '';
    }
  }

  addSubRequest(requestName: string) {
    const subRequest = this.newSubRequest[requestName]?.trim();
    if (subRequest) {
      const request = this.requestTypes.find(req => req.name === requestName);
      if (request) {
        request.subRequests.push(subRequest);
        this.newSubRequest[requestName] = '';
      }
    }
  }

  deleteRequestType(requestName: string) {
    this.requestTypes = this.requestTypes.filter(req => req.name !== requestName);
  }
}
