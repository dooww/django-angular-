import { Component } from '@angular/core';
import {ApplyService }from './apply.service'
//import {Applicaion} from './application'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})

export class AppComponent {



  constructor(private _applyservice: ApplyService){}
  //applicationmodel= new Applicaion();

  title = 'mysite-front';
}
