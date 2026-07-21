import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, tap } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CourseService {

  constructor(private http: HttpClient) {}

  getCourses(): Observable<any[]> {
    console.log('CourseService Called');

    return this.http
      .get<any[]>('https://jsonplaceholder.typicode.com/posts?_limit=5')
      .pipe(
        tap(data => {
          console.log('API Returned');
          console.log(data);
        })
      );
  }
}