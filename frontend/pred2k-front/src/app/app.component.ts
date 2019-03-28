// import { Component } from '@angular/core';

// @Component({
//   selector: 'app-root',
//   templateUrl: './app.component.html',
//   styleUrls: ['./app.component.sass']
// })
// export class AppComponent {
//   title = 'pred2k-front';
// }


import { Component, OnInit } from '@angular/core';
import { ExpService } from './services/exp.service';
import { Observable } from 'rxjs';
// import { of } from 'rxjs/observable';
import {DataSource} from '@angular/cdk/collections';
import { Exp } from './models/exp.model';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass']
})
export class AppComponent implements OnInit {
  dataSource = new UserDataSource(this.userService);
  displayedColumns = ['post', 'salary'];
  constructor(private userService: ExpService) { }
  
  ngOnInit() {
  }
}
export class UserDataSource extends DataSource<any> {
  constructor(private userService: ExpService) {
    super();
  }
  connect(): Observable<Exp[]> {
    return this.userService.getUser();
  }
  disconnect() {}
}
