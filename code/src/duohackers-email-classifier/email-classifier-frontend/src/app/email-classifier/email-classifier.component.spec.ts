import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EmailClassifierComponent } from './email-classifier.component';

describe('EmailClassifierComponent', () => {
  let component: EmailClassifierComponent;
  let fixture: ComponentFixture<EmailClassifierComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EmailClassifierComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EmailClassifierComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
