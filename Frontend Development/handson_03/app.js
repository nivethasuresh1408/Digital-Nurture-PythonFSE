import { courses } from "./data.js";

/* ---------------- ES6 Practice ---------------- */

courses.forEach(course => {

const {name,credits}=course;

console.log(name,credits);

});

const formattedCourses=courses.map(course=>

`${course.code} — ${course.name} (${course.credits} credits)`

);

console.log(formattedCourses);

const filteredCourses=courses.filter(course=>course.credits>=4);

console.log("Courses with >=4 credits :",filteredCourses.length);

const totalCredits=courses.reduce(

(total,course)=>total+course.credits,

0

);

console.log("Total Credits :",totalCredits);

/* ---------------- DOM ---------------- */

const courseGrid=document.querySelector(".course-grid");

const totalCreditsText=document.querySelector("#total-credits");

const selectedCourse=document.querySelector("#selected-course");

const searchInput=document.querySelector("#search-courses");

const sortButton=document.querySelector("#sort-btn");

/* ---------------- Render Function ---------------- */

function renderCourses(courseArray){

courseGrid.innerHTML="";

courseArray.forEach(course=>{

const article=document.createElement("article");

article.className="course-card";

article.dataset.id=course.id;

article.innerHTML=`

<h3>${course.name}</h3>

<p><strong>Course Code:</strong> ${course.code}</p>

<p><strong>Credits:</strong> ${course.credits}</p>

`;

courseGrid.appendChild(article);

});

totalCreditsText.textContent=

`Total Credits Enrolled : ${courseArray.reduce((sum,c)=>sum+c.credits,0)}`;

}

/* ---------------- Initial Render ---------------- */

renderCourses(courses);

/* ---------------- Search ---------------- */

searchInput.addEventListener("input",()=>{

const keyword=searchInput.value.toLowerCase();

const filtered=courses.filter(course=>

course.name.toLowerCase().includes(keyword)

);

renderCourses(filtered);

});

/* ---------------- Sort ---------------- */

sortButton.addEventListener("click",()=>{

const sorted=[...courses].sort(

(a,b)=>b.credits-a.credits

);

renderCourses(sorted);

});

/* ---------------- Event Delegation ---------------- */

courseGrid.addEventListener("click",(event)=>{

const card=event.target.closest(".course-card");

if(!card)return;

const id=Number(card.dataset.id);

const course=courses.find(c=>c.id===id);

selectedCourse.innerHTML=`

<h3>Selected Course</h3>

<p>

<strong>${course.name}</strong>

</p>

<p>

Grade : ${course.grade}

</p>

`;

});