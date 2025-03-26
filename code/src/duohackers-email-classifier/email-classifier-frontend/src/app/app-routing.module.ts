import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { EmailClassifierComponent } from './email-classifier/email-classifier.component';
import { RequestManagementComponent } from './request-management/request-management.component';

const routes: Routes = [
  { path: '', component: EmailClassifierComponent },
  { path: 'manage-requests', component: RequestManagementComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
