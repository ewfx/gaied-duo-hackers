import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { RequestManagementComponent } from './request-management/request-management.component';
import { EmailClassifierComponent } from './email-classifier/email-classifier.component';

@NgModule({
  declarations: [
    AppComponent,
    RequestManagementComponent,
    EmailClassifierComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
	AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
