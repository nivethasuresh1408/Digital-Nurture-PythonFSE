import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { CourseCard } from '../course-card/course-card';
import { CourseService } from '../course';

@Component({
  selector: 'app-course-list',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    CourseCard
  ],
  templateUrl: './course-list.html',
  styleUrl: './course-list.css'
})
export class CourseList implements OnInit {

  courses: any[] = [];
  loading = true;
  searchTerm = '';

  constructor(private courseService: CourseService) {}

  ngOnInit(): void {

    this.loading = true;

    this.courseService.getCourses().subscribe({

      next: (data: any[]) => {

        console.log("Data received:", data);

        const courseNames = [
          "Data Structures",
          "Operating Systems",
          "Database Management",
          "Computer Networks",
          "Software Engineering"
        ];

        this.courses = data.map((post: any, index: number) => ({
          id: post.id,
          name: courseNames[index],
          code: `CS10${index + 1}`,
          credits: index % 2 === 0 ? 4 : 3,
          grade: ["A", "A+", "B+", "A", "A"][index]
        }));

        this.loading = false;

      },

      error: (err) => {

        console.log("API ERROR");
        console.log(err);

        this.loading = false;

      }

    });

  }

  get filteredCourses() {
    return this.courses.filter(course =>
      course.name.toLowerCase().includes(
        this.searchTerm.toLowerCase()
      )
    );
  }

}