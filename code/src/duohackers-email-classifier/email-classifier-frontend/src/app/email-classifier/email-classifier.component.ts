import { Component } from '@angular/core';
import { HttpClient, HttpEvent, HttpEventType,HttpResponse } from '@angular/common/http';
@Component({
  selector: 'app-email-classifier',
  templateUrl: './email-classifier.component.html',
  styleUrls: ['./email-classifier.component.css']
})
export class EmailClassifierComponent {
 selectedFile: File | null = null;
  classificationResult: any = null;
  error: string | null = null;
  duplicateError: string | null = null;
  progress: number = -1;

  constructor(private http: HttpClient) {}

  onFileSelected(event: Event) {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      this.selectedFile = input.files[0];
    }
  }

  uploadFile() {
    if (!this.selectedFile) return;
    this.error = null;
	this.duplicateError = null;
    this.progress = 0;
    const formData = new FormData();
    formData.append("file", this.selectedFile);
    this.classificationResult = null;
    this.http.post<HttpEvent<any>>("http://localhost:8000/upload/", formData, {
      reportProgress: true,
      observe: 'events'
    }).subscribe(event => {
      if (event.type === HttpEventType.UploadProgress && event.total) { 
        this.progress = Math.round((100 * event.loaded) / event.total);
      } else if (event.type === HttpEventType.Response) { // Correct check for response type
        const response = event as HttpResponse<any>; // Cast event to HttpResponse
        if (response.body?.error && response.body.error.includes("Duplicate email detected")) {
          this.duplicateError = response.body.error;
        } else {
          this.classificationResult = response.body;
		  if(this.classificationResult.classification.primary_request === null){
			 this.classificationResult = null; 
			 this.error = "No Matching Request type found."
		  }
        }
        this.progress = -1;
      }
    }, error => {
      this.error = "Error uploading file";
      this.progress = -1;
    });
  }

  getCategories(): string[] {
    return this.classificationResult ? Object.keys(this.classificationResult.classification.classification) : [];
  }
}