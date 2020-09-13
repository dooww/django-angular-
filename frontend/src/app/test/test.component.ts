import { Component, OnInit } from '@angular/core';
import { Validators,FormsModule } from '@angular/forms';
import{NgModule} from '@angular/core';
import{ApplyService} from '../apply.service'
import { Application }from '../application'


@Component({
  selector: 'app-test',
  templateUrl: './test.component.html',
  styleUrls: ['./test.component.scss']
})
export class TestComponent implements OnInit {



  constructor(private _applyservice: ApplyService){}

  ngOnInit(): void {
  }

  selectfile(event){
    this.applicationModel=event.target.files[0]
     
  }


  submitted=false;
  applicationModel= new Application('','','','',null,'',0,'',null)
  onSubmit(){
    this._applyservice.apply(this.applicationModel)
    .subscribe(
    data => console.log('success',data),
    error => console.error()
    )
    this.submitted=true
    
  }

}
