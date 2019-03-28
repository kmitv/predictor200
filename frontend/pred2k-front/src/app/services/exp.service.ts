import { Injectable }   from '@angular/core';
import { HttpClient }   from '@angular/common/http';
import { Observable }   from 'rxjs';
import { map } from 'rxjs/operators';
import { Exp } from '../models/exp.model';
@Injectable()
export class ExpService {
  private serviceUrl = 'http://127.0.0.1:8000/api/exp/?format=json';
  
  constructor(private http: HttpClient) { }
  
  getUser(): Observable<Exp[]> {
    return this.http.get<Exp[]>(this.serviceUrl);
  }
  
}