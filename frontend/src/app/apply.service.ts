import { Injectable } from '@angular/core';
import{HttpClient} from '@angular/common/http'
import { Application } from './application';

@Injectable({
  providedIn: 'root'
})
export class ApplyService {

  _url='http://127.0.0.1:8000/application';

  constructor ( private _http : HttpClient) { }
  apply(application:Application)
  {
    return this._http.post<any>(this._url,application);
  }

}
